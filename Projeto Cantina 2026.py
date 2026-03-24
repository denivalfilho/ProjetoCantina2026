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
    def __init__(self, pagador, categoria, curso, item, valor, data_hora):
        self.pagador = pagador
        self.categoria = categoria
        self.curso = curso
        self.item = item
        self.valor = valor
        self.data_hora = data_hora
        self.proximo = None

class HistoricoVendas:
    def __init__(self):
        self.inicio = None

    def adicionar_pagamento(self, novo):
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def gerar_extrato(self, filtro=None):
        atual = self.inicio
        print("--- EXTRATO DE PAGAMENTOS ---")
        while atual is not None:
            if filtro is None or atual.categoria == filtro:
                print("Pagador:", atual.pagador, "| Item:", atual.item, "| Valor: R$", atual.valor)
            atual = atual.proximo

    def relatorio_consumo(self):
        atual = self.inicio
        print("--- RELATORIO DE CONSUMO ---")
        while atual is not None:
            print("O(a)", atual.pagador, "consumiu:", atual.item, "em:", atual.data_hora)
            atual = atual.proximo

# --- TESTES ---
cantina = Estoque()
historico = HistoricoVendas()

it1 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "18/03", 10)
cantina.adicionar(it1)

# Ao vender, pegamos o objeto e passamos os dados para o historico
venda = cantina.vender("Coxinha")
if venda:
    p1 = Pagamento("Maria", "Professor", "ESG", venda.nome, venda.preco_venda, "22/03 15:30")
    historico.adicionar_pagamento(p1)

historico.relatorio_consumo()