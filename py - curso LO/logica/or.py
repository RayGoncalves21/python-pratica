# uma ou outras expressao que tem ser verdadeira, se um valor for verdadeiro a expressao será avaliada naquele valor


# avaliação de curo circuito

entrada = input('[E]ntrar [S]air: ')

login_bd = 'ray'
senha_bd = '123'

if entrada == 'E' or entrada == 'e':
    login = input('Login: ')
    senha = input('senha: ')

    if login == login_bd and senha == senha_bd:
        print('Entrada autorizada')
        print(f'Saldo de {login}: R$ 100.453,29')
    else:
        print('Login ou senha inválidas')

else:
    print('O usuario saiu do sistema')
