from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from comments.forms import CommentForm
from comments.models import Comment
from django.contrib.auth.decorators import login_required
from channels.models import Channel

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()

    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments, 'form': form})



def article_list(request, id_channel):
    articles = Article.objects.filter(channel_id=id_channel)
    return render(request, 'articles/article_list.html', {'articles': articles})


@login_required
def create_article(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    form = None  # Определение переменной form

    if channel.owner != request.user:
        return render(request, 'articles/access_denied.html')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.channel = channel
            article.creator = request.user
            article.save()
            return redirect('channel_detail', channel_id=channel.id)


    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})


@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user != request.user:  # Проверяем, является ли текущий пользователь владельцем статьи
        return redirect('article_list')
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_list')



