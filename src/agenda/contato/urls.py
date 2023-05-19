from django.urls import path, include

from rest_framework_nested import routers
from .api import CategoriaViewSet, ContatoViewSet

from . import views

api_router = routers.DefaultRouter()
api_router.register(r"categorias", CategoriaViewSet)

categorias_router = routers.NestedDefaultRouter(
    api_router, r"categorias", lookup="categoria"
)

categorias_router \
    .register(
    r"contatos", 
    ContatoViewSet, 
    basename="categoria-contatos")

urlpatterns = [
    path("contato/", views.contato, name="contato"),
    path("contatos/", views.contatos, name="contatos"),
    path("contato/<int:id>/", views.detalhes, name="detalhes"),
    path("api/", include(api_router.urls)),
    path("api/", include(categorias_router.urls)),
]
