from django.db import models
import numpy as np

def preprocess_input(data):
    # Convertir les données du formulaire en tableau compatible avec le modèle
    data_array = np.array([float(i) for i in data.split(',')]).reshape(1, -1)
    # print(data_array)
    return data_array



