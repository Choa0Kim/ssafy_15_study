from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # 책 제목
    author = models.CharField(max_length=50)  # 저자

    def __str__(self):
        return self.title