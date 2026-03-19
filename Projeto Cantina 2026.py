class ItemEstoque:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade
        self.proximo = None 

item1 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "18/03", 20)
item2 = ItemEstoque("Suco", 2.00, 4.50, "15/03", "20/03", 15)
item3 = ItemEstoque("Chocolate", 1.50, 3.00, "15/03", "15/12", 50)

item1.proximo = item2 
item2.proximo = item3

print("Teste")
print(item1.nome)
print(item1.proximo)
print(item1.proximo.nome)
print(item2.nome)
print(item1.proximo.proximo.nome)
print(item3.proximo)