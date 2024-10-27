from django.shortcuts import render

import tensorflow as tf
import numpy as np
from .forms import DiabetesPredictionForm  # Créez un formulaire pour les prédictions
from .forms import CancerPredictionForm 
from .models import preprocess_input  # Fonction de prétraitement des données

from pathlib import Path
from django.conf import settings  # Pour accéder à BASE_DIR

import csv

# Charger les modèles avec le chemin absolu
model_bc = tf.keras.models.load_model(Path(settings.BASE_DIR) / 'models_app' / 'models_app' / 'models' / 'best_model_bc.h5.keras')
model_dia = tf.keras.models.load_model(Path(settings.BASE_DIR) / 'models_app' / 'models_app' / 'models' / 'best_model_dia.h5.keras')

def handle_uploaded_file(file):
    """Fonction pour traiter le fichier CSV téléchargé"""
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    data = list(reader)
    return np.array(data).astype(float)

def predict_cancer(request):
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST, request.FILES)  # Gérer les fichiers également
        if form.is_valid():
            input_data = form.cleaned_data['input_data']
            uploaded_file = form.cleaned_data['file_upload']

            if uploaded_file:
                processed_data = handle_uploaded_file(uploaded_file)
                if processed_data.shape[1] != 30:
                    return render(request, 'models_app/error.html', {'message': 'Le fichier CSV doit contenir exactement 30 colonnes.'})
            elif input_data:
                processed_data = preprocess_input(input_data)
            else:
                return render(request, 'models_app/error.html', {'message': 'Veuillez entrer des données ou télécharger un fichier.'})

            # Effectuer la prédiction
            prediction = model_bc.predict(processed_data)
            result = "Malignant" if prediction[0] > 0.5 else "Benign"
            return render(request, 'models_app/result.html', {'result': result})
    else:
        form = CancerPredictionForm()

    return render(request, 'models_app/predict_cancer.html', {'form': form})

def predict_diabetes(request):
    if request.method == 'POST':
        form = DiabetesPredictionForm(request.POST, request.FILES)  # Gérer les fichiers également
        if form.is_valid():
            input_data = form.cleaned_data['input_data']
            uploaded_file = form.cleaned_data['file_upload']

            if uploaded_file:
                processed_data = handle_uploaded_file(uploaded_file)
                if processed_data.shape[1] != 8:
                    return render(request, 'models_app/error.html', {'message': 'Le fichier CSV doit contenir exactement 8 colonnes.'})
            elif input_data:
                processed_data = preprocess_input(input_data)
            else:
                return render(request, 'models_app/error.html', {'message': 'Veuillez entrer des données ou télécharger un fichier.'})

            # Effectuer la prédiction
            prediction = model_dia.predict(processed_data)
            result = "Diabetic" if prediction[0] > 0.5 else "Not Diabetic"
            return render(request, 'models_app/result.html', {'result': result})
    else:
        form = DiabetesPredictionForm()

    return render(request, 'models_app/predict_diabetes.html', {'form': form})