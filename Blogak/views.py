from rest_framework import viewsets

from .models import Bloga


class BlogakViewSet(viewsets.ModelViewSet):
    model = Bloga