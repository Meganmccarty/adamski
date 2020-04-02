# Generated by Django 3.0.4 on 2020-04-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20200401_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], help_text='Select the month the presentation was presented.', max_length=15, null=True),
        ),
    ]