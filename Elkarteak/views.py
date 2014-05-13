from rest_framework import viewsets

from .models import Elkartea

class ElkarteaViewSet(viewsets.ModelViewSet):
    model = Elkartea
