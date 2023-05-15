from django.urls import path

from . import views

urlpatterns = [
    path("contato/", views.contato, name="contato"),
    path("contatos/", views.contatos, name="contatos"),
    path("contato/<int:id>/", views.detalhes, name="detalhes"),
]
