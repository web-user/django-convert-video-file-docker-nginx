# Generated by Django 2.2.9 on 2020-01-08 13:33

import convertfile.utils
from django.db import migrations, models
import uploading.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(default='', upload_to=uploading.models.upload_media_file, validators=[convertfile.utils.validate_file_extension]),
        ),
    ]
