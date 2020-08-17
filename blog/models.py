from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class Account(models.Model):
#    username = models.CharField(label='Enter Username', max_length=15)
#    password = models.CharField(label='Enter Password', max_length=30)
#    password_confirm = models.CharField(label='Confirm Password', max_length=30)
#    email = models.EmailField(label='Enter Email', max_length=30)

#    def __str__(self):
#        return self.username

#class Profile(models.Model):
#    users = models.OneToOneField(User)
#    biography = CharField(max_length)
