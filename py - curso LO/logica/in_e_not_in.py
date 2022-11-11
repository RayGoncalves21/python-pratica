# in & not in

# in -> estar entre |  not in -> não está dentro


nome = 'Rayzinho'

print(nome[2])
print(nome[-6])

print('a' in nome)


if 'z' in nome:
    print('tem z no nome.')

if 'z' not in nome:
    print('Não tem Z no nome')


nome_entrada = input('Digite seu nome: ')

if 'a' in nome_entrada:
    print('tem "a" em seu nome')

else:
    print('Não tem "a" no seu nome, taokey?')

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar not in nome2:
    print(f'{encontrar} não está em {nome2}')
else:
    print(f'{encontrar} está em {nome2}')
