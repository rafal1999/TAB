# Generated by Django 3.2 on 2021-05-26 15:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates_Role',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default=None, max_length=25)),
            ],
            options={
                'verbose_name': 'Candidate role',
                'verbose_name_plural': 'Candidates roles',
            },
        ),
        migrations.CreateModel(
            name='Recruitment_Meetings',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Hard_skills', models.TextField(default='', null=True)),
                ('Soft_skills', models.TextField(default='', null=True)),
                ('Grade', models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('Notes', models.TextField(default='', null=True)),
            ],
            options={
                'verbose_name': 'meeting',
                'verbose_name_plural': 'Recruitment meetings',
            },
        ),
        migrations.CreateModel(
            name='Workers_Role',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40, null=True, unique=True, verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Workers roles',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=25, null=True)),
                ('Surname', models.CharField(default='', max_length=25, null=True)),
                ('Birthdate', models.DateField(null=True)),
                ('Login', models.CharField(max_length=32, null=True)),
                ('Password', models.CharField(default='', max_length=32)),
                ('Email_address', models.EmailField(max_length=50, null=True)),
                ('ID_Workers_Role', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.workers_role')),
            ],
            options={
                'verbose_name': 'worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Points', models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('ID_Candidates_Role', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Site.candidates_role', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default=None, max_length=25)),
                ('Surname', models.CharField(default=None, max_length=25)),
                ('Birthdate', models.DateField()),
                ('Application_date', models.DateField(auto_now_add=True)),
                ('Phone_number', models.CharField(max_length=13, null=True)),
                ('Sex', models.CharField(choices=[('U', 'Unsure'), ('F', 'Female'), ('M', 'Male')], default=None, max_length=1, null=True)),
                ('Email_address', models.EmailField(max_length=50, null=True)),
                ('CV', models.TextField(default='')),
                ('Motivation_letter', models.TextField(default='')),
                ('Stage', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='', max_length=1)),
                ('Hired', models.CharField(choices=[('P', 'In process'), ('Y', 'Yes'), ('N', 'No')], default='', max_length=10)),
                ('ID_Candidates_Role', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.candidates_role')),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Meeting_date', models.DateField()),
                ('Description', models.TextField(default='', null=True)),
                ('Worker_present', models.CharField(choices=[('U', 'Unknown'), ('Y', 'Yes'), ('N', 'No')], default='U', max_length=1, verbose_name='Worker present')),
                ('Candidate_present', models.CharField(choices=[('U', 'Unknown'), ('Y', 'Yes'), ('N', 'No')], default='U', max_length=1, verbose_name='Candidate present')),
                ('Candidates_ID_Candidate', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.candidates', verbose_name='Candidate')),
                ('Recruitment_Meetings_ID', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.recruitment_meetings', verbose_name='Recruitment meeting')),
                ('Tests_ID', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.tests', verbose_name='Test')),
                ('Workers_ID_Worker', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.workers', verbose_name='Worker')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'Calendar',
            },
        ),
    ]
