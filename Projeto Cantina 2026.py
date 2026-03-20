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
        while atual is not None:
            if atual.nome == nome_procurado:
                if atual.quantidade > 0:
                    atual.quantidade = atual.quantidade - 1
                    return atual
                else:
                    print("Erro: Produto", nome_procurado, "esta esgotado!")
                    return None
            atual = atual.proximo
        return None

    def editar_quantidade(self, nome_procurado, nova_qtd):
        atual = self.inicio
        while atual is not None:
            if atual.nome == nome_procurado:
                atual.quantidade = nova_qtd
                return atual
            atual = atual.proximo
        print("Erro: Produto nao encontrado para editar")
        return None

cantina = Estoque()

item1 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "18/03", 20)
item2 = ItemEstoque("Suco", 2.00, 4.50, "15/03", "20/03", 15)
item3 = ItemEstoque("Chocolate", 1.50, 3.00, "15/03", "15/12", 50)

cantina.adicionar(item1)
cantina.adicionar(item2)
cantina.adicionar(item3)

print("Quantidade de Coxinha antes:", item1.quantidade)

cantina.vender("Coxinha")
print("Quantidade apos vender uma unidade:", item1.quantidade)

cantina.editar_quantidade("Coxinha", 100)
print("Quantidade apos editar para 100:", item1.quantidade)