# Generated by Django 3.0.3 on 2020-05-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_remove_katalog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='katalog/%Y/%m/%d'),
        ),
    ]