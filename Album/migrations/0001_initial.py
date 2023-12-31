# Generated by Django 4.2.7 on 2023-12-17 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ablum_name', models.CharField(help_text='Album Names', max_length=100)),
                ('album_release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.mymusicianmodel')),
            ],
        ),
    ]
