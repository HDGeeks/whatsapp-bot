from django.urls import path
from . import views

urlpatterns = [
    path('survey', views.survey, name='survey'),
]
#https://5dd4-169-150-218-25.eu.ngrok.io/bot/survey