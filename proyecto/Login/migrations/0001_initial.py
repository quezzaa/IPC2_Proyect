# Generated by Django 4.2.6 on 2023-11-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('idDoctor', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('colegiado', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=128)),
                ('role', models.CharField(default='2', max_length=1)),
            ],
            options={
                'db_table': 'tbdoctor',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('contraseña', models.CharField(max_length=128)),
                ('role', models.CharField(default='3', max_length=1)),
            ],
            options={
                'db_table': 'tbpacientes',
            },
        ),
    ]
