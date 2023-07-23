from django.db import models


class WebsiteFixTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WebsiteFix(models.Model):
    STATUS_CHOICES = (
        ('Done', 'Done'),
        ('Not Fixed', 'Not Fixed'),
        ('In Progress', 'In Progress'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Fixed')
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(WebsiteFixTag)

    def __str__(self):
        return f"{self.title} - {self.status} - {self.tags}"