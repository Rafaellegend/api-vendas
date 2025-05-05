from django.contrib import admin
from vendas.models import Produto, Categoria

class Produtos(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque', 'categoria', 'criado_em', 'atualizado_em',)
    list_display_links = ('nome',)
    list_per_page = 20
    search_fields = ('nome', 'categoria__nome')
    ordering = ('nome','-criado_em',)

admin.site.register(Produto, Produtos)

class Categorias(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criado_em', 'atualizado_em',)
    list_display_links = ('nome',)
    list_per_page = 20
    search_fields = ('nome',)
    ordering = ('nome', '-criado_em',)

admin.site.register(Categoria, Categorias)