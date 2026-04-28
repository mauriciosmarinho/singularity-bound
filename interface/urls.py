from django.urls import path
from .views import (
    dashboard, 
    next_turn_web,
    explore_sector_web,
    sectors_report_web,
    colonize_web,
    fleet_web,
    research_web,
    spy_web,
    negotiate_web,
    attack_web, 
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("next-turn/", next_turn_web, name="next_turn_web"),
    path("sectors-report/", sectors_report_web, name="sectors_report_web"),
    path("explore-sector/", explore_sector_web, name="explore_sector_web"),
    path("colonize/", colonize_web, name="colonize_web"),
    path("fleet/", fleet_web, name="fleet_web"),
    path("research/", research_web, name="research_web"),
    path("spy/<str:faction_name>/", spy_web, name="spy_web"),
    path("negotiate/", negotiate_web, name="negotiate_web"),
    path("attack/", attack_web, name="attack_web"),
]