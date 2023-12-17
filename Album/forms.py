from django import forms 
from .models import MyAlbumModel
class MyAlbumForm(forms.ModelForm):
    class Meta:
        model = MyAlbumModel
        fields = '__all__'
        
