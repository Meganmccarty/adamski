from django.db import models

class Publication(models.Model):
    STATUS = (
        ('Published', 'Published'),
        ('Accepted', 'Accepted'),
        ('Submitted', 'Submitted'),
        ('In prep', 'In prep'),
    )
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True, 
                                help_text='Select the status of the publication.')
    pub_num = models.IntegerField(null=True, blank=True, verbose_name = 'Publication Number',
                                help_text='Enter the number of this publication, if it is published.')
    author = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Author(s)',
                                help_text='Enter the author(s) who wrote this publication.')
    year = models.IntegerField(null=True, blank=True, help_text='Enter the year the publication ' \
                                'was published.')
    letter = models.CharField(max_length=2, null=True, blank=True, help_text='Enter a letter ' \
                                'to follow the publication year, if this publication shares the ' \
                                'exact same authors and author order as another publication.')
    journal_title = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter ' \
                                'the title of the publication. If the title has scientific names, ' \
                                'put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" tags. This will ' \
                                'render the name in italics on the website.')
    journal = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter the ' \
                                'journal where the publication was published.')
    volume_num = models.IntegerField(null=True, blank=True, verbose_name='Volume Number', \
                                help_text='Enter the volume number, if the publication has one.')
    issue_num = models.IntegerField(null=True, blank=True, verbose_name='Issue ' \
                                'Number', help_text='Enter the issue number, if the publication has one.')
    pages = models.CharField(max_length=20, null=True, blank=True, help_text='Enter the pages ' \
                                'for the publication.')
    editor = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter the ' \
                                'name(s) of the editor(s), if this publication has editor(s).')
    chapter_title = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter ' \
                                'the chapter title of the publication. If the title has scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" ' \
                                'tags. This will render the name in italics on the website.')
    book_title = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter the ' \
                                'book title of the publication. If the title has scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and "&lt;/i&gt;" ' \
                                'tags. This will render the name in italics on the website.')
    edition = models.IntegerField(null=True, blank=True, help_text='Enter the edition of the publication.')
    volume = models.IntegerField(null=True, blank=True, help_text='Enter the volume number.')
    publisher = models.CharField(max_length=1000, null=True, blank=True, help_text='Enter the ' \
                                'name of the publisher, if the publication is a book.')
    publisher_country = models.CharField(max_length=100, null=True, blank=True, help_text='Enter ' \
                                'the country of the publisher.')
    book_pages = models.CharField(max_length=10, null=True, blank=True, help_text='Enter the ' \
                                'book\'s pages.')
    pdf = models.FileField(upload_to='publication-pdfs', null=True, blank=True)

    class Meta:
        ordering = ['pub_num', 'author', 'year']
    
    @property
    def get_year_and_letter(self):
        if self.letter:
            return f'{self.year}{self.letter}'
        else:
            return self.year

    def __str__(self):
        return f'{self.pub_num}: {self.author}. {self.get_year_and_letter}. {self.journal_title}'

class Presentation(models.Model):
    MONTH = (
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )
    day = models.CharField(max_length=5, null=True, blank=True, verbose_name='day(s)', \
                                help_text='Enter the day(s) the presentation was presented.')
    month = models.CharField(max_length=15, choices=MONTH, null=True, blank=True, \
                                help_text='Select the month the presentation was presented.')
    year = models.IntegerField(null=True, blank=True, help_text='Enter the year the ' \
                                'presentation was presented.')
    presenter = models.CharField(max_length=50, null=True, blank=True, help_text='Enter ' \
                                'the name of the presenter.')
    title = models.CharField(max_length=500, null=True, blank=True, help_text='Enter the ' \
                                'title of the presenation. If the title has scientific ' \
                                'names, put the scientific name between "&lt;i&gt;" and ' \
                                '"&lt;/i&gt;" tags. This will render the name in italics on ' \
                                'the website.')
    symposium = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the ' \
                                'symposium for this presentation, if it was presented in one.')
    meeting = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the ' \
                                'meeting at which the presentation was presented.')
    location = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the ' \
                                'location where the presentation was presented.')

    @property
    def get_day(self):
        if self.day:
            return self.day
        else:
            return ""
    @property
    def get_month(self):
        if self.month:
            return self.month
        else:
            return ""
    @property
    def get_year(self):
        if self.year:
            return self.year
        else:
            return ""

    def __str__(self):
        return f'{self.get_day} {self.get_month} {self.get_year}: {self.title}'

