# Generated by Django 3.0.8 on 2020-07-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_auto_20200730_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(),
        ),
    ]
