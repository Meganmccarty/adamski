# Generated by Django 3.0.4 on 2020-04-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_auto_20200401_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['year', 'letter', 'author']},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='book_pages',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='book_title',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='chapter_title',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='editor',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='issue_num',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='journal_title',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='pub_num',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='publisher_country',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='status',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='volume_num',
        ),
        migrations.AddField(
            model_name='publication',
            name='reference',
            field=models.TextField(blank=True, default='', help_text='Enter the rest of the publication (title, journal, pages, etc.', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='letter',
            field=models.CharField(blank=True, help_text='Enter a letter to follow the publication year, if there was more than 1 publication in a given year.', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='publication_pdfs'),
        ),
    ]
