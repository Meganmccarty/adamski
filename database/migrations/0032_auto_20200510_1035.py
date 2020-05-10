# Generated by Django 3.0.4 on 2020-05-10 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_auto_20200510_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pub_num',
            field=models.IntegerField(blank=True, help_text="Enter the publication's number.", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)], verbose_name='Publication Number'),
        ),
    ]