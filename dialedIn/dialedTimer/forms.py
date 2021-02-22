from django.forms import ModelForm
from .models import Coffee, Extraction


class CoffeeCreationForm(ModelForm):
    class Meta:
        model = Coffee
        fields = ['coffee_name', 'roaster_name', 'roast_level']


class ExtractionForm(ModelForm):
    class Meta:
        model = Extraction
        fields = ['user_id', 'coffee_id', 'timestamp', 'extraction_length', 'mass_in', 'mass_out', 'notes']
