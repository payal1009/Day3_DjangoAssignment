from django.db import models
class event_scheduler(models.Model):
    #index = models.Index()
    name = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.name},{self.date},{self.time},{self.description}"