from django.db import models

# Create your models here.
class Login(models.Model):
    user = models.CharField(max_length=200, null=False, blank=False)
    passkey = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.user