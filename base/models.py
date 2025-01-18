from django.db import models


class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name