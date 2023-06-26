from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'channel', 'article_created_date', 'get_creators')
    list_filter = ('channel', 'article_created_date', 'creators')
    filter_horizontal = ('creators',)
    date_hierarchy = 'article_created_date'  # Добавление иерархии даты
    list_display_links = ('article_title', 'channel')  # Установка ссылки для полей 'article_title' и 'channel'
    raw_id_fields = ('channel',)  # Замена выбора поля ForeignKey на поиск
    readonly_fields = ('article_title',)  # Установка поля 'article_created_date' как только для чтения
    search_fields = ('article_title', 'channel__channelName')  # Поля для поиска

    def get_creators(self, obj):
        return ", ".join([str(creator) for creator in obj.creators.all()])
    get_creators.short_description = 'Creators'

class ArticleInline(admin.TabularInline):
    model = Article.creators.through
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [ArticleInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
