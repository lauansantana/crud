from django.shortcuts import render
from .models import Estudante
from django.shortcuts import redirect

# Create your views here.

def home(request):
    crud=Estudante.objects.all()

    return render(request, "crud/home.html", {'crud':crud})

def crud_add(request):
    if request.method=='POST':
        print('Adicionado')
        crud2_matricula=request.POST.get("crud_matricula")
        crud2_nome=request.POST.get("crud_nome")
        crud2_email=request.POST.get("crud_email")
        crud2_endereco=request.POST.get("crud_endereco")
        crud2_telefone=request.POST.get("crud_telefone")

        s=Estudante()
        s.matricula=crud2_matricula
        s.nome=crud2_nome
        s.email=crud2_email
        s.endereco=crud2_endereco
        s.telefone=crud2_telefone

        s.save()


    return render(request, "crud/add_crud.html", {})


def delete_crud(request, matricula):
    s=Estudante.objects.get(pk=matricula)
    s.delete()

    return redirect("/crud/home")

def atualizar_crud(request, matricula):
    crud=Estudante.objects.get(pk=matricula)

    return render(request, "crud/atualizar_crud.html", {'crud':crud})

def a_atualizar_crud(request,matricula):
    crud_matricula=request.POST.get('crud_matricula')
    crud_nome=request.POST.get('crud_nome')
    crud_email=request.POST.get('crud_email')
    crud_endereco=request.POST.get('crud_endereco')
    crud_telefone=request.POST.get('crud_telefone')

    crud=Estudante.objects.get(pk=matricula)
    
    crud.matricula=crud_matricula
    crud.nome=crud_nome
    crud.email=crud_email
    crud.endereco=crud_endereco
    crud.telefone=crud_telefone

    crud.save()
    return redirect("/crud/home")