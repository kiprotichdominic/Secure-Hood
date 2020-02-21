from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class NeigbourHood(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique = True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]
        
class NeigbourHoodMember(models.Model):
    neigbourhood = models.ForeignKey(NeigbourHood,related_name='membership')
    user = models.ForeignKey(User,related_name='user_neigbourhood')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ("neigbourhood","user")