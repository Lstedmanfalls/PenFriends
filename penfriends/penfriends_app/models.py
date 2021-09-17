from django.db import models
from django.db.models.deletion import CASCADE
from login_registration_app.models import User
# Create your models here.
#associating FK with each category of user
#User class: 
#a list of residents when User.category="Admin"
#if User.category=="Admin"
    #Resident.objects.create(
        #all fields except penfriends
    #)
#a list of residents when User.category="Penpal"
#a list of messages when User.category="Penpal"
#a list of posts when User.category="Admin"

class Resident(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    picture = models.ImageField()
    bio = models.TextField()
    creator = models.ForeignKey(User, related_name="residents", on_delete = models.CASCADE)
    penfriends = models.ManyToManyField(User, related_name="penpal_residents")
    #a list of penpals this resident has
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # a list of res_messages
    
class Message(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    attachment = models.FileField(upload_to='media')
    creator = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    recipient = models.ForeignKey(Resident, related_name="res_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    maker = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)