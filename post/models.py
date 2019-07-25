from django.db import models
from django.contrib.auth.models import User
from groups.models import Groups
from django.template.defaultfilters import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    group = models.ForeignKey(Groups, on_delete = models.CASCADE)
    slug = models.CharField(max_length =255, blank = True)
    created_at = models.DateTimeField(auto_now=True)


    def unique_slug(self):
        slug = slugify(self.title)
        return slug
