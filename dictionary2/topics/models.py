# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.urlresolvers import reverse
from dictionary2.users.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_slug


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    # "#{title}.format(title=self.title)"

    """
    class Meta:
        verbose_name=_("abc")
        verbose_name_plural = _("xyz")
        ordering = ("created_at")

    """


class Topic(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User")
    )

    title = models.CharField(
        max_length=140,
        unique=True,
        verbose_name=_("Title")
    )

    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created_at")
    )

    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=_("Category")
    )

    def __unicode__(self):
        return self.slug


class Entry(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User")
    )

    title = models.ForeignKey(
        Topic,
        verbose_name=_("Topic")
    )

    content = models.TextField(
        verbose_name=_("Content")
    )

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created_at")
    )

class Favorite(models.Model):
    entry = models.ForeignKey(
        Entry
    )

    user = models.ForeignKey(
        User,
    )

    class meta:
        unique_together = (('entry', 'user'),)