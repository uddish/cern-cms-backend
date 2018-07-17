from rest_framework.pagination import PageNumberPagination


class BackupArchiveRawPagination(PageNumberPagination):
    page_size = 10

class BackupSetsPagination(PageNumberPagination):
    page_size = 10

class BackupOperationsPagination(PageNumberPagination):
    page_size = 10
