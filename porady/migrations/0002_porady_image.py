# Generated by Django 3.0.3 on 2020-05-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porady', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porady',
            name='image',
            field=models.ImageField(default='static/img/backgrounds/img-2.jpg', upload_to='media/porady'),
        ),
    ]
