from bs4 import BeautifulSoup
from random import randint
import requests
import urllib.request
from urllib.error import HTTPError, URLError

url_i = 'main/list.html'


def makeSoup(url):
    soup = BeautifulSoup(open(url, encoding="utf8"), "html.parser")
    return soup


def get_random_word():
    soup = makeSoup(url_i)
    word_list = soup.find_all(class_='entry learnable')
    word = word_list[randint(0, len(word_list) - 1)]
    word_txt = word.find(class_='word dynamictext').text
    word_define = word.find(class_='definition').text
    word_example = word.find(class_='example').text.replace(
        '\n', '').replace('.', '.\n-')
    word_a = {'txt': word_txt, 'define': word_define, 'example': word_example}
    return word_a

url_news = 'https://feeds.feedburner.com/ndtvnews-top-stories?format=xml'


def get_news():
    page = requests.get(url_news)
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.find_all('item')
    headline = {}
    headlines = []
    for item in items:
        headline = {}
        if item.title:
            headline['title'] = item.title.text
        if item.link:
            headline['link'] = item.link.text
        if item.updatedAt:
            headline['update'] = item.updatedAt.text
        if item.StoryImage:
            headline['image'] = item.StoryImage.text
        if item.description:
            headline['desc'] = item.description.text
        headlines.append(headline)
    return headlines


def get_random_quote():
    file = open('main/quote_list.txt')
    quote_list = file.readlines().encode('utf-8')
    total = len(quote_list) - 1
    quote_text = quote_list[randint(0, total)]
    return quote_text.split(' -')


def smallify(data):
    soup = BeautifulSoup(data, "html.parser")
    return soup.text


def downloadFile(fb_id, path):
    url = 'http://graph.facebook.com/' + str(fb_id) + '/picture?type=square'
    try:
        f = urllib.request.urlopen(url)
        print("Downloading Profile Photo for ", url)
        local_file = open(path, "wb")
        local_file.write(f.read())
        local_file.close()
        return True
    except HTTPError as e:
        print("HTTP Error:", e.code, url)
    except URLError as e:
        print("URL Error:", e.reason, url)
    return False
