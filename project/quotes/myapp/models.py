from django.db import models


from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.text} - {self.author}"
