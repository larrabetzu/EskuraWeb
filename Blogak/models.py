from django.db import models

class Bloga(models.Model):
    izena = models.CharField(max_length=140)
    rss_link = models.URLField()

    def __unicode__(self):
        return self.izena #return "%s - %s "% (self.nor,self.tituloa)