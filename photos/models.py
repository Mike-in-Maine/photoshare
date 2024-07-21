from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse



class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    #utility variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.DateTiemField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.SlugField(null=True, blank=True)
    last_updated = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug':self.slug})
class Photo(models.Model):
    file = models.FileField(upload_to="files")

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption