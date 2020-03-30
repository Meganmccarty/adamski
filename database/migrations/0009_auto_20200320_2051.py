# Generated by Django 3.0.4 on 2020-03-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20200320_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='book_title',
            field=models.CharField(blank=True, help_text='Enter the book title of the publication. If the title has scientific names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will render the name in italics on the website.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='chapter_title',
            field=models.CharField(blank=True, help_text='Enter the chapter title of the publication. If the title has scientific names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will render the name in italics on the website.', max_length=1000, null=True),
        ),
    ]
