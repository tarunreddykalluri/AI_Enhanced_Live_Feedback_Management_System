# from django.db import models

# class Feedback(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     movie = models.CharField(max_length=100)
#     email = models.EmailField()
#     feed = models.TextField()

#     def __str__(self):
#         return f"{self.name} ({self.movie})"

# models.py
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    movie = models.CharField(max_length=100)
    email = models.EmailField()
    feed = models.TextField()

    # --- THESE 4 LINES ARE THE FIX ---
    sentiment = models.CharField(max_length=50, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    suggestions = models.TextField(null=True, blank=True)
    is_analyzed = models.BooleanField(default=False)