from rest_framework import pagination

class APIPagination(pagination.PageNumberPagination):
  page_size = 5