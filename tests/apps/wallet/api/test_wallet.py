"""."""

from rest_framework import status
from rest_framework.test import APIClient

from wallet_api.apps.wallet.models.wallet import Wallet


def test_get_list(api_client: APIClient, wallet_model: Wallet):
    """Test get list."""
    response = api_client.get("/api/wallets/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    wallet_data = response.data["results"][0]
    assert wallet_data["id"] == wallet_model.id
    assert wallet_data["label"] == wallet_model.label
    assert wallet_data["balance"] == str(wallet_model.balance)


def test_get_by_id(api_client: APIClient, wallet_model: Wallet):
    """Test get by id."""
    response = api_client.get(f"/api/wallets/{wallet_model.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": wallet_model.id,
        "label": wallet_model.label,
        "balance": str(wallet_model.balance),
    }


def test_create(api_client: APIClient):
    """Test create."""
    assert Wallet.objects.all().count() == 0
    response = api_client.post(
        "/api/wallets/",
        {"data": {"type": "Wallet", "attributes": {"label": "test"}}},
        format="vnd.api+json",
    )
    assert response.data["label"] == "test"
    assert response.data["balance"] == "0.000000000000000000"

    assert Wallet.objects.get(id=response.data["id"]).label == "test"


def test_update(api_client: APIClient, wallet_model: Wallet):
    """Test update."""
    assert wallet_model.label != "test"
    assert wallet_model.balance != "0.0000000000000000"
    response = api_client.put(
        f"/api/wallets/{wallet_model.id}/",
        {
            "data": {
                "type": "Wallet",
                "id": wallet_model.id,
                "attributes": {"label": "test", "balance": "0.0000000000000000"},
            }
        },
        format="vnd.api+json",
    )
    assert response.status_code == status.HTTP_200_OK

    updated_wallet = Wallet.objects.get(id=wallet_model.id)
    assert updated_wallet.label == "test"
    assert updated_wallet.balance != "0.0000000000000000"
