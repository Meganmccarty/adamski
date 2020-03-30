# Generated by Django 3.0.4 on 2020-03-21 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200320_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='issue_num',
            field=models.IntegerField(blank=True, help_text='Enter the issue number, if the publication has one.', null=True, verbose_name='Issue Number'),
        ),
    ]
