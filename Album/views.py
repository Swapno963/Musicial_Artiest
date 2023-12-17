from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.MyAlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            redirect('homepage')
    else:
        album_form = forms.MyAlbumForm()

    return render(request,'album.html', {'album_form':album_form})



def edit_album(request, id):
    album = models.MyAlbumModel.objects.get(pk = id)
    album_form = forms.MyAlbumForm(instance=album)

    if request.method == 'POST':
        album_form = forms.MyAlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    return render(request,'album.html', {'album_form':album_form})


def delete_album(request, id):
    album = models.MyAlbumModel.objects.get(pk = id)
    album.delete()
    return redirect('homepage')