from django.urls import path
from .views import ping, get_schema_json, validate_sql_syntax

urlpatterns = [
    path('ping', ping, name="ping"),
    path('get_schema_json', get_schema_json, name="get_schema_json"),
    path('validate_sql_syntax', validate_sql_syntax, name="validate_sql_syntax")
]