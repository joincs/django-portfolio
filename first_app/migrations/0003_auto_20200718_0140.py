# Generated by Django 3.0.8 on 2020-07-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20200718_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='project_file/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]
