from django.contrib import admin
from .models import Book, Author, Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "state", "zip")


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "rating")
    list_filter = ("title", "author", "rating")

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)