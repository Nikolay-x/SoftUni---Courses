from django.db import models
from django.urls import reverse


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    seniority_level = models.CharField(
        max_length=30,
        choices=(
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
            ('Senior', 'Senior'),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse('employee details', kwargs={'pk': self.pk})