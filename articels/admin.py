from django.contrib import admin
from .models import Articels
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","article_title"]
    search_fields = ["article_title","article_content"]
admin.site.register(Articels,ArticleAdmin)
