from classes import ItemEstoque, Estoque, Pagamento, HistoricoVendas
from faker import Faker
import random

# --- CONFIGURAÇÕES INICIAIS ---
# Inicializa o Faker para gerar nomes brasileiros
fake = Faker('pt_BR')

# Instancia as classes da nossa estrutura de dados
cantina = Estoque()
historico = HistoricoVendas()

# --- FUNÇÃO PARA O FAKER (DADOS DE TESTE) ---
def gerar_dados_teste():
    produtos_teste = ["Coxinha", "Suco", "Pao de Queijo", "Cafe"]
    
    print("\n>>> Gerando 5 vendas automaticas com nomes aleatorios...")
    
    for i in range(5):
        nome_prod = random.choice(produtos_teste)
        
        # 1. Adiciona um item ao estoque (Preço fixo para o teste)
        novo_item = ItemEstoque(nome_prod, 2.50, 5.00, "24/03", "30/03", 10)
        cantina.adicionar(novo_item)
        
        # 2. Tenta realizar a venda
        venda = cantina.vender(nome_prod)
        
        if venda:
            # Aqui entra o Faker criando o nome do Aluno
            nome_aluno = fake.name()
            
            pago = Pagamento(
                nome_aluno, 
                "Aluno", 
                "ADS", 
                venda.nome, 
                venda.preco_venda, 
                "24/03 10:30"
            )
            historico.adicionar_pagamento(pago)
            print(f"Venda registrada para: {nome_aluno}")

# --- MENU PRINCIPAL ---
while True:
    print("\n" + "="*30)
    print("      SISTEMA CANTINA FATEC")
    print("="*30)
    print("1. Cadastrar Produto (Manual)")
    print("2. Gerar 5 Vendas (Faker - Automatico)")
    print("3. Ver Relatorio de Vendas")
    print("4. Sair")
    print("="*30)
    
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("\n--- Cadastro Manual ---")
        nome = input("Nome do Produto: ")
        qtd = int(input("Quantidade inicial: "))
        
        # Cria e adiciona na lista encadeada de estoque
        item = ItemEstoque(nome, 3.0, 6.0, "24/03", "30/03", qtd)
        cantina.adicionar(item)
        print(f"Sucesso: {nome} adicionado ao estoque!")

    elif opcao == "2":
        # Chama a função que usa a biblioteca Faker
        gerar_dados_teste()

    elif opcao == "3":
        print("\n--- Relatorio de Consumo ---")
        historico.relatorio_consumo()

    elif opcao == "4":
        print("Saindo do sistema... Ate logo!")
        break
    
    else:
        print("Opcao invalida! Tente novamente.")