from rest_framework import serializers
from vendas.models import Produto, Categoria

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        read_only_field = ( 'criado_em', 'atualizado_em',)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_field = ( 'criado_em', 'atualizado_em',)