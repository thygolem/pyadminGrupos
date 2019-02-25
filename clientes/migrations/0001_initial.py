# Generated by Django 2.1.5 on 2019-01-30 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.CharField(max_length=200)),
                ('nombre_contacto', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=20)),
                ('descripción', models.TextField(blank=True)),
                ('fecha_de_alta', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('grupo_1_id', models.CharField(max_length=200)),
                ('grupo_2_id', models.CharField(max_length=200)),
                ('grupo_3_id', models.CharField(max_length=200)),
                ('grupo_4_id', models.CharField(max_length=200)),
                ('grupo_5_id', models.CharField(max_length=200)),
                ('grupo_6_id', models.CharField(max_length=200)),
                ('grupo_7_id', models.CharField(max_length=200)),
                ('grupo_8_id', models.CharField(max_length=200)),
                ('grupo_9_id', models.CharField(max_length=200)),
                ('grupo_10_id', models.CharField(max_length=200)),
                ('grupo_11_id', models.CharField(max_length=200)),
                ('grupo_12_id', models.CharField(max_length=200)),
                ('grupo_13_id', models.CharField(max_length=200)),
                ('grupo_14_id', models.CharField(max_length=200)),
                ('grupo_15_id', models.CharField(max_length=200)),
                ('grupo_16_id', models.CharField(max_length=200)),
                ('grupo_17_id', models.CharField(max_length=200)),
                ('grupo_18_id', models.CharField(max_length=200)),
                ('grupo_19_id', models.CharField(max_length=200)),
                ('grupo_20_id', models.CharField(max_length=200)),
                ('grupo_21_id', models.CharField(max_length=200)),
            ],
        ),
    ]