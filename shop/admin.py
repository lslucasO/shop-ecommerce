from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Book, BookAdmin)
admin.site.register(BookCover)