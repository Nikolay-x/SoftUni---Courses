# Generated by Django 4.1.1 on 2022-10-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employee_level_alter_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]