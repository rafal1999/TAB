# Generated by Django 3.2 on 2021-05-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_auto_20210516_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='Email_address',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='Name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='Stage',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='Surname',
            field=models.TextField(default='', null=True),
        ),
    ]
