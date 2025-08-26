cadastro = {}
print(type(cadastro))
print(cadastro)
### 1 - Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:
cadastro = {
    'Nome': 'Leo',
    'Idade': 37,
    'Nacionalidade': 'Brasileiro'
}
print(cadastro)
### 2 - Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", retornando "Não informado" se a chave não existir.

cliente = {"nome": "Amanda", "idade": 31}
cliente.get('telefone', 'não informado')
print (cliente.get('telefone', 'não informado'))

### 3 - Utilize um laço for para imprimir todas as chaves do dicionário abaixo.
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
for titulo in livro:
    print (titulo)

### 4 - Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
livro['disponível']=True
print (livro)

### 5 - Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
livro.pop('ano')
print (livro)
