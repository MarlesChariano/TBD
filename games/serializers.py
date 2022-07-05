from rest_framework import serializers
from .models import Games

class insertGame(serializers.Serializer):
    titulo = serializers.CharField()
    genero = serializers.CharField()
    anolanzamiento = serializers.IntegerField()

    class Meta:
        model = Games
        fields = ('titulo','genero','anolanzamiento')

class buscarGame(serializers.Serializer):
    titulo = serializers.CharField()

class updateGamme(serializers.Serializer):
    titulo = serializers.CharField()
    genero = serializers.CharField()
    anolanzamiento = serializers.IntegerField()

class deleteGame(serializers.Serializer):
    titulo = serializers.CharField()
