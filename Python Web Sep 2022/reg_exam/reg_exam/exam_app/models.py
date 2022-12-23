from django.core import validators
from django.db import models

from reg_exam.exam_app.validators import min_length_validator, car_year_validator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        verbose_name='Username',
        max_length=10,
        validators=(
            min_length_validator,
        )
    )

    email = models.EmailField(
        verbose_name='Email',
    )

    age = models.IntegerField(
        verbose_name="Age",
        validators=(
            validators.MinValueValidator(18),
        )
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=30,
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=10,
        choices=CAR_TYPES,
    )

    model = models.CharField(
        verbose_name='Model',
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
        )
    )

    year = models.IntegerField(
        verbose_name='Year',
        validators=(
            car_year_validator,
        ),
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=(
            validators.MinValueValidator(1),
        ),
    )

    class Meta:
        ordering = ('pk',)
