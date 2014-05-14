from rest_framework import viewsets

from .models import Elkartea

class ElkarteakViewSet(viewsets.ModelViewSet):
    model = Elkartea
