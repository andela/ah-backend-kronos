# Generated by Django 2.1.7 on 2019-04-15 14:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190405_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, default=list, size=None),
        ),
    ]