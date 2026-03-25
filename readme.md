Sistema de Gestão - Cantina Fatec

Projeto de controle de estoque e vendas desenvolvido para as disciplinas de Estrutura de Dados e Linguagem de Programação 2.

O que o sistema faz

    Cadastro de Produtos: Adição manual de itens ao estoque.

    Vendas: Realiza a baixa no estoque e gera um registro de pagamento.

    Geração de Dados: Usa a biblioteca Faker para criar massa de testes automática.

    Persistência: Salva e carrega os dados em arquivo binário (.dat) usando Pickle.

    Relatórios: Extrato financeiro, relatório de consumo e recomendações de compra.

Tecnologias Aplicadas

    Linguagem: Python 3.

    Estrutura de Dados: Lista Encadeada Simples (implementada manualmente).

    POO: Uso de classes, atributos privados e métodos Getters/Setters.

Como rodar

    Instale a dependência necessária:
    Bash

    pip install faker

    Execute o arquivo principal:
    Bash

    python main.py