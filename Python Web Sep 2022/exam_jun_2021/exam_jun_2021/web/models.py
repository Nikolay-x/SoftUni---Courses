from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=20,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=20,
    )

    age = models.PositiveIntegerField(
        verbose_name='Age'
    )

    image_url = models.URLField(
        verbose_name='Link to Profile Image',
    )


class Note(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=30,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    content = models.TextField(
        verbose_name='Content',
    )

    class Meta:
        ordering = ('pk',)
