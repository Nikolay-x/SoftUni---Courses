from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        verbose_name='Age',
        validators=(
            MinValueValidator(12),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=30,
        null=False,
        blank=False,
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


class Game(models.Model):
    Action = 'Action'
    Adventure = 'Adventure'
    Puzzle = 'Puzzle'
    Strategy = 'Strategy'
    Sports = 'Sports'
    Board_Card_Game = 'Board/Card Game'
    Other = 'Other'

    GAMES_TYPE = (
        (Action, Action),
        (Adventure, Adventure),
        (Puzzle, Puzzle),
        (Strategy, Strategy),
        (Sports, Sports),
        (Board_Card_Game, Board_Card_Game),
        (Other, Other),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=15,
        choices=GAMES_TYPE,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
        null=True,
        blank=True,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
