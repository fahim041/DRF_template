from rest_framework.pagination import PageNumberPagination


class DefailtPagination(PageNumberPagination):
    page_size = 10
