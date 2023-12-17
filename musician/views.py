from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MyMusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            redirect('homepage')
    else:
        musician_form = forms.MyMusicianForm()

    return render(request,'musician.html', {'musician_form':musician_form})



def edit_musician(request, id):
    musician = models.MyMusicianModel.objects.get(pk = id)
    musician_form = forms.MyMusicianForm(instance=musician)

    if request.method == 'POST':
        musician_form = forms.MyMusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    return render(request,'musician.html', {'musician_form':musician_form})


def delete_musician(request, id):
    musician = models.MyMusicianModel.objects.get(pk = id)
    musician.delete()
    return redirect('hompage')