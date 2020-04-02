# Generated by Django 3.0.4 on 2020-04-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20200329_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='month',
            field=models.CharField(blank=True, choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], help_text='Select the month the presentation was presented.', max_length=15, null=True),
        ),
    ]
