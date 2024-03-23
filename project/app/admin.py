from django.contrib import admin

from .models import Author, Social

# Register your models here.
admin.site.register(Author)
admin.site.register(Social)