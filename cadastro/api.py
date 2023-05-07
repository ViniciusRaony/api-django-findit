from ninja import Router, ModelSchema
from .models import Cadastro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpRequest

cadastro_router = Router()


class CadastroSchema(ModelSchema):
    class Config:
        model = Cadastro
        model_fields = ['titulo', 'status']


@cadastro_router.get('cadastro/')
def listar(request):
    cadastro = Cadastro.objects.all()  # QuerySet
    response = [{'id': i.id, 'titulo': i.titulo, 'status': i.status} for i in
                cadastro]  # List comprehension para serializar
    print(response)
    return response


@cadastro_router.get('cadastro/{id}')
def listar_individual(request, id: int):
    cadastro = get_object_or_404(Cadastro, id=id)
    return model_to_dict(cadastro)


@cadastro_router.post("cadastro", response=CadastroSchema)
def criar_cadastro(request, cadastro: CadastroSchema):
    cadastro = Cadastro(**cadastro.dict())
    cadastro.save()
    return cadastro


@cadastro_router.put('cadastro/{id}', response=CadastroSchema)
def atualizar_cadastro(request, id: int, teste: CadastroSchema):
    cadastro = get_object_or_404(Cadastro, id=id)
    for attr, value in teste.dict().items():
        setattr(cadastro, attr, value)
    cadastro.save()
    return cadastro


@cadastro_router.delete("cadastro/{id}")
def deletar_cadastro(request, id: int):
    cadastro = get_object_or_404(Cadastro, id=id)
    cadastro.delete()
    return {"success": 'Cadastro deletado com sucesso'}
