# Generated by Django 3.0.8 on 2020-07-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20200718_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
    ]