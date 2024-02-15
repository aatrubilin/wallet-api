"""."""

from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


class Wallet(models.Model):
    """Wallet model."""

    label: str = models.TextField(_("label"))
    balance: Decimal = models.DecimalField(
        _("balance"),
        max_digits=50,
        decimal_places=18,
        default=Decimal("0.0"),
    )

    def __str__(self) -> str:
        """."""
        return f"Wallet({self.id})"

    def __repr__(self) -> str:
        """."""
        return f"<Wallet(id={self.id})>"
