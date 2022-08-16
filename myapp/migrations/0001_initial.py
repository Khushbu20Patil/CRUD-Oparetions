# Generated by Django 4.0.6 on 2022-08-11 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductDescription', models.CharField(max_length=200)),
                ('ProductImage', models.ImageField(upload_to='')),
                ('ProductPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usermodel')),
            ],
        ),
    ]