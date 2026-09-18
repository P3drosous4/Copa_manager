import unicodedata

def obter_inteiro(msg=''):
    while True:
        try:
            num=int(input(msg))
            break
        except ValueError:
            print('digite um número adequado !')
    return num


def obter_string(msg=''):
    while True:
        palavra = input(msg)
        palavra = palavra.strip()
        if palavra != '':
            return palavra
        print('Digite um valor válido!')


def limpar_tela(msg=''):
    import os
    input(msg)
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def validacao():
    while True:
        resposta=obter_string('deseja continuar ? (S/N)').upper().split()[0]

        if resposta=="N":
            return True
        elif resposta=="S":
            return False
        else:
            print('resposta inadequada !')
            continue
        

def limpar_tela_automatico():
    import os
  
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def valorboll(msg=''):
    while True:
        try:
            resposta=input(msg).lower().strip()[0]
            if resposta=="s":
                return True
                
            elif resposta=='n':
                return False
            else:
                print('digite uma opção adequada !')
        except ValueError:
            print('digite uma a palavra coorreta !')


def filter_manual(lista, funcao):
    resultado = []
    for item in lista:
        if funcao(item):
            resultado.append(item)
    return resultado

def reduce_manual(lista, funcao, valor_inicial):
    acumulador = valor_inicial
    for item in lista:
        acumulador = funcao(acumulador, item)
    return acumulador

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = "".join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acentos


def mensagem_salvamento():
    print(" Dados salvos com sucesso!")
    limpar_tela('Pressione ENTER para continuar...')