from django import forms

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
class ExperienceForm(forms.Form):
    years_of_experience = forms.IntegerField(
        label='Years of Experience',
        validators=[
            MinValueValidator(0, message='Years of experience must be greater than or equal to 0.'),
            MaxValueValidator(20, message='Years of experience must be less than or equal to 89.')
        ]
    )
