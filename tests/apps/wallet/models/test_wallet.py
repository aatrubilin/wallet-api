"""."""

from wallet_api.apps.wallet.models.wallet import Wallet


def test_str(wallet_model: Wallet):
    """."""
    assert str(wallet_model) == f"Wallet({wallet_model.id})"


def test_repr(wallet_model: Wallet):
    """."""
    assert repr(wallet_model) == f"<Wallet(id={wallet_model.id})>"
