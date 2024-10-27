# models_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_cancer, name='predict_cancer'),
    path('predict-cancer/', views.predict_cancer, name='predict_cancer'),
    path('predict-diabetes/', views.predict_diabetes, name='predict_diabetes'),
]
