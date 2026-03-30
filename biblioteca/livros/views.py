from rest_framework import viewsets, permissions 
from .models import Autor, Livro 
from .serializers import AutorSerializer, LivroSerializer 


class AutorViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
    
class LivroViewSet(viewsets.ModelViewSet): 
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 