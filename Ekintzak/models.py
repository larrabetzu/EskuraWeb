from django.db import models

from Elkarteak.models import Elkartea

class Ekintza(models.Model):
    tituloa = models.CharField(max_length=140)
    ekintzanOrdue = models.DateTimeField()
    ekintzanAmaieranOrdue = models.DateTimeField()
    lekua = models.CharField(max_length=140)
    deskribapena = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=True)
    kartela = models.ImageField(upload_to='kartelak/', blank=True, null=True)
    sortzailea = models.ManyToManyField(Elkartea)

    def __unicode__(self):
        return self.tituloa #return "%s - %s "% (self.nor,self.tituloa)