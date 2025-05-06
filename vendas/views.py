from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from vendas.models import Produto, Categoria
from vendas.serializer import ProdutoSerializer, CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'categoria__nome', 'decricao']
    serializer_class = ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer