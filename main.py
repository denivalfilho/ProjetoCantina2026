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
    print("Populando sistema automaticamente...")
    produtos_teste = ["Coxinha", "Suco Laranja", "Cafe Expresso", "Bolo Cenoura"]
    for nome in produtos_teste:
        item = ItemEstoque(nome, 3.50, 7.00, "20/03", "30/03", 10)
        cantina.adicionar(item)
    
    for _ in range(3):
        venda = cantina.vender(random.choice(produtos_teste))
        if venda:
            p = Pagamento(fake.name(), "Aluno", random.choice(["IA", "ESG"]), 
                          venda.get_nome(), venda.get_preco_venda(), "10:30")
            historico.adicionar_pagamento(p)
    print("Estoque e Vendas gerados com Faker!")

while True:
    print("\n--- SISTEMA GESTOR CANTINA (FATEC) ---")
    print("1. Cadastrar Produto (Manual Completo)")
    print("2. Ver Itens no Estoque")
    print("3. Editar Quantidade (Ajuste)")
    print("4. Realizar Venda (Cliente via Faker)")
    print("5. Relatorio Financeiro (Caixa)")
    print("6. Relatorio de Consumo (Clientes)")
    print("7. Popular Sistema (Faker - Automatico)")
    print("8. Sair e Salvar (Pickle)")
    
    op = input("Escolha uma opcao: ")

    if op == "1":
        print("\n-- NOVO CADASTRO --")
        n = input("Nome do Produto: ")
        pc = float(input("Preco de Compra: "))
        pv = float(input("Preco de Venda: "))
        dc = input("Data Compra (dd/mm): ")
        dv = input("Data Vencimento (dd/mm): ")
        q = int(input("Quantidade: "))
        item = ItemEstoque(n, pc, pv, dc, dv, q)
        cantina.adicionar(item)
        print("Produto adicionado ao estoque!")

    elif op == "2":
        cantina.relatorio_estoque()

    elif op == "3":
        n = input("Nome do produto para editar: ")
        q = int(input("Nova quantidade total: "))
        if cantina.editar_quantidade_manual(n, q):
            print("Estoque atualizado!")
        else:
            print("Produto nao encontrado.")

    elif op == "4":
        n = input("Nome do produto vendido: ")
        v = cantina.vender(n)
        if v:
            p = Pagamento(fake.name(), "Aluno", "IA", v.get_nome(), v.get_preco_venda(), "16:00")
            historico.add_pagamento(p) if hasattr(historico, 'add_pagamento') else historico.adicionar_pagamento(p)
            print("Venda concluida para cliente aleatorio!")
        else:
            print("Erro: Produto sem estoque ou inexistente.")

    elif op == "5":
        historico.gerar_extrato()

    elif op == "6":
        historico.relatorio_consumo()

    elif op == "7":
        gerar_dados_teste()

    elif op == "8":
        salvar_dados(cantina, historico)
        print("Saindo... Dados persistidos no arquivo via Pickle.")
        break
    else:
        print("Opcao invalida!")