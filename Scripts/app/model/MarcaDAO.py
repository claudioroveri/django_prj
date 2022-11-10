from app.model.Carros import Carros
from app.model.Marca import Marca
from django.db.models import Count

class MarcaDAO:

    # Lista os carros de forma personalizada
    def listarMarcas():
        lista = []
        dados = Marca.objects.all()

        for dado in dados:
            linha = {}
            linha['id'] = dado.id
            linha['descricao'] = dado.descricao
            linha['origem'] = dado.origem
            linha['luxo'] = "Sim" if dado.luxo == True else "Não" #ternario
            lista.append(linha) # só exibe o ultimo
        return lista