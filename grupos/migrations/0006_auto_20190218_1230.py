# Generated by Django 2.1.5 on 2019-02-18 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20190218_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupo',
            old_name='potencia_kva',
            new_name='kva',
        ),
    ]