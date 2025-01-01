from django.urls import path
from . import views

urlpatterns = [
    path('', views.CostList.as_view(), name='cost-list'),
]
