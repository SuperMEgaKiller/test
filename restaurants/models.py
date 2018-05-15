from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    time_add = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('..saving')
    print(instance.time_add)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def rl_post_save_receiver(sender, instance, *args, **kwargs):
    print('saved')
    print(instance.time_add)
    

pre_save.connect(rl_pre_save_receiver, sender=Restaurant)
post_save.connect(rl_post_save_receiver, sender=Restaurant)
