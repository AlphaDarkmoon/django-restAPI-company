# Generated by Django 4.2.5 on 2023-09-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Project Leader', 'Project Leader')], max_length=50),
        ),
    ]
