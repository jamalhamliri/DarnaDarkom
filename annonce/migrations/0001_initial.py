# Generated by Django 4.2.4 on 2023-08-30 18:20

import annonce.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='Location')),
                ('type', models.CharField(choices=[('Offre', 'OFFRE'), ('Demande', 'DEMANDE')], max_length=50)),
                ('type_hebergement', models.CharField(blank=True, choices=[('Hotel', 'HOTEL'), ('Maison', 'MAISON')], max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/annonce', validators=[annonce.validators.file_size])),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='nom de pays')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_name', models.CharField(max_length=255, unique=True, verbose_name='ville name')),
                ('pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pays', to='annonce.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annonce.annonce')),
            ],
        ),
    ]
