from django.db import models

# Added all
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    # parent = models.ForeignKey("Category", on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    description = models.TextField(null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    net_worth = models.BigIntegerField(default=0)
    positive_reviews = models.PositiveIntegerField(default=0)
    negative_reviews = models.PositiveIntegerField(default=0)
    books_published = models.PositiveIntegerField(default=0)
    years_experience = models.SmallIntegerField(default=0)
    rating = models.FloatField(default=0)
    average_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name