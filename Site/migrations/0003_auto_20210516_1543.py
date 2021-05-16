# Generated by Django 3.2 on 2021-05-16 15:43

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_alter_candidates_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='Application_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 5, 16, 15, 43, 46, 6662, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidates',
            name='Birthdate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
