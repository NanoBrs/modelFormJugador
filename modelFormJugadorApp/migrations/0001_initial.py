# Generated by Django 3.2 on 2024-10-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('posicion', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('equipo', models.CharField(max_length=50)),
            ],
        ),
    ]