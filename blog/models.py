from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    count_post = models.IntegerField(null=True)
    image = models.ImageField(upload_to="", null=True, blank=True)

    def __str__(self):
        return self.title
