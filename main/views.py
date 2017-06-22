from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .scripts import get_random_word, get_news, get_random_quote

from .models import Article
from discussions.models import Discussion

from taggit.models import Tag
from social_django.models import UserSocialAuth

# Create your views here.


def index(request):
    word = get_random_word()
    quote, q_author = get_random_quote()
    article_list = Article.objects.all().order_by('-created_date')
    discussion_list = Discussion.objects.all().order_by('-created_date')
    newspaper = None
    # newspaper = get_news()
    return render(request, 'index.html',
                  {'word': word,
                   'quote': quote,
                   'q_author': q_author,
                   'article_list': article_list,
                   'newspaper': newspaper,
                   'discuss_list': discussion_list,}
                  )


def articles(request):
    articles = Article.objects.all().order_by('-created_date')

    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 4)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    return render(request, 'articles.html', {'article_list': article_list})


def single_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'single_article.html',
                  {'article': article}
                  )


def article_by_tag(request, tag):
    articles = Article.objects.filter(tags__slug=tag).distinct()

    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 4)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    return render(request, 'articles.html',
                  {'article_list': article_list, 'tag': tag}
                  )


def tag_list(request):
    tag_list = Tag.objects.all().order_by('name')

    return render(request, 'tags.html',
                  {'tag_list': tag_list}
                  )


def tutorials(request):
    return render(request, 'tutorials.html', {})


def about_me(request):
    return render(request, 'about_me.html', {})


@login_required
def user_logout(request):
    logout(request)
    messages.add_message(
        request, messages.SUCCESS, 'Successfuly Signed out')
    return redirect('index')
