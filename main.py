qtdProdutos = int(input("Quantos produtos deseja adicionar na lista?"))
listaCompras = []
for i in range(qtdProdutos):
  produto = input("Digite o nome do produto:")
  listaCompras.append(produto)
print("Os produtos da lista são:", listaCompras)