# Generated by Django 5.1.3 on 2024-11-26 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alter_alumnos_nota1_alter_alumnos_nota2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='carrera',
        ),
    ]
