# pets/models.py

from django.db import models
from django.utils.text import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin


# Create your models here.


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name',)

    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        # Without 'if not' the following scenario might happen:
        # The url is '/pets/4-stamat'
        # Rename 'stamat' to 'stamata'
        # The new url is '/pets/4-stamata', but the old url '/pets/4-stamat' does not work

        # Update
        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'ID={self.id}, Name={self.name}'
