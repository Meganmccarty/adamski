# Generated by Django 3.0.4 on 2020-04-02 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_auto_20200402_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentation',
            options={'ordering': ['year', 'title']},
        ),
    ]
