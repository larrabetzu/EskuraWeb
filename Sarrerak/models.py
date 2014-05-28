from django.db import models

from Blogak.models import Bloga

class Sarrera(models.Model):
    tituloa = models.CharField(max_length=140)
    sarrera_data = models.DateTimeField()
    sarrera_link = models.URLField()
    bloga = models.ForeignKey(Bloga)

    def izena(self):
        return self.bloga.izena

    def __unicode__(self):
        return self.tituloa #return "%s - %s "% (self.nor,self.tituloa)
