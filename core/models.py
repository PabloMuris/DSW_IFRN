from django.db import models

# Create your models here.



class Fornecedor(models.Model):
    nome_do_fornecedor = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_do_fornecedor
    

class Categoria(models.Model):
    nome_da_categoria = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)
    codigo_da_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_da_categoria
    



class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo_do_produto = models.CharField(max_length=200,unique=True)
    descricao = models.TextField(max_length=400)
    quantidade_em_estoque = models.IntegerField()
    preco = models.DecimalField(decimal_places=2,max_digits=10)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)