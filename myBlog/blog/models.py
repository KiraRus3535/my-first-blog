from django.conf import settings
from django.db import models
from django.utils import timezone
 
# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
 
    def __unicode__(self):
        return self.title
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-timestamp"]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.CharField('имя автора', max_length = 50) 
    comment_text = models.CharField('текст комментария', max_length = 200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'