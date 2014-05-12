from django.db import models

class Elkartea(models.Model):
    nor = models.CharField(max_length=30)
    email = models.EmailField()
    webgunea = models.URLField()

    def __unicode__(self):
        return self.nor
