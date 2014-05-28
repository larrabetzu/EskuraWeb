from rest_framework import serializers

from .models import Sarrera


class SarrerakSerializers(serializers.HyperlinkedModelSerializer):
    bloga = serializers.SerializerMethodField('bloganIzena')

    def bloganIzena(self, obj):
        return obj.izena()

    class Meta:
        model = Sarrera
        fields = ('tituloa', 'sarrera_data', 'sarrera_link', 'bloga')