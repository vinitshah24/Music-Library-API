from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):
    page_size = 10
    default_limit = 5
    max_limit = 20


class CustomSingleObjectPagination(pagination.LimitOffsetPagination):
    page_size = 1
    default_limit = 1
    max_limit = 10
