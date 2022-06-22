from django.contrib import admin
from .models import Post,Comment # todo import modelů

admin.site.register(Post)
admin.site.register(Comment)