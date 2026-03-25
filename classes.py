class ItemEstoque:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento
        self.__quantidade = quantidade
        self.__proximo = None 

    def get_nome(self): return self.__nome
    def get_preco_venda(self): return self.__preco_venda
    def get_quantidade(self): return self.__quantidade
    def set_quantidade(self, qtd): self.__quantidade = qtd
    def get_proximo(self): return self.__proximo
    def set_proximo(self, prox): self.__proximo = prox

class Estoque:
    def __init__(self):
        self.__inicio = None

    def adicionar(self, novo_item):
        if self.__inicio is None:
            self.__inicio = novo_item
        else:
            atual = self.__inicio
            while atual.get_proximo() is not None:
                atual = atual.get_proximo()
            atual.set_proximo(novo_item)

    def vender(self, nome_procurado):
        atual = self.__inicio
        anterior = None
        while atual is not None:
            if atual.get_nome() == nome_procurado and atual.get_quantidade() > 0:
                nova_qtd = atual.get_quantidade() - 1
                atual.set_quantidade(nova_qtd)
                
                if atual.get_quantidade() == 0:
                    if anterior is None:
                        self.__inicio = atual.get_proximo()
                    else:
                        anterior.set_proximo(atual.get_proximo())
                return atual
            anterior = atual
            atual = atual.get_proximo()
        return None

class Pagamento:
    def __init__(self, pagador, categoria, curso, item, valor, data_hora):
        self.__pagador = pagador
        self.__categoria = categoria
        self.__curso = curso
        self.__item = item
        self.__valor = valor
        self.__data_hora = data_hora
        self.__proximo = None

    def get_pagador(self): return self.__pagador
    def get_item(self): return self.__item
    def get_valor(self): return self.__valor
    def get_data_hora(self): return self.__data_hora
    def get_proximo(self): return self.__proximo
    def set_proximo(self, prox): self.__proximo = prox

class HistoricoVendas:
    def __init__(self):
        self.__inicio = None

    def adicionar_pagamento(self, novo):
        if self.__inicio is None:
            self.__inicio = novo
        else:
            atual = self.__inicio
            while atual.get_proximo() is not None:
                atual = atual.get_proximo()
            atual.set_proximo(novo)

    def gerar_extrato(self):
        print("\n" + "-"*30)
        print("   EXTRATO FINANCEIRO")
        print("-"*30)
        atual = self.__inicio
        if atual is None:
            print("Nenhuma venda financeira registrada.")
            return
        total_caixa = 0
        while atual is not None:
            print("Item: {} | Valor: R$ {}".format(atual.get_item(), atual.get_valor()))
            total_caixa += atual.get_valor()
            atual = atual.get_proximo()
        print("TOTAL EM CAIXA: R$ {}".format(total_caixa))

    def relatorio_consumo(self):
        print("\n" + "-"*30)
        print("   RELATORIO DE CONSUMO")
        print("-"*30)
        atual = self.__inicio
        if atual is None:
            print("Nenhum consumo registrado.")
            return
        while atual is not None:
            print("Cliente: {} | Produto: {} | Hora: {}".format(
                atual.get_pagador(), atual.get_item(), atual.get_data_hora()
            ))
            atual = atual.get_proximo()

    def gerar_recomendacoes(self):
        print("\n" + "-"*30)
        print("   RECOMENDACOES GESTORA")
        print("-"*30)
        if self.__inicio is None:
            print("Sem dados para analise.")
            return

        contagem = {}
        atual = self.__inicio
        while atual is not None:
            nome_item = atual.get_item()
            contagem[nome_item] = contagem.get(nome_item, 0) + 1
            atual = atual.get_proximo()
        
        mais_vendido = max(contagem, key=contagem.get)
        print("Analise: O produto '{}' e o lider de vendas.".format(mais_vendido))
        print("Recomendacao: Garantir estoque extra de {} para evitar faltas.".format(mais_vendido))