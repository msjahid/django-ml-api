from django.urls import path
from . import views

urlpatterns = [
    path('salary-prediction/', views.SalaryPredictionView.as_view()),
]