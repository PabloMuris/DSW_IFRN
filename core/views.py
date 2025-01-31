from django.shortcuts import render,redirect
from .forms import CategoriaForms,ProdutoForms,FornecedorForms
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Fornecedor, Categoria, Produto

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'listar_fornecedores.html', {'fornecedores': fornecedores})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def formulario_produto(request):
    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('pagina_sucesso') 
    else:
        form = ProdutoForms()

    return render(request, 'cadastrar_produto.html', {'form': form})

def formulario_categoria(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('pagina_sucesso') 
    else:
        form = CategoriaForms()

    return render(request, 'cadastrar_categoria.html', {'form': form})

def formulario_Fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForms(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('pagina_sucesso') 
    else:
        form = FornecedorForms()

    return render(request, 'cadastrar_fornecedor.html', {'form': form})

