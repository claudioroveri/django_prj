from app.model.Carros import Carros
from app.model.Marca import Marca
from django.db.models import Count

class CarrosDAO:

    # Lista os carros de forma personalizada
    def listarCarros():
        lista = []
        dados = Carros.objects.all()

        for dado in dados:
            descricao = Marca.objects.get(pk=dado.marca.id).descricao
            linha = {}
            linha['id'] = dado.id
            linha['marca'] = descricao
            linha['modelo'] = dado.modelo
            linha['ano'] = dado.ano
            linha['automatico'] = "Sim" if dado.automatico == True else "Não" #ternario
            lista.append(linha) # só exibe o ultimo
        return lista

    # Retorna a marca de carro mais comprada (usa join entre tabelas)
    def getMaxMarca():
        lista = []
        
        registros = Carros.objects.all()
        marca_maior = registros.values('marca_id').annotate(dcount=Count('marca_id')).order_by('-dcount').first()
        maior = Marca.objects.get(pk=marca_maior['marca_id'])

       
        return maior.descricao