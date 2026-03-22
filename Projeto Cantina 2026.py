class ItemEstoque:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade
        self.proximo = None 

class Estoque:
    def __init__(self):
        self.inicio = None

    def adicionar(self, novo_item):
        if self.inicio is None:
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item

    def vender(self, nome_procurado):
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.nome == nome_procurado and atual.quantidade > 0:
                atual.quantidade -= 1
                if atual.quantidade == 0:
                    if anterior is None:
                        self.inicio = atual.proximo
                    else:
                        anterior.proximo = atual.proximo
                return atual
            anterior = atual
            atual = atual.proximo
        return None

class Pagamento:
    def __init__(self, pagador, categoria, curso, valor, data_hora):
        self.pagador = pagador
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora
        self.proximo = None

class HistoricoVendas:
    def __init__(self):
        self.inicio = None

    def registrar_pagamento(self, novo_pagamento):
        if self.inicio is None:
            self.inicio = novo_pagamento
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_pagamento

    def gerar_extrato(self, filtro_categoria=None):
        atual = self.inicio
        print("--- EXTRATO DE PAGAMENTOS ---")
        while atual is not None:
            if filtro_categoria is None or atual.categoria == filtro_categoria:
                print(f"Pagador: {atual.pagador} | Cat: {atual.categoria} | Curso: {atual.curso} | Valor: R$ {atual.valor}")
            atual = atual.proximo

cantina = Estoque()
historico = HistoricoVendas()

item1 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "18/03", 10)
cantina.adicionar(item1)

venda = cantina.vender("Coxinha")
if venda:
    p1 = Pagamento("Maria", "Professor", "ESG", venda.preco_venda, "22/03 15:30")
    historico.registrar_pagamento(p1)

historico.gerar_extrato()