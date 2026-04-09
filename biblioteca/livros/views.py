from rest_framework import viewsets, permissions 
from .models import Autor, Livro 
from .serializers import AutorSerializer, LivroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AutorViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
    
class LivroViewSet(viewsets.ModelViewSet): 
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class LivroListView(APIView):
    
    def get(self, request):
        autor_id = request.query_params.get('autor')
        livros = Livro.objects.all()
        if autor_id:
            try:
                livros = livros.filter(autor_id=int(autor_id))
            except ValueError:
                return Response({"erro": "ID do autor deve ser um número válido"},
                status=status.HTTP_400_BAD_REQUEST
                )
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)