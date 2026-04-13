from drf_hal_json.serializers import HalModelSerializer
from rest_framework.reverse import reverse
from .models import Autor, Livro

class SafeHalModelSerializer(HalModelSerializer):
    class Meta:
        ref_name = None
        nested_fields = []

class AutorSerializer(SafeHalModelSerializer): 
    
    class Meta:
        model = Autor
        fields = ['id', 'nome']
        ref_name = "AutorHAL"
        nested_fields = [] # evita introspecção recursiva
        
    def get__links(self, obj):
        request = self.context.get('request')
        
        links = {
            "self": reverse('autor-detail', args=[obj.pk], request=request),
            "livros": reverse('livro-list', request=request) + f"?autor={obj.pk}"
        }
        user = request.user if request else None
        if user and user.is_authenticated and user.has_perm('livros.change_autor'):
            links['editar'] = reverse('autor-detail', args=[obj.pk], request=request)
            links['excluir'] = reverse('autor-detail', args=[obj.pk], request=request)
        return links


class LivroSerializer(SafeHalModelSerializer):
    autor = AutorSerializer(read_only=True)
    
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor']
        ref_name = "LivroHAL"
        nested_fields = [] # evita introspecção recursiva
        
    def get__links(self, obj):
        request = self.context.get('request')
        return {
            "self": reverse('livro-detail', args=[obj.pk], request=request),
            "autor": reverse('autor-detail', args=[obj.autor.pk], request=request)
        }
