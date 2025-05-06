from django.db import models

class Produto(models.Model):
    '''
    Modelo Produto
        - `nome`: 
            - Máximo 255 caracteres
        - `descricao`: 
            - Campo opcional
            - Máximo 1000 caracteres
        - `preco`: 
            - Deve ser um número decimal positivo.
        - `quantidade_estoque`: 
            - Deve ser um número inteiro positivo.
        - `categoria`: 
            - Chave estrangeira para o modelo `Categoria`
            - Deve ser uma categoria existente no sistema.
        - `imagem`: 
            - Campo opcional
            - Deve ser uma URL válida para uma imagem.
        - `criado_em`: 
            - Campos automáticos gerados pelo sistema.
        - `atualizado_em`: 
            - Campos automáticos gerados pelo sistema.
    '''
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagem = models.URLField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    '''
    Modelo Categoria
        - `nome`:
            - Máximo 100 caracteres
        - `descricao`:
            - Campo opcional
            - Máximo 500 caracteres
        - `criado_em`:
            - Campos automáticos gerados pelo sistema
        - `atualizado_em`:
            - Campos automáticos gerados pelo sistema
    '''
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500,blank=True,null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)