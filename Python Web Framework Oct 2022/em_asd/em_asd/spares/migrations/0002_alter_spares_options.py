# Generated by Django 4.1.3 on 2022-12-09 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spares', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spares',
            options={'ordering': ('ref_doc_code',), 'verbose_name_plural': 'Spares'},
        ),
    ]
