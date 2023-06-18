from django.shortcuts import render, redirect
from .models import Favorite
from articles.models import Article

def add_to_favorites(request, article_id):
    article = Article.objects.get(id=article_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, article=article)

    if created:
        # Статья успешно добавлена в избранное
        # Вы можете добавить дополнительную логику или уведомление пользователю здесь
        pass
    else:
        # Статья уже добавлена в избранное пользователем
        # Вы можете добавить дополнительную логику или уведомление пользователю здесь
        pass

    return redirect('article_detail', article_id=article_id)



def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/favorites_list.html', {'favorites': favorites})
