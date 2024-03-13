from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from products.api.serializers import ProductSerializer
from stores.models import Store
from .serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Store.objects.all().order_by('-created_at')
    serializer_class = StoreSerializer
    lookup_field = 'slug'
    
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # Pagina a consulta
        serializer = self.get_serializer(queryset, many=True)
        #TODO: Adicionar a quantidade de produtos no serializer
        #TODO: Encontrar uma forma mehor de fazer isso
        for item in serializer.data:
            item['products'] = item['products'][:3]
        return self.get_paginated_response(serializer.data)
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        request.data['message-Teste'] = 'Teste de mensagem!'
        object: Store = self.get_object()
        object_serialized: StoreSerializer = self.get_serializer(object)
        return Response(object_serialized.data)
        return super().retrieve(request, *args, **kwargs)