# Generated by Django 3.0.5 on 2021-09-23 14:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('type_of_image', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
