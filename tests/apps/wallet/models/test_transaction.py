"""."""

from decimal import Decimal

import pytest

from tests.factories.wallet import WalletFactory
from wallet_api.apps.wallet.models.transaction import Transaction
from wallet_api.apps.wallet.models.wallet import Wallet


def test_str(transaction_model: Transaction):
    """."""
    assert str(transaction_model) == f"Transaction({transaction_model.id})"


def test_repr(transaction_model: Transaction):
    """."""
    assert (
        repr(transaction_model)
        == f"<Transaction(id={transaction_model.id}, txid='{transaction_model.txid}')>"
    )


def test_save(db: None):
    """Test save."""
    wallet_model: Wallet = WalletFactory(balance=Decimal("0.0"))
    assert wallet_model.balance == 0.0

    Transaction.objects.create(wallet=wallet_model, amount=Decimal("1001.2002"))
    assert Wallet.objects.get(id=wallet_model.id).balance == Decimal("1001.2002")

    tr = Transaction.objects.create(wallet=wallet_model, amount=Decimal("-501.2002"))
    assert Wallet.objects.get(id=wallet_model.id).balance == Decimal("500.0")

    with pytest.raises(RuntimeError):
        tr.save()
