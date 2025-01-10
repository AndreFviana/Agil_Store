import random 
import string
import json
from tabulate import tabulate

class Produto:
    def __init__(self, nome, categoria, quantidade, preco):
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
    
    def converter_para_dicionario(self): 
        return {    'id': self.id, 
                    'nome': self.nome, 
                    'categoria': self.categoria, 
                    'quantidade': self.quantidade, 
                    'preco': self.preco }

class GerenciadorDeInventario:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self):
        nome = input("Nome do Produto: ")
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade em Estoque: "))
        preco = float(input("Preço: "))
        novo_produto = Produto(nome, categoria, quantidade, preco)
        self.produtos.append(novo_produto)
        print(f"Produto '{nome}' adicionado com sucesso! ID: {novo_produto.id}")

    def listar_produtos(self): 
        if not self.produtos: 
            print("Nenhum produto cadastrado no inventário.") 
        else:
            tabela = [] 
            for produto in self.produtos: 
                tabela.append([produto.id, produto.nome, produto.categoria, produto.quantidade, produto.preco]) 
            cabecalho = ["ID", "Nome do Produto", "Categoria", "Quantidade em Estoque", "Preço"] 
            print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))

    def atualizar_produto(self): 
        produto_id = input("Digite o ID do produto que deseja atualizar: ") 
        produto = next((p for p in self.produtos if p.id == produto_id), None) 
        if produto is None: 
            print("Produto não encontrado.") 
            return 
        print("Digite os novos dados do produto (deixe em branco para não alterar):") 
        novo_nome = input(f"Nome do Produto ({produto.nome}): ").strip() 
        atualizar_nova_categoria = input(f"Categoria ({produto.categoria}): ").strip() 
        atualizar_nova_quantidade = input(f"Quantidade em Estoque ({produto.quantidade}): ").strip() 
        novo_preco = input(f"Preço ({produto.preco}): ").strip()
        if novo_nome: 
            produto.nome = novo_nome 
        if atualizar_nova_categoria: 
            produto.categoria = atualizar_nova_categoria 
        if atualizar_nova_quantidade: 
            produto.quantidade = int(atualizar_nova_quantidade) 
        if novo_preco: 
            produto.preco = float(novo_preco) 
        print(f"Produto '{produto.nome}' atualizado com sucesso!")

    def remover_produto(self): 
        produto_id = input("Digite o ID do produto que deseja remover: ") 
        produto = next((p for p in self.produtos if p.id == produto_id), None) 
        if produto is None: 
            print("Produto não encontrado.") 
            return 
        confirmacao = input(f"Tem certeza que deseja remover o produto '{produto.nome}'? (s/n): ") 
        if confirmacao.lower() == 's': 
            self.produtos.remove(produto) 
            print(f"Produto '{produto.nome}' removido com sucesso!") 
        else: print("Remoção cancelada.")
    
    def buscar_produto(self): 
        criterio = input("Buscar por ID: ").strip().lower() 
        if criterio == 'id': 
            produto_id = input("Digite o ID do produto: ").strip() 
            produto = next((p for p in self.produtos if p.id == produto_id), None) 
            if produto is None: print("Produto não encontrado.") 
            else: self.exibir_detalhes_produto(produto) 
        elif criterio == 'nome': 
            parte_nome = input("Digite parte do nome do produto: ").strip().lower()
            produtos_encontrados = [p for p in self.produtos if parte_nome in p.nome.lower()] 
            if not produtos_encontrados: 
                print("Nenhum produto encontrado com esse nome.") 
            else: 
                for produto in produtos_encontrados: 
                    self.exibir_detalhes_produto(produto) 
        else: 
            print("Critério de busca inválido. Tente buscar pelo ID")
    
    def exibir_detalhes_produto(self, produto): 
        print(f"\nDetalhes do Produto (ID: {produto.id}):") 
        print(f"Nome: {produto.nome}") 
        print(f"Categoria: {produto.categoria}") 
        print(f"Quantidade em Estoque: {produto.quantidade}") 
        print(f"Preço: {produto.preco}\n")

    def salvar_dados(self): 
        with open('inventario.json', 'w') as f: json.dump([produto.converter_para_dicionario() for produto in self.produtos], f, indent=4) 
        print("Dados salvos com sucesso!") 
        
    def carregar_dados(self): 
        try: 
            with open('inventario.json', 'r') as f: 
                produtos = json.load(f) 
                self.produtos = [Produto(**produto) for produto in produtos] 
            print("Dados carregados com sucesso!") 
        except FileNotFoundError: print("Nenhum arquivo de dados encontrado. Iniciando com inventário vazio.")

inventario = GerenciadorDeInventario() 
inventario.adicionar_produto() 
inventario.listar_produtos() 
inventario.atualizar_produto() 
inventario.listar_produtos() 
inventario.remover_produto() 
inventario.listar_produtos() 
inventario.buscar_produto()