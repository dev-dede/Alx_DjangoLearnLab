from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    Each author has a name, and an author can be linked to only one book (OneToOne relationship).
    """
     
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.OneToOneField(Author, on_delete=models.SET_NULL, null=True, related_name="book")

    def __str__(self):
        return self.title