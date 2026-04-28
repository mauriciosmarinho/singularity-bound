from django.shortcuts import render, redirect
from django.core.management import call_command
from io import StringIO
from django.contrib import messages
from players.models import Commander
from turns.models import Turn
from core.models import Faction, Sector, Fleet
from core.services.turn_engine import TurnEngine


def dashboard(request):

    commander = Commander.objects.first()
    turn = Turn.objects.order_by("-number").first()
    factions = Faction.objects.all()
    sectors = Sector.objects.all()
    fleets = Fleet.objects.all()

    context = {
        "commander": commander,
        "turn": turn,
        "factions": factions,
        "sectors": sectors,
        "fleets": fleets,
    }

    return render(request, "interface/dashboard.html", context)


def next_turn_web(request):
    if request.method == "POST":
        out = StringIO()
        call_command(
            "next_turn",
            stdout=out
        )
        aura_text = out.getvalue()
        messages.success(request, aura_text)
        #TurnEngine().run()
    return redirect("dashboard")

def explore_sector_web(request):
    if request.method == "POST":
        out = StringIO()
        call_command(
            "explore_sector",
            stdout=out
        )
        aura_text = out.getvalue()
        messages.success(request, aura_text)
    return redirect("dashboard")

def sectors_report_web(request):
    if request.method == "POST":
        out = StringIO()
        call_command(
            "sectors_report",
            stdout=out
        )
        aura_text = out.getvalue()
        messages.success(request, aura_text)
    return redirect("dashboard")

def colonize_web(request):
    if request.method =="POST":
        out = StringIO()
        call_command("colonize_sector", 
            request.POST['fleet_name'], 
            request.POST['sector_name'],
            stdout=out
        )
        aura_text = out.getvalue()
        messages.success(request, aura_text)
    return redirect("dashboard")

def fleet_web(request):
    if request.method == "POST":
        call_command("build_fleet")
    return redirect("dashboard")

def research_web(request):
    if request.method == "POST":
        call_command("start_research")
    return redirect("dashboard")

def spy_web(request, faction_name):
    if request.method == "POST":
        out = StringIO()

        call_command(
            "spy_on",
            faction_name,
            stdout=out
        )

        aura_text = out.getvalue()

        messages.success(request, aura_text)

    return redirect("dashboard")

def negotiate_web(request):
    if request.method == "POST":
        call_command("negotiate")
    return redirect("dashboard")

def attack_web(request):
    if request.method =="POST":
        out = StringIO()
        call_command("attack_faction", 
            request.POST['fleet_name'], 
            request.POST['faction_name'],
            stdout=out
        )
        aura_text = out.getvalue()
        messages.success(request, aura_text)
    return redirect("dashboard")