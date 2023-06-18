from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_date')
    list_filter = ('user', 'created_date')
    search_fields = ('user__username', 'article__article_title')
