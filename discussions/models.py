from django.db import models
from django.utils import timezone
from tinymce import HTMLField

from taggit.managers import TaggableManager
# Create your models here.


class Discussion(models.Model):
    title = models.CharField(max_length=125, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    creater = models.ForeignKey('auth.User', null=True)
    body = HTMLField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    voters = models.ManyToManyField(
        'auth.User', related_name='voters', blank=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = "Discussion"
        verbose_name_plural = "Discussions"

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.creater.get_full_name())

    def get_title(self):
        return self.title

    def get_comments(self):
        return Comment.objects.filter(discussion=self)

    @models.permalink
    def get_absolute_url(self):
        return ('single_discuss', (), {'slug': self.slug})


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion)
    commenter = models.ForeignKey('auth.User', blank=True, null=True)
    body = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    voters = models.ManyToManyField('auth.User', related_name='com_voters')

    def __str__(self):
        return '{0} - {1}'.format(self.commenter, self.discussion.get_title())

    def get_subcomments(self):
        return SubComment.objects.filter(comment=self)


class SubComment(models.Model):
    discussion = models.ForeignKey(Discussion, null=True)
    comment = models.ForeignKey(Comment, null=True)
    commenter = models.ForeignKey('auth.User', null=True)
    body = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    voters = models.ManyToManyField('auth.User', related_name='sub_com_voters')

    def __str__(self):
        return '{0} - {1}'.format(self.commenter, self.comment)
