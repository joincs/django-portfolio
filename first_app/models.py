from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from django.db import models

# Create your models here.

class Categorie(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class project(models.Model):
    name         = models.CharField(max_length=120)
    slug         = models.SlugField(blank=True)
    category     = models.ForeignKey(Categorie,on_delete=models.SET_NULL,blank=True,null=True,)
    file_upload  = models.FileField(upload_to='documents/', null=True,blank=True)
    image        = models.ImageField(upload_to='projects/')
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_date  = models.DateTimeField(auto_now_add=False,auto_now=True)
    description  = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self,slug):
        return reverse('first_app:project_detail', kwargs={slug:self.slug})
    
    class Meta:
        ordering = ['-created_date','-update_date']

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(slug_generator, sender=project)

class About(models.Model):
    short_desc   = models.CharField(max_length=220)
    image        = models.ImageField(upload_to='about/')
    description  = models.TextField()

    def __str__(self):
        return self.short_desc

class Contact(models.Model):
    name        = models.CharField(max_length=120)
    email       = models.EmailField()
    subject     = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.name + "  " + self.email


class SampleAttachment(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email


class Resume(models.Model):
    resume = models.FileField(upload_to='resume/', null=True,blank=True)

    def __str__(self):
        return str(self.resume)


    

    
