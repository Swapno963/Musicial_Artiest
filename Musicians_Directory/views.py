from django.shortcuts import render
from Album.models import MyAlbumModel
def homepage(request):
    data = MyAlbumModel.objects.all()
    return render(request, 'homepage.html',{'data':data})
