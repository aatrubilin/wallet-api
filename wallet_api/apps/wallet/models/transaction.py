"""."""

import uuid
from decimal import Decimal

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from .wallet import Wallet


class Transaction(models.Model):
    """Transaction model."""

    wallet: Wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    txid: uuid.UUID = models.UUIDField(
        _("txid"),
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    amount: Decimal = models.DecimalField(
        _("amount"),
        max_digits=50,
        decimal_places=18,
        default=Decimal("0.0"),
    )

    def __str__(self) -> str:
        """."""
        return f"Transaction({self.id})"

    def __repr__(self) -> str:
        """."""
        return f"<Transaction(id={self.id}, txid='{self.txid}')>"

    def save(self, *args, **kwargs):
        """."""
        if self.id is None:
            with transaction.atomic():
                super().save(*args, **kwargs)
                Wallet.objects.filter(id=self.wallet_id).update(
                    balance=models.F("balance") + self.amount
                )
        else:
            raise RuntimeError("Update is not permitted")
