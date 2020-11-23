from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Photo(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user');
    text=models.TextField(blank=True) # instagram text
    image=models.ImageField(upload_to='timeline_photo/%Y/%m/%d') # make timeline_photo, photo will save year, month, day
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name = 'like_post', blank=True)
    favorite=models.ManyToManyField(User, related_name = 'favorite_post', blank=True)

    def __str__(self):
        return "text : "+self.text
    
    class Meta:
        ordering=['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])