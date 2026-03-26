from classes import ItemEstoque, Estoque, Pagamento, HistoricoVendas
from faker import Faker
import random
import pickle
import os

fake = Faker('pt_BR')

def salvar_dados(est, hist):
    with open('dados.dat', 'wb') as f:
        pickle.dump((est, hist), f)

def carregar_dados():
    if os.path.exists('dados.dat'):
        try:
            with open('dados.dat', 'rb') as f:
                return pickle.load(f)
        except:
            return Estoque(), HistoricoVendas()
    return Estoque(), HistoricoVendas()

cantina, historico = carregar_dados()

def gerar_dados_teste():
    produtos_teste = ["Coxinha", "Suco", "Cafe", "Bolo"]
    for nome in produtos_teste:
        item = ItemEstoque(nome, 3.50, 7.00, "20/03", "30/03", 10)
        cantina.adicionar(item)
    
    for _ in range(3):
        venda = cantina.vender(random.choice(produtos_teste))
        if venda:
            p = Pagamento(fake.name(), "Aluno", random.choice(["IA", "ESG"]), 
                          venda.get_nome(), venda.get_preco_venda(), "10:30")
            historico.adicionar_pagamento(p)

while True:
    print("\n--- SISTEMA GESTOR CANTINA (FATEC) ---")
    print("1. Cadastrar Produto")
    print("2. Ver Itens no Estoque")
    print("3. Editar Quantidade")
    print("4. Realizar Venda")
    print("5. Relatorio Financeiro")
    print("6. Relatorio de Consumo")
    print("7. Popular Sistema")
    print("8. Sair e Salvar")
    
    op = input("Escolha uma opcao: ")

    if op == "1":
        n = input("Nome: ")
        pc = float(input("Preco Compra: "))
        pv = float(input("Preco Venda: "))
        dc = input("Data Compra: ")
        dv = input("Data Vencimento: ")
        q = int(input("Quantidade: "))
        item = ItemEstoque(n, pc, pv, dc, dv, q)
        cantina.adicionar(item)

    elif op == "2":
        cantina.relatorio_estoque()

    elif op == "3":
        n = input("Produto: ")
        q = int(input("Nova Qtd: "))
        cantina.editar_quantidade_manual(n, q)

    elif op == "4":
        n = input("Produto vendido: ")
        v = cantina.vender(n)
        if v:
            p = Pagamento(fake.name(), "Aluno", "IA", v.get_nome(), v.get_preco_venda(), "16:00")
            historico.adicionar_pagamento(p)
            print(f"Vendido para: {p.get_pagador()}")

    elif op == "5":
        historico.gerar_extrato()

    elif op == "6":
        historico.relatorio_consumo()

    elif op == "7":
        gerar_dados_teste()

    elif op == "8":
        salvar_dados(cantina, historico)
        break