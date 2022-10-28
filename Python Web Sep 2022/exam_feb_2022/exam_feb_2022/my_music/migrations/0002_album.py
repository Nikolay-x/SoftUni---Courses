# Generated by Django 4.1.2 on 2022-10-25 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True, verbose_name='Album Name')),
                ('artist', models.CharField(max_length=30, verbose_name='Artist')),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30, verbose_name='Genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
            ],
        ),
    ]