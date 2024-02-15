"""."""

import factory
from factory.django import DjangoModelFactory

from wallet_api.apps.wallet.models.transaction import Transaction
from wallet_api.apps.wallet.models.wallet import Wallet


class WalletFactory(DjangoModelFactory):
    """Wallet factory."""

    label = factory.Faker("pystr", min_chars=1, max_chars=10)
    balance = factory.Faker("pydecimal", left_digits=32, right_digits=18)

    class Meta:
        """."""

        model = Wallet


class TransactionFactory(DjangoModelFactory):
    """Transaction factory."""

    wallet = factory.SubFactory(WalletFactory)
    txid = factory.Faker("uuid4")
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=18)

    class Meta:
        """."""

        model = Transaction
