import os
import uuid

from django.db import models

from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


# Create your models here.


class Person(models.Model):
    MAX_LEN_NAME = 20

    # def get_file_path(self, filename):
    #     ext = filename.split('.')[-1]
    #     filename = f"{self.name}-{uuid.uuid4()}.{ext}"
    #     return os.path.join('persons', filename)

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    profile_image = models.ImageField(
        upload_to='persons',
        # upload_to=get_file_path,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3
    MAX_LEN_TEXT = 25

    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
