from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CoffeeCreationForm(forms.Form):
    coffee_name = forms.CharField()
    roaster_name = forms.CharField()
    roast_level = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'coffeeForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'home'

        self.helper.add_input(Submit('submit', 'Submit'))
