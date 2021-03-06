# Generated by Django 3.0.4 on 2020-03-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20200320_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=5, null=True, verbose_name='day(s)')),
                ('month', models.CharField(blank=True, max_length=15, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('presenter', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('symposium', models.CharField(blank=True, max_length=100, null=True)),
                ('meeting', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
