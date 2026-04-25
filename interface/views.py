from django.shortcuts import render, redirect

from players.models import Commander
from turns.models import Turn
from core.models import Faction, Sector
from core.services.turn_engine import TurnEngine


def dashboard(request):

    commander = Commander.objects.first()
    turn = Turn.objects.order_by("-number").first()
    factions = Faction.objects.all()
    sectors = Sector.objects.all()

    context = {
        "commander": commander,
        "turn": turn,
        "factions": factions,
        "sectors": sectors,
    }

    return render(request, "interface/dashboard.html", context)


def next_turn_web(request):

    engine = TurnEngine()
    engine.run()

    return redirect("dashboard")