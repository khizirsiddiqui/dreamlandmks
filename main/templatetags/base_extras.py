from django import template
from django.core.urlresolvers import reverse
from django.templatetags.static import static

from main.scripts import smallify, downloadFile

import urllib.request
import os
from django.conf import settings

register = template.Library()

# os.path.isfile(path)


@register.simple_tag
def navactive(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""


@register.simple_tag
def get_user_profile_url(user):
    if user.is_authenticated():
        facebook_data = user.social_auth.filter(provider='facebook').first()
        if facebook_data:
            fb_id = facebook_data.uid
            access_token = facebook_data.extra_data['access_token']
            return 'http://graph.facebook.com/' + str(fb_id) + '/picture?access_token=' + str(access_token)
    return '/static/img/default.png'


@register.filter
def summarize(data):
    return smallify(data)


@register.simple_tag
def get_user_image_url(user):
    if user.is_authenticated():
        username = user.username
        path = os.path.join(settings.STATICFILES_DIRS[0], "img", username)+'.jpg'
        if os.path.isfile(path):
            return '/static/img/{}.jpg'.format(username)
        else:
            facebook_data = user.social_auth.filter(
                provider='facebook').first()
            if facebook_data:
                fb_id = facebook_data.uid
                if downloadFile(fb_id, path):
                    if os.path.isfile(path):
                        return '/static/img/' + str(username) + '.jpg'
                else:
                    print("You programmed WRONG")
    return '/static/img/default.png'
