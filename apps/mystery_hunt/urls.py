from django.urls import path
from . import views

app_name = "mystery_hunt"

urlpatterns = [
	path("", views.index, name="index"),
	path("all", views.all, name="all"),
	path("process", views.process, name="process"),
	path("show/<int:pred_id>", views.show_one, name="show"),
	path("get_stats", views.get_stats, name="get_stats"),
]