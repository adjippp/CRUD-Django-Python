from django.db import models


# Create your models here.
class Book(models.Model):
    type_of_book = (
        ('One of Novel', 'One of Novel'),
        ('Documentation', 'Documentation'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    date_published = models.DateField(blank=True)
    pages = models.PositiveIntegerField(default=1)
    type_of_book = models.CharField(max_length=25, choices=type_of_book, default='Other')
    
    def __unicode__(self):
        return self.title