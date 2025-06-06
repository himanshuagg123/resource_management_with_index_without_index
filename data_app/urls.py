# data_app/urls.py
from django.urls import path
from .views import query_performance_test

urlpatterns = [
    path('run-query/', query_performance_test, name='query_performance_test'),
]
