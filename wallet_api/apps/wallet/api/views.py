"""."""

from rest_framework import filters
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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["label"]
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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["txid"]
    lookup_field = "pk"
    ordering = ["pk"]
