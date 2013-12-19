from django.db import models


class Autor(models.Model):
    nor = models.CharField(max_length=30)
    email = models.EmailField()
    webgunea = models.URLField()

    def __unicode__(self):
        return self.nor


class Ekintza(models.Model):
    tituloa = models.CharField(max_length=100)
    egune = models.DateTimeField()
    lekua = models.CharField(max_length=100)
    deskribapena = models.CharField(max_length=600)
    pub_date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=True)
    kartela = models.ImageField(upload_to='kartelak/',blank=True,null=True)
    sortzailea = models.ManyToManyField(Autor)

    def __unicode__(self):
        return self.tituloa #return "%s - %s "% (self.nor,self.tituloa)
