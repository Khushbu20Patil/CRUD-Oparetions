# Generated by Django 4.0.6 on 2022-08-15 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_poductmodel_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poductmodel',
            name='User',
        ),
    ]