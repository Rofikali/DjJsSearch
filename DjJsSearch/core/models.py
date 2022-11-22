from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title
