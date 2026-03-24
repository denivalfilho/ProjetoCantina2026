from classes import ItemEstoque, Estoque, Pagamento, HistoricoVendas

# Criando os objetos das listas
cantina = Estoque()
historico = HistoricoVendas()

while True:
    print("\n========== MENU CANTINA FATEC ==========")
    print("1. Cadastrar Produto no Estoque")
    print("2. Realizar Venda")
    print("3. Ver Extrato de Pagamentos")
    print("4. Ver Relatorio de Consumo")
    print("5. Sair")
    
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        p_compra = float(input("Preco de compra: "))
        p_venda = float(input("Preco de venda: "))
        d_compra = input("Data de compra: ")
        d_venc = input("Data de vencimento: ")
        qtd = int(input("Quantidade: "))
        
        novo = ItemEstoque(nome, p_compra, p_venda, d_compra, d_venc, qtd)
        cantina.adicionar(novo)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        prod = input("Qual produto deseja vender? ")
        resultado = cantina.vender(prod)
        
        if resultado:
            cliente = input("Nome do cliente: ")
            cat = input("Categoria (Aluno/Professor/Servidor): ")
            curso = input("Curso (IA/ESG): ")
            data = input("Data/Hora atual: ")
            
            pago = Pagamento(cliente, cat, curso, resultado.nome, resultado.preco_venda, data)
            historico.adicionar_pagamento(pago)
            print(f"Venda de {resultado.nome} realizada!")
        else:
            print("Produto nao encontrado ou estoque vazio.")

    elif opcao == "3":
        filtro = input("Filtrar por categoria (Enter para todos): ")
        if filtro == "":
            historico.gerar_extrato()
        else:
            historico.gerar_extrato(filtro)

    elif opcao == "4":
        historico.relatorio_consumo()

    elif opcao == "5":
        print("Encerrando o sistema...")
        break
    else:
        print("Opcao invalida!")