# Generated by Django 4.1.1 on 2022-10-06 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_alter_employee_options_accesscard_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
