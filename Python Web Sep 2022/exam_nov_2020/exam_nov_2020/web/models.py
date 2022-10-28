from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=30,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    ingredients = models.CharField(
        verbose_name='Ingredients',
        max_length=250,
    )

    time = models.IntegerField(
        verbose_name='Time',
    )

    class Meta:
        ordering = ('pk',)
