from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserList)
admin.site.register(BookList)