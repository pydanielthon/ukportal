# Generated by Django 3.0.3 on 2020-05-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porady', '0002_porady_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoradyVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=200)),
                ('film', models.CharField(max_length=700)),
            ],
        ),
    ]
