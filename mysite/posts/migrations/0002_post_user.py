# Generated by Django 4.1.5 on 2023-01-02 17:30

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.TextField(default=django.utils.timezone.now, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
    ]
