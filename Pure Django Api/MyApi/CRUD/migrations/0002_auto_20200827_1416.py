# Generated by Django 3.1 on 2020-08-27 08:46

import CRUD.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=CRUD.models.upload_updated_image),
        ),
    ]
