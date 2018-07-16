from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class BackupArchiveRawPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BackupArchiveRawOffset(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
