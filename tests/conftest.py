"""."""
import pytest
from rest_framework.test import APIClient

from tests.factories.wallet import TransactionFactory, WalletFactory
from wallet_api.apps.wallet.models.transaction import Transaction
from wallet_api.apps.wallet.models.wallet import Wallet


@pytest.fixture
def wallet_model(db: None) -> Wallet:
    """."""
    return WalletFactory()


@pytest.fixture
def transaction_model(db: None) -> Transaction:
    """Transaction model."""
    return TransactionFactory()


@pytest.fixture
def api_client(db: None) -> APIClient:
    """Api client."""
    return APIClient()
