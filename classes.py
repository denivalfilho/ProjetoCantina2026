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

    def editar_quantidade_manual(self, nome, nova_qtd):
        atual = self.__inicio
        while atual is not None:
            if atual.get_nome() == nome:
                atual.set_quantidade(nova_qtd)
                return True
            atual = atual.get_proximo()
        return False

    def vender(self, nome):
        atual = self.__inicio
        anterior = None
        while atual is not None:
            if atual.get_nome() == nome and atual.get_quantidade() > 0:
                atual.set_quantidade(atual.get_quantidade() - 1)
                if atual.get_quantidade() == 0:
                    if anterior is None:
                        self.__inicio = atual.get_proximo()
                    else:
                        anterior.set_proximo(atual.get_proximo())
                return atual
            anterior = atual
            atual = atual.get_proximo()
        return None

    def relatorio_estoque(self):
        print("LISTA DE ESTOQUE:")
        atual = self.__inicio
        while atual is not None:
            print("Item:", atual.get_nome(), "| Qtd:", atual.get_quantidade())
            atual = atual.get_proximo()

class Pagamento:
    def __init__(self, pagador, categoria, curso, item, valor, data_hora):
        self.__pagador = pagador
        self.__categoria = categoria
        self.__curso = curso
        self.__item = item
        self.__valor = valor
        self.__data_hora = data_hora
        self.__proximo = None

    def get_item(self): return self.__item
    def get_valor(self): return self.__valor
    def get_pagador(self): return self.__pagador
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
        print("VENDAS REALIZADAS:")
        total = 0
        atual = self.__inicio
        while atual is not None:
            print("Produto:", atual.get_item(), "| Valor:", atual.get_valor())
            total += atual.get_valor()
            atual = atual.get_proximo()
        print("TOTAL EM CAIXA:", total)

    def relatorio_consumo(self):
        print("QUEM CONSUMIU:")
        atual = self.__inicio
        while atual is not None:
            print("Cliente:", atual.get_pagador(), "| Item:", atual.get_item())
            atual = atual.get_proximo()