"""."""

from rest_framework import serializers

from wallet_api.apps.wallet.models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer[Wallet]):
    """Wallet serializer."""

    class Meta:
        """."""

        model = Wallet
        fields = ["id", "label", "balance"]
        read_only_fields = ["balance"]


class TransactionSerializer(serializers.ModelSerializer[Transaction]):
    """Transaction serializer."""

    wallet_id = serializers.PrimaryKeyRelatedField(
        queryset=Wallet.objects.all(),
        source="wallet",
        write_only=True,
        allow_null=False,
    )

    class Meta:
        """."""

        model = Transaction
        fields = ["id", "wallet_id", "txid", "amount"]
