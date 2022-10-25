from enum import Enum

from django.core.exceptions import ValidationError
from django.core import validators
from django.db import models

# Create your models here.


def letters_numbers_val(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    username = models.CharField(
        verbose_name='Username',
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            letters_numbers_val,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


# # With enums
# class ChoicesEnum(Enum):
#     @classmethod
#     def choices(cls):
#         return [(x.name, x.value) for x in cls]
#
#
# class AlbumGenres(ChoicesEnum):
#     POP = 'Pop Music'
#     JAZZ = "Jazz Music"
#     RNB = "R&B Music"
#     ROCK = "Rock Music"
#     COUNTRY = "Country Music"
#     DANCE = "Dance Music"
#     HIP_HOP = "Hip Hop Music"
#     OTHER = "Other"


class Album(models.Model):
    Pop = "Pop Music"
    Jazz = "Jazz Music"
    RNB = "R&B Music"
    Rock = "Rock Music"
    Country = "Country Music"
    Dance = "Dance Music"
    HipHop = "Hip Hop Music"
    Other = "Other"

    GENRES = (
        (Pop, Pop),
        (Jazz, Jazz),
        (RNB, RNB),
        (Rock, Rock),
        (Country, Country),
        (Dance, Dance),
        (HipHop, HipHop),
        (Other, Other),
    )

    album_name = models.CharField(
        verbose_name='Album Name',
        unique=True,
        max_length=30,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        verbose_name='Artist',
        max_length=30,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        verbose_name='Genre',
        max_length=30,
        choices=GENRES,
        # choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=(
            validators.MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )
