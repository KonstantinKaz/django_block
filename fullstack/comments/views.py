from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
from articles.models import Article
from django.contrib.auth.decorators import login_required


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', article_id=article_id)

    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments, 'form': form})


@login_required
def create_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()

    return render(request, 'comments/create_comment.html', {'form': form})



def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.article.id

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.article.id

    if request.method == 'POST':
        comment.delete()
        return redirect('article_detail', article_id=article_id)

    return redirect('article_detail', article_id=article_id)
