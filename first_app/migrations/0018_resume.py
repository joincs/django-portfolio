# Generated by Django 3.0.8 on 2020-08-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
            ],
        ),
    ]
