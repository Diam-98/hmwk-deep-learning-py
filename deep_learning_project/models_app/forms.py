from django import forms

class CancerPredictionForm(forms.Form):
    input_data = forms.CharField(
        label='Entrez les caractéristiques séparées par des virgules',
        widget=forms.Textarea(attrs={'placeholder': '14.2,20.5,91.6,...,0.089'}),
        required=False  # Champ non obligatoire si un fichier est uploadé
    )
    
    file_upload = forms.FileField(
        label='Ou téléchargez un fichier CSV avec les caractéristiques',
        required=False,  # Le fichier est facultatif si les données sont saisies manuellement
        widget=forms.ClearableFileInput(attrs={'accept': '.csv'})  # Limiter les fichiers acceptés aux CSV
    )
    
    def clean_input_data(self):
        input_data = self.cleaned_data.get('input_data')
        
        if input_data:
            # Diviser la chaîne de texte par des virgules et convertir en liste de flottants
            try:
                data_list = [float(x) for x in input_data.split(',')]
            except ValueError:
                raise forms.ValidationError('Toutes les valeurs doivent être des nombres.')
            
            # Vérifier que nous avons bien 30 caractéristiques pour le cancer
            if len(data_list) != 30:
                raise forms.ValidationError('Vous devez entrer exactement 30 valeurs séparées par des virgules.')
        
        return input_data

    def clean_file_upload(self):
        file_upload = self.cleaned_data.get('file_upload')
        
        if file_upload:
            if not file_upload.name.endswith('.csv'):
                raise forms.ValidationError('Le fichier doit être un fichier CSV.')
            
            # Vous pouvez ajouter des validations supplémentaires sur la taille du fichier ici si nécessaire
            # file_upload.size pour vérifier la taille du fichier

        return file_upload

    def clean(self):
        cleaned_data = super().clean()
        input_data = cleaned_data.get('input_data')
        file_upload = cleaned_data.get('file_upload')
        
        # Assurez-vous que l'utilisateur a rempli au moins l'un des deux champs (input_data ou file_upload)
        if not input_data and not file_upload:
            raise forms.ValidationError('Veuillez entrer des données manuellement ou télécharger un fichier CSV.')
        
        return cleaned_data


from django import forms

class DiabetesPredictionForm(forms.Form):
    input_data = forms.CharField(
        label='Entrez les caractéristiques séparées par des virgules',
        widget=forms.Textarea(attrs={'placeholder': '6,148,72,35,0,33.6,0.627,50'}),
        required=False  # Champ non obligatoire si un fichier est uploadé
    )
    
    file_upload = forms.FileField(
        label='Ou téléchargez un fichier CSV avec les caractéristiques',
        required=False,  # Le fichier est facultatif si les données sont saisies manuellement
        widget=forms.ClearableFileInput(attrs={'accept': '.csv'})  # Limiter les fichiers acceptés aux CSV
    )
    
    def clean_input_data(self):
        input_data = self.cleaned_data.get('input_data')
        
        if input_data:
            # Diviser la chaîne de texte par des virgules et convertir en liste de flottants
            try:
                data_list = [float(x) for x in input_data.split(',')]
            except ValueError:
                raise forms.ValidationError('Toutes les valeurs doivent être des nombres.')
            
            # Vérifier que nous avons bien 8 caractéristiques pour le diabète
            if len(data_list) != 8:
                raise forms.ValidationError('Vous devez entrer exactement 8 valeurs séparées par des virgules.')
        
        return input_data

    def clean_file_upload(self):
        file_upload = self.cleaned_data.get('file_upload')
        
        if file_upload:
            if not file_upload.name.endswith('.csv'):
                raise forms.ValidationError('Le fichier doit être un fichier CSV.')
            
        return file_upload

    def clean(self):
        cleaned_data = super().clean()
        input_data = cleaned_data.get('input_data')
        file_upload = cleaned_data.get('file_upload')
        
        # Assurez-vous que l'utilisateur a rempli au moins l'un des deux champs (input_data ou file_upload)
        if not input_data and not file_upload:
            raise forms.ValidationError('Veuillez entrer des données manuellement ou télécharger un fichier CSV.')
        
        return cleaned_data
