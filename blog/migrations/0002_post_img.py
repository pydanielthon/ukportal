# Generated by Django 3.0.3 on 2020-04-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='static/img/backgrounds/img-2.jpg', upload_to='media'),
        ),
    ]
