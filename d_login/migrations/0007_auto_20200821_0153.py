# Generated by Django 3.1 on 2020-08-20 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_login', '0006_auto_20200821_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
