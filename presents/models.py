from django.db import models


class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
# will need attribute to say whether a present is still required or not.

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    idea_link = models.CharField(max_length=255, blank=True, default='')
    recipient = models.ForeignKey(Person, on_delete=models.CASCADE)
    suggested_by = models.CharField(max_length=255, blank=True, default='')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title
