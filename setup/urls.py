from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from vendas.views import CategoriaViewSet, ProdutoViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet, basename='Produto')
router.register('categorias', CategoriaViewSet, basename='Categoria')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
