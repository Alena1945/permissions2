from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filters_class = AdvertisementFilter


def get_permissions(self):
    """Получение прав для действий."""
    if self.action in ["create", "update", "partial_update"]:
        return [IsAuthenticated()]
    return []
