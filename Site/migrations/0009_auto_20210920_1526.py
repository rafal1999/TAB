# Generated by Django 3.2.4 on 2021-09-20 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0008_alter_calendar_meeting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment_meetings',
            name='ID_Recruitment_Process',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.recruitment_process', verbose_name='Recruitment process'),
        ),
        migrations.AlterField(
            model_name='recruitment_process',
            name='ID_Candidates',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.candidates', verbose_name='Candidate'),
        ),
    ]
