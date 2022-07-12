from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


# Create your models here.
class ArticleModel(models.Model):
    sarlavha = models.CharField(max_length=50)
    qisqa_mazmun = models.CharField(max_length=200)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    muallif = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.sarlavha

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class CommentModel(models.Model):
    maqola = models.ForeignKey(
        ArticleModel,
        on_delete=models.CASCADE,
        related_name='izohlar'
    )
    izoh = models.CharField(max_length=400)
    muallif = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.izoh

    def get_absolute_url(self):
        return reverse('article_list')
