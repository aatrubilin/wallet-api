"""."""

from rest_framework import status
from rest_framework.test import APIClient

from wallet_api.apps.wallet.models.transaction import Transaction


def test_get_list(api_client: APIClient, transaction_model: Transaction):
    """Test get list."""
    response = api_client.get("/api/transactions/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    transaction_data = response.data["results"][0]
    assert transaction_data["id"] == transaction_model.id
    assert transaction_data["txid"] == transaction_model.txid
    assert transaction_data["amount"] == str(transaction_model.amount)


def test_get_by_id(api_client: APIClient, transaction_model: Transaction):
    """Test get by id."""
    response = api_client.get(f"/api/transactions/{transaction_model.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": transaction_model.id,
        "txid": str(transaction_model.txid),
        "amount": str(transaction_model.amount),
    }
