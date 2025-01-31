from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_da_categoria', 'descricao', 'codigo_da_categoria')
    search_fields = ('nome_da_categoria', 'descricao')

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome_do_fornecedor', 'grupo')
    search_fields = ('nome_do_fornecedor', 'grupo')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_do_produto', 'nome', 'preco', 'quantidade_em_estoque', 'created_at')
    search_fields = ('codigo_do_produto', 'nome')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
