from django.db import models


class Autor(models.Model): 
    
    nome = models.CharField(max_length=100, blank=False, null=False) 
    
    nacionalidade = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self): 
        return f"{self.nome} - {self.nacionalidade}"


class Livro(models.Model): 
    
    titulo = models.CharField(max_length=200, blank=False, null=False) 

    ano_publicacao = models.IntegerField(blank=False, null=False) 
    
    autor = models.ForeignKey(Autor, related_name="livros", on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self): 
        return f"{self.titulo} - {self.ano_publicacao}"