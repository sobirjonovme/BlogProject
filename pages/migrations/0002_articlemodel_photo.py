# Generated by Django 4.0.6 on 2022-07-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]