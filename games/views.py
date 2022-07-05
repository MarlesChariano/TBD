from requests import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Games
from . import serializers

class allGameView(APIView):

    serializer_class = serializers.insertGame

    def get(self, format=None):
        game = serializers.insertGame(Games.objects.all(), many=True)
        self.data = game.data
        return Response(self.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data.get('titulo')
            genero = serializer.validated_data.get('genero')
            anolanzamiento = serializer.validated_data.get('anolanzamiento')

            temp = Games(titulo=titulo,genero=genero,anolanzamiento=anolanzamiento)
            temp.save()
            return Response(status=status.HTTP_200_OK)
        
        else: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class deleteGameView(APIView):

    serializer_class = serializers.deleteGame

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data.get('titulo')

            temp = Games.objects.get(titulo=titulo)
            temp.delete()
            return Response(status=status.HTTP_200_OK)
        
        else: 
            return Response(status=status.HTTP_400_BAD_REQUEST)

class updateGameView(APIView):

    serializer_class = serializers.updateGamme

    def get(self, format=None):
        game = serializers.insertGame(Games.objects.all(), many=True)
        self.data = game.data
        return Response(self.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data.get('titulo')
            genero = serializer.validated_data.get('genero')
            anolanzamiento = serializer.validated_data.get('anolanzamiento')

            temp = Games.objects.filter(titulo=titulo)
            temp.update(genero=genero,anolanzamiento=anolanzamiento)

            game = serializers.insertGame(Games.objects.filter(titulo=titulo), many=True)
            self.data = game.data
            return Response(self.data)
        
        else: 
            return Response(status=status.HTTP_400_BAD_REQUEST)