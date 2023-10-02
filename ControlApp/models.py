from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200, blank=False)
    content = models.TextField(verbose_name="Содержание", blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title