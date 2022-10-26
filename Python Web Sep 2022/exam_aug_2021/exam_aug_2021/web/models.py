from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=30,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )


class Book(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=30,
    )

    description = models.TextField(
        verbose_name='Description',
    )

    image = models.URLField(
        verbose_name='Image',
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=30,
    )

    class Meta:
        ordering = ('pk',)
