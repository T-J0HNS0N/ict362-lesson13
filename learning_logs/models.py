# learning_logs
from django.db import models


#find out what the user needs
class Topic(models.Model):
    """What topic is this"""
    subject1 = models.CharField(max_length=200)
    subject2 = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Print out class """
        if self.subject2:
            return f"{self.subject1} - {self.subject2}"
        return self.subject1


#get more specific
class Entry(models.Model):
    """What did I learn about this topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Print out class """
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text