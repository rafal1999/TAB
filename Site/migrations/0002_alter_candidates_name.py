# Generated by Django 3.2 on 2021-05-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='Name',
            field=models.TextField(default=''),
        ),
    ]
