from rest_framework import viewsets

from .models import Sarrera


class SarrerakViewSet(viewsets.ModelViewSet):
    model = Sarrera