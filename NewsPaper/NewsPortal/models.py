from django.db import models
from django.contrib.auth.models import User
from .config import CHOICE, news
from django.db.models.functions import Coalesce
from django.db.models import Sum

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_a = models.IntegerField(default=0, db_column='rating_author')

    def update_rating(self):
        rat1_post = Post.objects.filter(author=self.pk).aggregate(sum_1=Coalesce(Sum('rating_p') * 3, 0))['sum_1']
        rat2_comment = Comment.objects.filter(user_id=self.author).aggregate(sum_2=Coalesce(Sum('rating_c'), 0))['sum_2']
        rat3_comment = Comment.objects.filter(post__author__author=self.author).aggregate(sum_3=Coalesce(Sum('rating_c'), 0))['sum_3']

        self.rating_a = rat1_post + rat2_comment + rat3_comment
       # print(self.rating_a)
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=CHOICE, default=news, db_column='Type_post')
    dtime_p = models.DateTimeField(auto_now_add=True, db_column='datetime_post')
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text_p = models.TextField(db_column='text_post')
    rating_p = models.IntegerField(default=0, db_column='rating_post')

    def like(self):
        self.rating_p += 1
        self.save()

    def dislike(self):
        self.rating_p -= 1
        self.save()

    def preview(self):
        t = str(self.text_p)
        if len(t) > 124:
            return t[:124] + '...'
        else:
            return t


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    text_c = models.TextField(db_column='text_comment')
    dtime_c = models.DateTimeField(auto_now_add=True, db_column='datetime_comment')
    rating_c = models.IntegerField(default=0, db_column='rating_comment')

    def like(self):
        self.rating_c += 1
        self.save()

    def dislike(self):
        self.rating_c -= 1
        self.save()
