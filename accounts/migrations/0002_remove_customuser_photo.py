# Generated by Django 4.0.6 on 2022-07-12 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='photo',
        ),
    ]