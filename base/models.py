from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #null=True allows for the database to have a blank instance
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #Timestamps everytime
    created = models.DateTimeField(auto_now_add=True) #Only timestamps when the instance is created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #Timestamps everytime
    created = models.DateTimeField(auto_now_add=True) #Only timestamps when the instance is created
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.body[0:50]

class Comments(models.Model):
    post = models.ForeignKey(Room, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s  - %s' % (self.post.title, self.name)