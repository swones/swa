from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField('Name', max_length=50, unique=True,
                            null=False, blank=False)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Name', max_length=15, unique=True,
                            null=False, blank=False)

    def __unicode__(self):
        return self.name


class Snippet(models.Model):
    name = models.CharField('Name', max_length=100, unique=True,
                            null=False, blank=False)
    created_by = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    public = models.BooleanField('Public', default=False)
    code = models.TextField('Code', blank=False, null=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    modified_at = models.DateTimeField('Last edit at', auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name + " - " + self.created_by.email
