# Generated by Django 3.0.8 on 2020-07-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20200730_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampleattachment',
            name='file_upload',
        ),
        migrations.RemoveField(
            model_name='sampleattachment',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='file_upload',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
