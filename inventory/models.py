from django.db import models

class Carpet(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)  # مثلاً 6 متری، 9 متری
    stock = models.PositiveIntegerField()  # موجودی
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='carpet_images/', null=True, blank=True)

    def __str__(self):
        return self.name
