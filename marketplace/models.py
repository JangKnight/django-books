from django.db import models
from django.db.models import Q
from django.core import validators
from django.utils.text import slugify
# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}\n{self.city}, {self.state}\n{self.zip}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self}")
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestseller = models.BooleanField(null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.rating} rating)"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)