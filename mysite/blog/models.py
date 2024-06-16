from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)       # Заголовок поста
    slug = models.SlugField(max_length=250,unique_for_date='publish')   # служебное, техническое поле
    author = models.ForeignKey(User,on_delete=models.CASCADE,           # Автор поста, внешний ключ
                               related_name='blog_posts')
    body = models.TextField()                                        # Содержание поста
    publish = models.DateTimeField(default=timezone.now)             # дата публикации
    created = models.DateField(auto_now_add=True)                    # дата создания
    updated = models.DateField(auto_now=True)                        # дата изменения
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')    # статус поста

    class Meta:                               # сортировка в порядке убывания даты публикации
        ordering = ('-publish',)
    def __str__(self):                           # возвращает отображение понятное для человека
        return self.title

