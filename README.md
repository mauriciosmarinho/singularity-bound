# Singularity Bound

**Grand Strategy Sci-Fi em Terminal**, desenvolvido com **Python + Django + PostgreSQL**.

Singularity Bound é um jogo de estratégia por turnos onde você lidera um império espacial em expansão, administra recursos críticos, enfrenta facções rivais e toma decisões capazes de moldar o destino da galáxia.

---

# Visão Geral

Em um universo fragmentado após séculos de colapso interestelar, novas potências emergem entre ruínas tecnológicas e sistemas abandonados.

Você assume o comando de uma civilização nascente e precisa equilibrar:

* Expansão territorial
* Economia colonial
* Pesquisa científica
* Moral interna
* Reputação política
* Guerra e espionagem
* Relações diplomáticas

Cada turno gera novas oportunidades, ameaças e consequências históricas.

---

# Principais Features

## Estratégia por Turnos

* Progressão diária por comandos de turno
* Crescimento contínuo do império
* Eventos dinâmicos

## Economia Viva

* Colônias produzem recursos automaticamente
* Gestão de fuel, minerals e science
* Expansão acelera crescimento

## Rival Autônomo

* Facções inimigas agem sozinhas
* Colonizam setores
* Fazem propaganda hostil
* Escalam militarmente

## Guerra Invisível

* Espionagem
* Sabotagem
* Inteligência estratégica

## Liderança Imperial

Recrute líderes únicos:

* **Almirante Vega** → foco militar
* **Ministra Lyra** → foco econômico
* **Cientista Orion** → foco científico

## Eventos Lendários

Eventos raros podem alterar completamente a campanha:

* IA ancestral desperta
* Guerra civil rival
* Colapso estelar
* Megadepósitos minerais
* Cultos tecnocráticos

---

# Tecnologias Utilizadas

* Python 3.12
* Django
* PostgreSQL
* Conda
* Git / GitHub

---

# Instalação

## 1. Clonar repositório

```bash
git clone https://github.com/mauriciosmarinho/singularity-bound.git
cd singularity-bound
```

## 2. Criar ambiente

```bash
conda create -n game python=3.12
conda activate game
```

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Configurar banco PostgreSQL

Crie banco e usuário compatíveis com o arquivo `.env`.

## 5. Rodar migrations

```bash
python manage.py migrate
```

## 6. Popular universo inicial

```bash
python manage.py seed_universe
```

---

# Como Jogar

## Painel principal

```bash
python manage.py play
```

## Avançar turno

```bash
python manage.py next_turn
```

## Ver mapa galáctico

```bash
python manage.py sectors_report
```

## Explorar novos setores

```bash
python manage.py explore_sector
```

## Colonizar setor

```bash
python manage.py colonize_sector X-497
```

## Pesquisa científica

```bash
python manage.py start_research warp_drive
```

## Espionagem

```bash
python manage.py spy_on "Clã Draconis"
```

## Sabotagem

```bash
python manage.py sabotage_sector D-815
```

## Conselho Imperial

```bash
python manage.py leaders_report
python manage.py recruit_leader lyra
```

---

# Condições de Vitória

* Alta reputação galáctica
* Domínio territorial
* Neutralização rival

# Condições de Derrota

* Colapso logístico
* Moral zerada
* Supremacia rival

---

# Roadmap Futuro

## Semana 4+

* Interface web Django
* Mapa visual interativo
* Diplomacia avançada
* Combate expandido
* Save/load de campanhas
* IA rival aprimorada
* Eventos narrativos maiores

---

# Filosofia do Projeto

Singularity Bound nasceu como experimento técnico e evoluiu para um sandbox estratégico emergente.

O foco do projeto é combinar:

* Sistemas interligados
* Progressão contínua
* Narrativas espontâneas
* Decisões com consequências

---

# Status Atual

**Versão jogável em terminal**
Em desenvolvimento ativo.

---

# Autor

Mauricio da Silva Marinho

---

# Licença

Projeto autoral para fins educacionais e experimentais.
