from django.db import models
from musician.models import MyMusicianModel
# Create your models here.
class MyAlbumModel(models.Model):
    ablum_name = models.CharField(help_text='Album Names', max_length=100)
    musician = models.ForeignKey(MyMusicianModel, on_delete=models.CASCADE)
    album_release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.ablum_name