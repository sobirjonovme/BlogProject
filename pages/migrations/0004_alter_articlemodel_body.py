# Generated by Django 4.0.6 on 2022-07-12 11:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_articlemodel_qisqa_mazmun_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
