from rest_framework import viewsets
from . import models
from . import serializers

class NotebookViewset(viewsets.ModelViewSet):
    queryset = models.Notebook.objects.all()
    serializer_class = serializers.NotebookSerializer

