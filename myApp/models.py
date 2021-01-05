from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re

class Post(models.Model):
    main_text = models.CharField(max_length=200)
    create_user = models.ForeignKey(User, on_delete = models.CASCADE)
    create_date = models.DateTimeField('date published', default=timezone.now)
    create_img = models.ImageField(blank=True, upload_to="post/%Y/%m/%d", null=True)

    def __str__(self):
        return self.main_text


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_text = models.CharField(max_length=200)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    comment_date = models.DateTimeField('date published', default=timezone.now)
    comment_update_date = models.DateTimeField('date published', null = True, default=timezone.now)
    
    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return '%s - %s' % (self.comment_user, self.comment_text) 