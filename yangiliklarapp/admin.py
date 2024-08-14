from django.contrib import admin

from .models import NewsModel, Category


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category)
