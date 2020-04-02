# Generated by Django 3.0.4 on 2020-04-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20200401_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='month',
            field=models.CharField(blank=True, choices=[('January', '01'), ('February', '02'), ('March', '03'), ('April', '04'), ('May', '05'), ('June', '06'), ('July', '07'), ('August', '08'), ('September', '09'), ('October', '10'), ('November', '11'), ('December', '12')], help_text='Select the month the presentation was presented.', max_length=15, null=True),
        ),
    ]
