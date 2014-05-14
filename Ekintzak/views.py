from rest_framework import viewsets

from .models import Ekintza


class EkintzakViewSet(viewsets.ModelViewSet):
    model = Ekintza