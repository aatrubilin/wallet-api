"""."""

from django.db import transaction
from django.db.models import F
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from wallet_api.apps.wallet.models import Transaction, Wallet

from .serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    """Wallet viewset."""

    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    lookup_field = "pk"
    ordering = ["pk"]


class TransactionViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """Transaction viewset."""

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field = "pk"
    ordering = ["pk"]
