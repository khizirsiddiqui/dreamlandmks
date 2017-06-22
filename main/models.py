from django.db import models
from django.utils import timezone
from tinymce import HTMLField

from taggit.managers import TaggableManager

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=125, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('auth.User', null=True)
    body = HTMLField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    tags = TaggableManager()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.author.get_full_name())

    def get_title(self):
        return '{0} - {1}'.format(self.title, self.author.get_full_name())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @models.permalink
    def get_absolute_url(self):
        return ('single_article', (), {'slug': self.slug})
