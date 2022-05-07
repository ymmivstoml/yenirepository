from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Dumdatas(models.Model):
    kartid = models.CharField(max_length=200)
    zaman = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kartid

    def get_absolute_url(self):
        return reverse("listing")
