from django.urls import path
from .views import dashboard, next_turn_web

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("next-turn/", next_turn_web, name="next_turn_web"),
]