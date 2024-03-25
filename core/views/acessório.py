from rest_framework.viewsets import ModelViewSet

from core.models import acessorio
from core.serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = acessorio.objects.all()
    serializer_class = AcessorioSerializer
