# -*- coding: utf-8 -*-
from django.contrib import admin
from test1.models import Book,Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)