from django.forms import ModelForm
from .models import Coffee
class CoffeeCreationForm(ModelForm):
    class Meta:
        model = Coffee
        fields = ['coffee_name', 'roaster_name', 'roast_level']
