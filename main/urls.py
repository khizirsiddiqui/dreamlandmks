from django.conf.urls import url

from . import views

from discussions.views import discussions, single_discuss

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'logout/$', views.user_logout, name='user_logout'),

    url(r'about_me/$', views.about_me, name='about_me'),

    url(r'articles/$', views.articles, name='articles'),
    url(r'articles/(?P<slug>[\w-]+)/$',
        views.single_article, name='single_article'),

    url(r'tags/$', views.tag_list, name='tag_list'),
    url(r'tags/(?P<tag>[\w-]+)/$',
        views.article_by_tag, name='article_by_tag'),

    url(r'tutorials/$', views.tutorials, name='tutorials'),

    url(r'discussions/$', discussions, name='discussions'),
    url(r'discussions/(?P<slug>[\w-]+)/$',
        single_discuss, name='single_discuss'),
]
