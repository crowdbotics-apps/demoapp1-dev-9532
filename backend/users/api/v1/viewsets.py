from rest_framework import authentication
from users.models import Address
from .serializers import AddressSerializer
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Address.objects.all()
