from tcsiapp.views import tcsielement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from tcsiapp.models import TcsiElement
from .serializers import TcsiElementSerializer
from tcsiapp.api import serializers


class TcsiElementApiView(APIView):
    # auth permission check
    #permission_classes = [permissions.IsAuthenticated]

    # List All
    def get(self, request, *args, **kwargs):
        tcsielements = TcsiElement.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        tcsielements_paginated = paginator.paginate_queryset(tcsielements, request)
        serializer = TcsiElementSerializer(tcsielements_paginated, many=True)
        return paginator.get_paginated_response(serializer.data)
