from django.db import models
from django.urls import reverse

# Create your models here.
class Singer(models.Model):
    nickname = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='hiphop')
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    about = models.TextField(blank=True, default='')
    
    class Meta:
        indexes = [models.Index(fields=['slug',])]
    
    def __str__(self):
        return self.nickname
    
    @property
    def fullname(self):
        return f"{self.name} {self.surname}"
    
    def get_absolute_url(self):
        return reverse("hiphop:singer", kwargs={"slug": self.slug})
    
    