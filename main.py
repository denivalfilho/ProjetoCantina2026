from classes import ItemEstoque, Estoque, Pagamento, HistoricoVendas
from faker import Faker
import random

fake = Faker('pt_BR')
cantina = Estoque()
historico = HistoricoVendas()

def gerar_dados_teste():
    produtos = ["Coxinha", "Suco", "Cafe"]
    for i in range(5):
        nome_sorteado = random.choice(produtos)
        # Cria o item e coloca no estoque
        item = ItemEstoque(nome_sorteado, 3.0, 5.0, "24/03", "30/03", 10)
        cantina.adicionar(item)
        
        # Realiza a venda usando o Faker para o nome do aluno
        venda = cantina.vender(nome_sorteado)
        if venda:
            pago = Pagamento(fake.name(), "Aluno", "ADS", venda.nome, venda.preco_venda, "24/03 10:00")
            historico.adicionar_pagamento(pago)
    print(">>> 5 Vendas geradas com sucesso!")

while True:
    print("\n--- MENU DA CANTINA ---")
    print("1. Cadastrar Produto (Manual)")
    print("2. Gerar Teste (Faker)")
    print("3. Ver Relatorio de Vendas")
    print("4. Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        qtd = int(input("Quantidade: "))
        novo = ItemEstoque(nome, 3.0, 5.0, "24/03", "30/03", qtd)
        cantina.adicionar(novo)
        print("Produto adicionado!")

    elif opcao == "2":
        gerar_dados_teste()

    elif opcao == "3":
        historico.relatorio_consumo()

    elif opcao == "4":
        print("Saindo...")
        break