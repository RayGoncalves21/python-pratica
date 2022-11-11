"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Seu nome: ')
idade = input('Sua idade: ')


nome_invertido = nome[::-1]

print('-'*20)

if idade and nome is not None:
    print(f'Seu nome é {nome}\nSeu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Tem espaço')
    else:
        print('Não tem espaços')
    print(f'seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')
