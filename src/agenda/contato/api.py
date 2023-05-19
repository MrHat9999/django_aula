from rest_framework import viewsets, permissions

from .models import Categoria, Contato
from .serializers import CategoriaSerializer, ContatoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('nome').all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer

    def get_queryset(self):
        return Contato.objects \
            .select_related('categoria') \
                .filter(categoria=self.kwargs['categoria_pk'])