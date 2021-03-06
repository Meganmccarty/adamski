# Generated by Django 3.0.4 on 2020-04-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20200402_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='day',
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='meeting',
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='month',
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='symposium',
        ),
        migrations.AlterField(
            model_name='presentation',
            name='location',
            field=models.CharField(blank=True, help_text='Enter the location where the presentation was presented, as well as any details regarding the meeting.', max_length=100, null=True),
        ),
    ]
