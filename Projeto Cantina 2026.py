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
            if atual.nome == nome_procurado:
                if atual.quantidade > 0:
                    atual.quantidade -= 1
                    
                    if atual.quantidade == 0:
                        if anterior is None:
                            self.inicio = atual.proximo
                        else:
                            anterior.proximo = atual.proximo
                            
                    return atual
            
            anterior = atual
            atual = atual.proximo
            
        print("Erro: Produto", nome_procurado, "nao encontrado ou esgotado")
        return None

    def editar_quantidade(self, nome_procurado, nova_qtd):
        atual = self.inicio
        while atual is not None:
            if atual.nome == nome_procurado:
                atual.quantidade = nova_qtd
                return atual
            atual = atual.proximo
        return None

cantina = Estoque()

lote1 = ItemEstoque("Coxinha", 3.50, 6.00, "10/03", "12/03", 1)
lote2 = ItemEstoque("Coxinha", 3.50, 6.00, "15/03", "20/03", 10)
item2 = ItemEstoque("Suco", 2.00, 4.50, "15/03", "20/03", 15)

cantina.adicionar(lote1)
cantina.adicionar(lote2)
cantina.adicionar(item2)

print("Venda 1 (Lote 1):")
v1 = cantina.vender("Coxinha")
print("Vendido:", v1.nome, "| Validade:", v1.data_vencimento)

print("Venda 2 (Lote 2 - o sistema pulou o lote 1 que zerou):")
v2 = cantina.vender("Coxinha")
print("Vendido:", v2.nome, "| Validade:", v2.data_vencimento)

print("Primeiro da lista agora:", cantina.inicio.nome)