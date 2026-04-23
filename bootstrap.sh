#!/usr/bin/env bash
set -e

# Caminho do projeto
PROJECT_DIR="$PWD"

# Funções -----------------------------------------------------

create_conda_env() {
    echo "=== Criando ambiente Conda ==="
    conda create -y -n game python=3.12
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate game
    echo "Ambiente 'game' criado e ativado."
}

install_python_deps() {
    echo "=== Instalando dependências Python ==="
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate game
    pip install --upgrade pip
    pip install \
        django \
        djangorestframework \
        celery \
        redis \
        psycopg2-binary \
        python-dotenv \
        django-environ \
        black \
        ruff \
        pytest \
        django-extensions
}

install_system_deps() {
    echo "=== Instalando PostgreSQL e Redis ==="
    sudo apt update
    sudo apt install -y postgresql postgresql-contrib redis-server
}

create_database() {
    echo "=== Criando banco de dados PostgreSQL ==="
    sudo -u postgres psql <<EOF
CREATE DATABASE game;
CREATE USER gameuser WITH PASSWORD 'gamepass';
ALTER ROLE gameuser SET client_encoding TO 'utf8';
ALTER ROLE gameuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE gameuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE game TO gameuser;
EOF
}

create_django_project() {
    echo "=== Criando projeto Django ==="
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate game

    django-admin startproject game .

    SECRET=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

    cat > .env <<EOF
DEBUG=True
SECRET_KEY=$SECRET
DATABASE_URL=postgres://gameuser:gamepass@localhost:5432/game
REDIS_URL=redis://localhost:6379/0
EOF

    cp .env .env.example
    sed -i 's/SECRET_KEY=.*/SECRET_KEY=CHANGEME/' .env.example

    SETTINGS="game/settings.py"

    # Inserir no topo
    sed -i "1i import environ" $SETTINGS
    sed -i "2i env = environ.Env()" $SETTINGS
    sed -i "3i environ.Env.read_env()" $SETTINGS

    # Substituir SECRET_KEY e DEBUG
    sed -i "s/^SECRET_KEY = .*/SECRET_KEY = env('SECRET_KEY')/" $SETTINGS
    sed -i "s/^DEBUG = .*/DEBUG = env.bool('DEBUG')/" $SETTINGS

    # Adicionar DB e Redis
    cat >> $SETTINGS <<EOF

DATABASES = {
    'default': env.db(),
}

CELERY_BROKER_URL = env('REDIS_URL')
CELERY_RESULT_BACKEND = env('REDIS_URL')
EOF
}

run_migrations() {
    echo "=== Aplicando migrações ==="
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate game
    python manage.py migrate
}

# Menu --------------------------------------------------------

while true; do
    clear
    echo "==========================================="
    echo " Singularity Bound — Bootstrap do Projeto"
    echo " Diretório atual: $PROJECT_DIR"
    echo "==========================================="
    echo ""
    echo "Escolha uma opção:"
    echo "1) Criar ambiente Conda"
    echo "2) Instalar dependências Python"
    echo "3) Instalar PostgreSQL e Redis"
    echo "4) Criar banco de dados"
    echo "5) Criar projeto Django"
    echo "6) Aplicar migrações"
    echo "7) Executar tudo (1 → 6)"
    echo "0) Sair"
    echo ""
    read -p "Opção: " opt

    case $opt in
        1) create_conda_env ;;
        2) install_python_deps ;;
        3) install_system_deps ;;
        4) create_database ;;
        5) create_django_project ;;
        6) run_migrations ;;
        7)
            create_conda_env
            install_python_deps
            install_system_deps
            create_database
            create_django_project
            run_migrations
            ;;
        0) echo "Saindo."; exit 0 ;;
        *) echo "Opção inválida."; sleep 1 ;;
    esac

    echo ""
    read -p "Pressione ENTER para voltar ao menu..."
done
