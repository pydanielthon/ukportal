# Generated by Django 3.0.3 on 2020-05-04 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='podstawowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('miasto', models.CharField(max_length=100)),
                ('numer', models.FloatField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='katalog/%Y/%m/%d')),
                ('www', models.CharField(max_length=400)),
                ('fb', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram', models.CharField(blank=True, max_length=250, null=True)),
                ('maps', models.CharField(blank=True, max_length=250, null=True)),
                ('kategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='podstawowy', to='katalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='darmowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('miasto', models.CharField(max_length=100)),
                ('numer', models.FloatField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='katalog/%Y/%m/%d')),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='darmowy', to='katalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='katalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='katalog/%Y/%m/%d')),
                ('adres', models.CharField(max_length=300, null=True)),
                ('telefon', models.FloatField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('www', models.CharField(blank=True, max_length=150, null=True)),
                ('fb', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram', models.CharField(blank=True, max_length=250, null=True)),
                ('maps', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='katalog', to='katalog.Category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
