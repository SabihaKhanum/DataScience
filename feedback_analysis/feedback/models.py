from django.db import models



class CustomerFeedback(models.Model):
    review = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.review[:50]  # Show first 50 characters