from django.db import models
from django.utils import timezone
import uuid
from projects.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length = 200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def Meta():
        ordering = ['created']
    

class Review(models.Model):
    vote_type = [
        ('Up','Up_vote'),
        ('Down','Down_vote')
    ]
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=vote_type)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.value
    
   
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        



    


