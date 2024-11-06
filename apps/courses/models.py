from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Course(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses_created')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User,related_name='courses_joined',blank=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course,related_name='modules',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    order = OrderField(blank=True,for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'
    

class Content(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name='contents')
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,limit_choices_to={'model_in':('text','video','image','file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')
    order = OrderField(blank=True,for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_related')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    
    def render(self):
        return render_to_string(f'courses/content/{self._meta.model_name}.html',{'itme':self})
    

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    image = models.ImageField(upload_to='images')

class Video(ItemBase):
    video = models.URLField()
