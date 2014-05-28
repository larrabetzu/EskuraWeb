from rest_framework import viewsets

from .models import Sarrera
from .serializers import SarrerakSerializers

class SarrerakViewSet(viewsets.ModelViewSet):
    model = Sarrera
    serializer_class = SarrerakSerializers