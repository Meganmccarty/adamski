# Generated by Django 3.0.4 on 2020-04-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_auto_20200402_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society', models.TextField(blank=True, help_text='Enter the name of the society, as well as any postions held.', max_length=500, null=True)),
            ],
        ),
    ]
