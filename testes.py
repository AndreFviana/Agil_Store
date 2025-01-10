from inventario import GerenciadorDeInventario

def main():
    inventario = GerenciadorDeInventario()

    inventario.adicionar_produto() 
    inventario.listar_produtos() 
    inventario.buscar_produto()

    print("\nProdutos no Inventario:")
    

if __name__ ==  "__main__":
    main()
    