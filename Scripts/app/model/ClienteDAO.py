from app.model.Cliente import Cliente

class ClienteDAO:

    # Lista os grupos de usuarios
    def listarClientes():
        lista = []
        dados = Cliente.objects.all()

        for dado in dados:
            linha = {}
            linha['id'] = dado.pk
            linha['nome'] = dado.nome
            linha['endereco'] = dado.endereco
            linha['idade'] = dado.idade
            linha['ativo'] = dado.ativo
            lista.append(linha) # só exibe o ultimo
        return lista