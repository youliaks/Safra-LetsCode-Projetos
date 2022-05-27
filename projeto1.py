import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados:list):
    '''
    Função retorna uma lista contendo todos as categorias de uma lista dada.    
    '''
    categorias = []
    
    for elemento in dados:
        if elemento['categoria'] not in categorias:
            categorias.append(elemento['categoria'])
    
    categorias.sort()

    print('Os produtos estão agrupados nas seguintes categorias:')
    i=0
    while i < len(categorias):
        print(categorias[i])
        i += 1

def listar_por_categoria(dados:list, categoria:str):
    '''
    Função retorna uma lista contendo todos os produtos pertencentes à determinada categoria.
    '''
    categoria_lista = []
    
    for i in range(0,len(dados)):
        if dados[i]['categoria'] == categoria:
            categoria_lista.append(dados[i])
    
    # organizar em ordem crescente os número e após em ordem alfabética 
    categoria_lista.sort(key = lambda x: x['id'])
            
    print('Os produtos da categoria escolhida são: ')
    print('')
    for i in categoria_lista:
        print ('ID: ',i['id'])
        print ('Preço: ',i['preco'])
        print ('Categoria: ',i['categoria'])
        print ('- - - - - - - - - - - - - - - - - - - - - - - -')
    

def produto_mais_caro(dados:list, categoria:str):
    '''
    Função retorna uma lista com o produto mais caro de determinadas categoria.
    '''
    categoria_lista = []
    
    for i in range(0,len(dados)):
        if dados[i]['categoria'] == categoria:
            categoria_lista.append(dados[i])
    
    # organizar em ordem crescente os número e após em ordem alfabética 
    categoria_lista.sort(key = lambda x: float(x ['preco']), reverse=True)
    
    print('O produto mais caro da categoria escolhida é: ')
    print('')
    print ('ID: ',categoria_lista[0]['id'])
    print ('Preço: ',categoria_lista[0]['preco'])
    print ('Categoria: ',categoria_lista[0]['categoria'])


def produto_mais_barato(dados:list, categoria:str):
    '''
    Função retorna uma lista com o produto mais barato de determinadas categoria.
    '''
     categoria_lista = []
    
    for i in range(0,len(dados)):
        if dados[i]['categoria'] == categoria:
            categoria_lista.append(dados[i])
    
    categoria_lista.sort(key = lambda x: float(x ['preco']))

    print('O produto mais barato da categoria escolhida é: ')
    print('')
    print ('ID: ',categoria_lista[0]['id'])
    print ('Preço: ',categoria_lista[0]['preco'])
    print ('Categoria: ',categoria_lista[0]['categoria'])

def top_10_caros(dados:list):
    '''
    Função retorna uma lista de dicionários com os 10 produtos mais baratos caros.
    '''
    caros = sorted(dados, key = lambda x: float(x ['preco']), reverse=True)
    dez_caros = caros[:10]
    print('Os 10 produtos mais caros dessa lista são: ')
    print('')
    for i in dez_caros:
        print(dez_caros.index(i)+1,'º produto mais caro:')
        print ('ID: ',i['id'])
        print ('Preço: ',i['preco'])
        print ('Categoria: ',i['categoria'])
        print ('- - - - - - - - - - - - - - - - - - - - - - - -')

def top_10_baratos(dados):
    '''
    Função retorna uma lista de dicionários com os 10 produtos mais baratos.
    '''
    baratos = sorted(dados, key = lambda x: float(x ['preco']))
    dez_baratos = baratos[:10]
    print('Os 10 produtos mais caros dessa lista são: ')
    print('')
    for i in dez_baratos:
        print(dez_baratos.index(i)+1,'º produto mais barato:')
        print ('ID: ',i['id'])
        print ('Preço: ',i['preco'])
        print ('Categoria: ',i['categoria'])
        print ('- - - - - - - - - - - - - - - - - - - - - - - -')

def pede_confere_categoria(dados:list) -> str:
    '''
    Função para pedir e conferir se a categoria desejada está na lista 
    '''
    categorias = []
    for elemento in dados:
        if elemento['categoria'] not in categorias:
            categorias.append(elemento['categoria'])
    categoria = input('Qual categoria deseja listar os produtos? ')   
    while categoria not in categorias:
        categoria = input('Opção inválida! Qual categoria deseja listar os produtos? ')  
    return categoria

def menu(dados:list) -> None:
    '''
    Menu para chamar e retornar a função adequada para tratar o pedido do usuário.
    '''
    
    realizar_acao = 's'

    while realizar_acao.lower() == 's':
    
        opcoes = ['1','2','3','4','5','6','0']
      
        print ('1. Listar categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros \n6. Top 10 produtos mais baratos \n0. Sair\n')
    
        escolha_usuario = input('Qual informação deseja saber sobre a lista: ')
      
        while escolha_usuario not in opcoes:
            print('Opção inválida')
            escolha_usuario = input('Qual informação deseja saber sobre a lista: ')
   
        if escolha_usuario == '1':
            listar_categorias(dados)
            
        elif escolha_usuario == '2':
            categoria = pede_confere_categoria(dados)
            
            listar_por_categoria(dados, categoria)
            
        elif escolha_usuario == '3':
            categoria = pede_confere_categoria(dados)
            produto_mais_caro(dados, categoria) 
            
        elif escolha_usuario == '4':
            categoria = pede_confere_categoria(dados)
            
            produto_mais_barato(dados, categoria)   
            
        elif escolha_usuario == '5':
            top_10_caros(dados)    
            
        elif escolha_usuario == '6':
            top_10_baratos(dados)  
            
        elif escolha_usuario == '0':
            print('Até logo!')
            break
        
        realizar_acao = input('\nDeseja realizar outra ação? (S/N)\n')