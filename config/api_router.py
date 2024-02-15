"""."""

from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from wallet_api.apps.wallet.api.views import TransactionViewSet, WalletViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("wallets", WalletViewSet)
router.register("transactions", TransactionViewSet)


app_name = "api"
urlpatterns = router.urls
