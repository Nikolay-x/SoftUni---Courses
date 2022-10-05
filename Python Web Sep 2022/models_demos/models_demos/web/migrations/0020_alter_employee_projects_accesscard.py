# Generated by Django 4.1.1 on 2022-10-05 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_project_employee_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employees', to='web.project'),
        ),
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.employee')),
            ],
        ),
    ]
