from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Publication(models.Model):
    author = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Author(s)',
                                help_text='Enter the author(s) who wrote this publication.')
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), \
                                MaxValueValidator(2100)], help_text='Enter the year of publication')
    letter = models.CharField(max_length=2, null=True, blank=True, help_text='Enter a letter ' \
                                'to follow the publication year, if there was more than 1 ' \
                                'publication in a given year.')
    reference = models.TextField(max_length=10000, default='', null=True, blank=True, \
                                help_text='Enter the rest of the publication (title, journal, ' \
                                'pages, etc. If the reference has scientific names, put the ' \
                                'scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. ' \
                                'This will render the name in italics on the website.')
    pdf = models.FileField(upload_to='publication_pdfs', null=True, blank=True)

    class Meta:
        ordering = ['year', 'letter', 'author']
    
    @property
    def year_and_letter(self):
        if self.letter:
            return f'{self.year}{self.letter}'
        else:
            return self.year

    def __str__(self):
        return f'{self.author}. {self.year_and_letter}'

class Presentation(models.Model):
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), \
                                MaxValueValidator(2100)], help_text='Enter the year the ' \
                                'presentation was presented.')
    title = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter the ' \
                                'title of the presenation. If the title has scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and ' \
                                '"&lt;/i&gt;" tags. This will render the name in italics on ' \
                                'the website.')
    location = models.TextField(max_length=10000, null=True, blank=True, help_text='Enter the ' \
                                'location where the presentation was presented, as well as ' \
                                'any details regarding the meeting.')
    presenter = models.CharField(max_length=50, null=True, blank=True, help_text='Enter ' \
                                'the name of the presenter if it was someone other than ' \
                                'yourself.')
    
    class Meta:
        ordering = ['year', 'title']

    def __str__(self):
        return f'{self.year}: {self.title}'

class Travel(models.Model):
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), \
                                MaxValueValidator(2100)], help_text='Enter the '\
                                'year of travel.')
    travel_details = models.TextField(max_length=10000, null=True, blank=True, help_text= \
                                'Enter the travel event details. If there are scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and ' \
                                '"&lt;/i&gt;" tags. This will render the name in italics on ' \
                                'the website.')
    
    class Meta:
        ordering = ['year', 'travel_details']
    
    def __str__(self):
        return f'{self.year}: {self.travel_details}'

class Grant(models.Model):
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), \
                                MaxValueValidator(2100)], help_text='Enter the '\
                                'year of the fellowship or grant.')
    amount = models.IntegerField(null=True, blank=True, help_text='Enter the amount ' \
                                'of the fellowship or grant.')
    grant_details = models.TextField(max_length=10000, null=True, blank=True, verbose_name= \
                                'Fellowship or grant details', help_text='Enter the details ' \
                                'of the fellowship or grant. If there are scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and ' \
                                '"&lt;/i&gt;" tags. This will render the name in italics on ' \
                                'the website.')
    class Meta:
        ordering = ['year', 'amount', 'grant_details']
    
    def __str__(self):
        return f'{self.year}: {self.grant_details}. {self.amount}'

