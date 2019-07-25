from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(blank=True)
    description = models.TextField(default='null')
    created_at = models.DateTimeField(auto_now=True)
    group_admin = models.ForeignKey(User, on_delete = models.CASCADE, related_name='group_admin', default = 0)
    members = models.ManyToManyField(User, related_name='members')


    def unique_slug(self):
        slug = slugify(self.name)
        return slug




    
        


# class Group_members(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     group = models.ForeignKey(Groups, on_delete=models.CASCADE)


