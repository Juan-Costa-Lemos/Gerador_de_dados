
import random, os 

lista_nomes = ['Marcos','Lucas','Ana','Clara','Bento']
lista_email = ['jululioMataporco@gmail.com','xaolin07@gmail.com','anaalcool@gmail.com','naodouglas@gmail.com','rengoku@gmail.com']
lista_telefone = [7895-7456,7898-4561,4598-5732,1235-9875,8528-9639]
lista_cidades = ['Nova Iguaçu','Mesquita','Queimados','Paraiso','Barra']
lista_estados = ['Rio de Janeiro','São Paulo','Espirito Santo','Acre','Amazonas']

def salvar(valor):
    salvar = input('Gostaria de salvar os dados em um arquivo de texto? (s/n)?\n')
    if salvar =='s':
        with open('dados.txt','a') as arquivo:
                arquivo.write(str(valor)+ '\n')
    else:
        pass        
    
def gerar_nome():
    nome = random.choice(lista_nomes)
    salvar(nome)
    return print(f'{nome}')


def gerar_email():
    email = random.choice(lista_email)
    salvar(email)
    return print(f'{email}')

def gerar_telefone():
    telefone = random.choice(lista_telefone)
    salvar(telefone)
    return print(f'{telefone}')

def gerar_cidade():
    cidade = random.choice(lista_cidades)
    salvar(cidade)   
    return print(f'{cidade}')

def gerar_estado():
    estado = random.choice(lista_estados)
    salvar(estado)
    return print(f'{estado}')



print('-=-'*20)
print('Bem vindo ao Gerador de dados! Digite "parar" a qualquer para encerar o programa.')
print('-=-'*20)
print('Selecione uma ou mais opções para serem geradas aleatóriamente.')
print('[1] - Nome')
print('[2] - E-mail')
print('[3] - Telefone')
print('[4] - Cidade')
print('[5] - Estado')

while True:
    try:
        dado =[]
        dado = input('Digite uma ou mais opções:\n')
        if dado == '1':
            print('Você selecionou [1]')
            gerar_nome()
                
        elif dado == '2':
            print('Você selecionou [2]')
            gerar_email()

        elif dado == '3':
            print('Você selecionou [3]')
            gerar_telefone()

        elif dado == '4':
            print('Você selecionou [4]')
            gerar_cidade()

        elif dado == '5':
            print('Você selecionou [5]')
            gerar_estado()

        else:
            if dado == 'parar':
                print('O programa foi encerrado!')
                break
            elif dado >='6':
                print('Opção invalida!')                            
    except:
        pass