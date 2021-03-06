# Generated by Django 3.0.4 on 2020-04-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0025_grant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='grant_details',
            field=models.TextField(blank=True, help_text='Enter the details of the fellowship or grant. If there are scientific names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will render the name in italics on the website.', max_length=10000, null=True, verbose_name='Fellowship or grant details'),
        ),
    ]
