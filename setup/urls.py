from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from vendas.views import CategoriaViewSet, ProdutoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view( 
    openapi.Info(
        title="API Vendas",
        default_version='v1',
        description="API para controle de vendas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="RafaeldeJesus_Work@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet, basename='Produto')
router.register('categorias', CategoriaViewSet, basename='Categoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
