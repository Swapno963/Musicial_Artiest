from django.db import models

# Create your models here.
class MyMusicianModel(models.Model):
    first_name = models.CharField(help_text='First Name', max_length=100)
    lastt_name = models.CharField(help_text='Last Name', max_length=100)
    email = models.CharField(help_text='Email', max_length=100)
    phone_num = models.CharField(help_text='Phone number', max_length=100)
    instument_type = models.CharField(help_text='Instrument Type', max_length=100)

    def __str__(self) -> str:
        return self.first_name