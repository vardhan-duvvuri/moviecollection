"""Form file."""
from django import forms
from collection.models import Movie


class MovieForm(forms.ModelForm):
    """Movie form."""
    class Meta:
        model = Movie
        fields = ('__all__')
