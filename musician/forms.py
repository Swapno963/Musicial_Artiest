from django import forms
from .models import MyMusicianModel

class MyMusicianForm(forms.ModelForm):
    class Meta:
        model = MyMusicianModel
        fields = '__all__'
