# Generated by Django 3.2 on 2021-05-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_auto_20210516_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='Application_date',
            field=models.DateField(auto_now=True),
        ),
    ]
