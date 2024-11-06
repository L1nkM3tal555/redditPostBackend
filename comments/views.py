from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from comments.models import Comentario
from comments.serializers import ComentarioSerializer

class CrearComentarioView(APIView):
    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            print("Is valid")
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response({"message": "Funciona el GET en CrearComentarioView"}, status=status.HTTP_200_OK)

class ResponderComentarioView(APIView):    
    def post(self, request, responseCommentId):
        try:
            responseComment = Comentario.objects.get(id=responseCommentId)
        except Comentario.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ComentarioSerializer(data={**request.data, 'responseComment':responseComment.id})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class ListarComentariosView(ListAPIView):
    queryset = Comentario.objects.filter(responseComment__isnull=True)
    serializer_class = ComentarioSerializer