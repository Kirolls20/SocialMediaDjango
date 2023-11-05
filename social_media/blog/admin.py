from django.contrib import admin

from .models import Blog,Comment,Bookmark
# Register your models here.
# admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Bookmark)