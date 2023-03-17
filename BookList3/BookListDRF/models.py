from django.db import models

# Create your models here.


# class Category(models.Model):
#     slug=models.SlugField()
#     type = models.CharField(max_length=255)
#     language = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.language}--{self.type}"


class Book(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title}-{self.author}"
