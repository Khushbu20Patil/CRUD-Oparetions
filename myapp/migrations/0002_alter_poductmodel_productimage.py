# Generated by Django 4.0.6 on 2022-08-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poductmodel',
            name='ProductImage',
            field=models.ImageField(max_length=254, upload_to='photos'),
        ),
    ]
