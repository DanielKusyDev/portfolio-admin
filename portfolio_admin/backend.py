from storages.backends.azure_storage import AzureStorage

from portfolio_admin.settings import (
    AZURE_STORAGE_NAME,
    AZURE_STORAGE_ACCESS_KEY,
    AZURE_MEDIA_CONTAINER_NAME,
    AZURE_STATIC_CONTAINER_NAME,
)


class AzureMediaStorage(AzureStorage):
    account_name = AZURE_STORAGE_NAME
    account_key = AZURE_STORAGE_ACCESS_KEY
    azure_container = AZURE_MEDIA_CONTAINER_NAME
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = AZURE_STORAGE_NAME
    account_key = AZURE_STORAGE_ACCESS_KEY
    azure_container = AZURE_STATIC_CONTAINER_NAME
    expiration_secs = None
