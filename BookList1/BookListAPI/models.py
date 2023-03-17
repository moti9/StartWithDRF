from django.db import models

# Create your Book model here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
# Create Meta class inside the Book model

    def __str__(self) -> str:
        return f"{self.author}-{self.title}"

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
