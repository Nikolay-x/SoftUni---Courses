# Generated by Django 4.1.3 on 2022-11-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pumps', '0005_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('manual_url', models.URLField(verbose_name='Certificate URL')),
                ('pump', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pumps.pump')),
            ],
            options={
                'ordering': ('pump',),
            },
        ),
    ]
