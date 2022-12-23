from django.core.exceptions import ValidationError


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def car_year_validator(value):
    if value < 1980 or 2049 < value:
        raise ValidationError('Year must be between 1980 and 2049')
