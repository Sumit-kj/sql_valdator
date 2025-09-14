from django.urls import path
from .views import ping, get_schema_json

urlpatterns = [
    path('ping', ping, name="ping"),
    path('get_schema_json', get_schema_json, name="get_schema_json")
]