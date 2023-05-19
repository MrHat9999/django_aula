from rest_framework import serializers
from rest_framework import permissions

from .models import Categoria, Contato


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        


class ContatoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Contato
        fields = '__all__'