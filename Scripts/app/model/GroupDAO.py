from django.contrib.auth.models import Group

class GroupDAO:

    # Lista os grupos de usuarios
    def listarGrupos():
        lista = []
        dados = Group.objects.all()

        for dado in dados:
            linha = {}
            linha['id'] = dado.pk
            linha['name'] = dado.name
            lista.append(linha) # só exibe o ultimo
        return lista