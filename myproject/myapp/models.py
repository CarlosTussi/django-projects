from django.db import models

# Create your models here.
class Book(models.Model):
    ISBN = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.IntegerField()
    price = models.FloatField()


    def __str__(self):
        return "\nISBN: {}\nName: {}\nAuthor: {}\nYear: {}\n".format(self.ISBN, self.name, self.author, self.year)


class MenuCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.FloatField(null=False)
    category_id = models.ForeignKey(MenuCategory, default= None, on_delete=models.PROTECT, related_name="somethingelse")


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()