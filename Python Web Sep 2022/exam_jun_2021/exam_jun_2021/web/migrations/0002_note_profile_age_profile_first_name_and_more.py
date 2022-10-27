# Generated by Django 4.1.2 on 2022-10-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.AddField(
            model_name='profile_page',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile_page',
            name='first_name',
            field=models.CharField(default=None, max_length=20, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile_page',
            name='image_url',
            field=models.URLField(default=None, verbose_name='Image URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile_page',
            name='last_name',
            field=models.CharField(default=None, max_length=20, verbose_name='Last Name'),
            preserve_default=False,
        ),
    ]
