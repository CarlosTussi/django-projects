from django.db import models

# Create your models here.
class Book(models.Model):
    ISBN = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.IntegerField()


    def __str__(self):
        return "\nISBN: {}\nName: {}\nAuthor: {}\nYear: {}\n".format(self.ISBN, self.name, self.author, self.year)