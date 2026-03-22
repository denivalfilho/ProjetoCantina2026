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

    def editar_quantidade(self, nome_procurado, nova_qtd):
        atual = self.inicio
        while atual is not None:
            if atual.nome == nome_procurado:
                atual.quantidade = nova_qtd
                return atual
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

cantina = Estoque()
historico = HistoricoVendas()

lote1 = ItemEstoque("Coxinha", 3.50, 6.00, "10/03", "12/03", 1)
item2 = ItemEstoque("Suco", 2.00, 4.50, "15/03", "20/03", 15)
cantina.adicionar(lote1)
cantina.adicionar(item2)

print("--- Realizando Venda ---")
item_vendido = cantina.vender("Coxinha")

if item_vendido:
    novo_pago = Pagamento("Jose", "Aluno", "IA", item_vendido.preco_venda, "22/03 15:00")
    historico.registrar_pagamento(novo_pago)
    print("Venda registrada para:", historico.inicio.pagador)
    print("Valor pago: R$", historico.inicio.valor)

print("Quantidade de Coxinha no estoque apos venda:", lote1.quantidade)