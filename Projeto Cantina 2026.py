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

    def vender(self):
        if self.inicio is None:
            print("Erro: Estoque vazio")
            return None
        else:
            item_vendido = self.inicio
            self.inicio = self.inicio.proximo
            return item_vendido

cantina = Estoque()

item1 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "18/03", 20)
item2 = ItemEstoque("Suco", 2.00, 4.50, "15/03", "20/03", 15)
item3 = ItemEstoque("Chocolate", 1.50, 3.00, "15/03", "15/12", 50)

cantina.adicionar(item1)
cantina.adicionar(item2)
cantina.adicionar(item3)

print("Teste de Venda")
print("Primeiro antes da venda:", cantina.inicio.nome)

venda = cantina.vender()

print("Item que saiu:", venda.nome)
print("Novo primeiro item:", cantina.inicio.nome)