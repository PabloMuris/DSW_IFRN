from django import forms
from .models import Categoria,Produto,Fornecedor

class FornecedorForms(forms.Form):
    
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ProdutoForms(forms.Form):
    
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaForms(forms.Form):
    
    class Meta:
        model = Categoria
        fields = '__all__'


    

