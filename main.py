from classes import ItemEstoque, Estoque, Pagamento, HistoricoVendas
from faker import Faker
import random
import pickle
import os

# --- CONFIGURACOES INICIAIS ---
fake = Faker('pt_BR')

def salvar_dados(estoque, historico):
    try:
        with open('dados_cantina.dat', 'wb') as f:
            pickle.dump((estoque, historico), f)
    except Exception as e:
        print("Erro ao salvar dados: {}".format(e))

def carregar_dados():
    if os.path.exists('dados_cantina.dat'):
        try:
            with open('dados_cantina.dat', 'rb') as f:
                return pickle.load(f)
        except:
            return Estoque(), HistoricoVendas()
    return Estoque(), HistoricoVendas()

# Inicializa o sistema carregando dados salvos (Persistencia)
cantina, historico = carregar_dados()

def gerar_dados_teste():
    produtos_teste = ["Coxinha", "Suco", "Pao de Queijo", "Cafe"]
    print("\n>>> Gerando 5 vendas automaticas com Faker...")
    
    for i in range(5):
        nome_prod = random.choice(produtos_teste)
        
        # Cria item e adiciona ao estoque
        # ItemEstoque(nome, preco_compra, preco_venda, data_c, data_v, qtd)
        novo_item = ItemEstoque(nome_prod, 2.50, 5.00, "24/03", "30/03", 10)
        cantina.adicionar(novo_item)
        
        # Realiza a venda (diminui estoque e retorna o objeto item)
        venda = cantina.vender(nome_prod)
        
        if venda:
            nome_aluno = fake.name()
            # Criando o registro de pagamento usando os Getters (Encapsulamento)
            pago = Pagamento(
                nome_aluno, 
                "Aluno", 
                "ADS", 
                venda.get_nome(), 
                venda.get_preco_venda(), 
                "24/03 10:30"
            )
            historico.adicionar_pagamento(pago)
            print("Venda registrada para: {}".format(nome_aluno))
    
    # Salva logo apos gerar para garantir a nao volatilidade
    salvar_dados(cantina, historico)

# --- MENU PRINCIPAL ---
while True:
    print("\n" + "="*40)
    print("      SISTEMA GESTOR - CANTINA FATEC")
    print("="*40)
    print(" 1. Cadastrar Produto no Estoque (Manual)")
    print(" 2. Gerar Dados de Teste (Faker + Vendas)")
    print(" 3. Relatorio de Vendas (Financeiro)")
    print(" 4. Relatorio de Consumo (Por Cliente)")
    print(" 5. Recomendacoes da Gestao (Analise)")
    print(" 6. Sair e Salvar Dados (Pickle)")
    print("="*40)
    
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("\n--- Cadastro Manual ---")
        nome = input("Nome do Produto: ")
        qtd = int(input("Quantidade inicial: "))
        # Adiciona na lista encadeada de estoque
        item = ItemEstoque(nome, 3.0, 6.0, "24/03", "30/03", qtd)
        cantina.adicionar(item)
        salvar_dados(cantina, historico)
        print("Sucesso: {} adicionado ao estoque!".format(nome))

    elif opcao == "2":
        gerar_dados_teste()

    elif opcao == "3":
        historico.gerar_extrato()

    elif opcao == "4":
        historico.relatorio_consumo()

    elif opcao == "5":
        historico.gerar_recomendacoes()

    elif opcao == "6":
        salvar_dados(cantina, historico)
        print("Dados salvos em 'dados_cantina.dat'. Ate logo!")
        break
    
    else:
        print("Opcao invalida! Tente novamente.")