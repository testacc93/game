from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog
# Register your models here.
class BlogAdmin(UserAdmin):
    model = Blog
    fields = '__all__'

admin.site.register(Blog)