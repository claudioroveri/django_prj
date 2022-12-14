from django.shortcuts import render, redirect 
from app.model.Carros import Carros
from app.model.Marca import Marca
from app.model.Usuario import Usuario
from app.model.Cliente import Cliente
from app.controller.CarrosForm import CarrosForm
from app.controller.MarcaForm import MarcaForm
from app.controller.UsuarioForm import UsuarioForm 
from app.controller.ClienteForm import ClienteForm 
from app.controller.UserForm import UserForm
from app.controller.UserGroupForm import UserGroupForm
from app.model.CarrosDAO import CarrosDAO
from app.model.ClienteDAO import ClienteDAO
from app.model.MarcaDAO import MarcaDAO
from app.model.GroupDAO import GroupDAO
from rest_framework.viewsets import ModelViewSet
from app.api.serializers import CarrosSerializer, MarcaSerializer, UsuarioSerializer, ClienteSerializer
import requests, json
from django.contrib.auth.decorators import login_required #forma automática de exigir login de acesso
from django.contrib.auth.models import User, Group

# Aqui são criadas as views vinculadas com os models.
# Aqui também se prepara os dados que sera vinculados
# e trabalhados na interface
# @login_required ==> forma automática de exigir autenticacao para acessar pagina
@login_required 
def carro(request):
    data={}
    
    # Vindo de um modelo comum
    #data['db'] = Carros.objects.all()

    # Vindo de uma API REST via requisição GET
    #r = requests.get("http://localhost:8000/api/v1/carros")
    #data['db'] = r.json()

    #Listagem personalizada
    data['db'] = CarrosDAO.listarCarros()
    data['sumario'] = CarrosDAO.getMaxMarca()
    return render(request, 'listaCarros.html', data)

@login_required 
def cliente(request):
    data={}
    
    # Vindo de um modelo comum
    #data['db'] = Carros.objects.all()

    # Vindo de uma API REST via requisição GET
    #r = requests.get("http://localhost:8000/api/v1/carros")
    #data['db'] = r.json()

    #Listagem personalizada
    data['db'] = ClienteDAO.listarClientes()
    return render(request, 'listaClientes.html', data)

# Muda um pouco a forma padrão de obter os campos porque 
# usa o modelo de criacao de usuario do do framework
def addUser(request):
  
        # Create user and save to the database
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        
        # Update fields and then save again
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Adicionando usuário ao grupo
        grupo = Group.objects.get(pk=request.POST.get('grupo')) 
        grupo.user_set.add(user)
        
        # Não funcionou a gravação da senha criptografada
        #form = UserForm(request.POST or None)  
    
        #if form.is_valid():
        #    form.save()
        
        return render(request, 'menu.html', {})

# foi criado um html customizado para criacao de usuario
# na tabela de controle de usuario de sessao do django
def createUser(request):
    data = {}
    data['form'] = UserForm()
    data['groups'] = GroupDAO.listarGrupos()
    return render(request, 'registration/createUser.html', data)

def usuario(request):
    data={}
    
    # Vindo de um modelo comum
    #data['db'] = Carros.objects.all()

    # Vindo de uma API REST via requisição GET
    r = requests.get("http://localhost:8000/api/v1/usuarios")
    data['db'] = r.json()

def removeUsuario(request, pk):
    data = {}
    r = requests.delete("http://localhost:8000/api/v1/usuarios/" + str(pk))
    data['db'] = r.json()

@login_required
def marca(request):
    data={}
    
    # Vindo de um modelo comum
    #data['db'] = Carros.objects.all()

    # Vindo de uma API REST via requisição GET
    r = requests.get("http://localhost:8000/api/v1/marca")
    data['db'] = r.json()

    #Listagem personalizada
    #data['db'] = MarcaDAO.listarMarcas()
    return render(request, 'listaMarca.html', data)

def delete(request, pk):
     db = Carros.objects.get(pk=pk)
     db.delete()
     return redirect('carro')

def home(request):
    return render(request, 'menu.html', {})

# Apaga os dados utilizando API REST do django
def deleteCarros(request, pk):
    r = requests.delete("http://localhost:8000/api/v1/carros/"+ str(pk))
    #print(r)
    return redirect('carro')

def deleteMarca(request, pk):
    r = requests.delete("http://localhost:8000/api/v1/marca/"+ str(pk))
    #print(r)
    return redirect('marca')

def deleteCliente(request, pk):
    r = requests.delete("http://localhost:8000/api/v1/cliente/"+ str(pk))
    #print(r)
    return redirect('cliente')

def form(request):
    data = {}
    data['form'] = CarrosForm()
    
    # Combo de Marcas
    r = requests.get("http://localhost:8000/api/v1/marca")
    data['combo'] = r.json()
    
    return render(request, 'formCarro.html', data)

def formMarca(request):
    data = {}
    data['form'] = MarcaForm()
     
    return render(request, 'formMarca.html', data)

def formUsuario(request):
    dadosUsuario={}
    dadosUsuario['campos'] = UsuarioForm()

    return render(request, 'formUsuario.html', dadosUsuario )

def formCliente(request):
    dadosCliente={}
    dadosCliente['campos'] = ClienteForm()
  

    return render(request, 'formCliente.html', dadosCliente )

def create(request):
    form = CarrosForm(request.POST or None)  
    
    if form.is_valid():
        form.save()
        return redirect('carro')

def createMarca(request):
    form = MarcaForm(request.POST or None)  
    
    if form.is_valid():
        form.save()
        return redirect('marca')

def createCliente(request):
    form = ClienteForm(request.POST or None)  
    if form.is_valid():
        form.save()
        return redirect('cliente')

def view(request,pk):
    data={}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])

     # Combo de Marcas
    r = requests.get("http://localhost:8000/api/v1/marca")
    data['combo'] = r.json()

    return render(request, 'formCarro.html', data)

def editMarca(request, pk):
    data = {}
    data['db'] = Marca.objects.get(pk=pk)
    data['form'] = MarcaForm(instance=data['db'])

    return render(request, 'formMarca.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('carro')

def updateMarca(request, pk):
    data = {}
    data['db'] = Marca.objects.get(pk=pk)
    form = MarcaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('marca')


class CarrosViewSet(ModelViewSet):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

