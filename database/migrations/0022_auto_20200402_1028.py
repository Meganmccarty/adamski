# Generated by Django 3.0.4 on 2020-04-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20200402_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, help_text='Enter the year of travel.', max_length=4, null=True)),
                ('travel_details', models.TextField(blank=True, help_text='Enter the travel event details. If there are scientific names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will render the name in italics on the website.', max_length=10000, null=True)),
            ],
            options={
                'ordering': ['year', 'travel_details'],
            },
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.TextField(blank=True, help_text='Enter the author(s) who wrote this publication.', max_length=10000, null=True, verbose_name='Author(s)'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.TextField(blank=True, default='', help_text='Enter the rest of the publication (title, journal, pages, etc. If the reference has scientific names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will render the name in italics on the website.', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.IntegerField(blank=True, help_text='Enter the year of publication', null=True),
        ),
    ]
