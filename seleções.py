import ultils
import persistência
from tabulate import tabulate


def criar_listas_dicionarios(lista):
    while True:
        
        id=obter_id(lista)
        nome = ultils.obter_string('Seleção: ').capitalize().strip()
        confederacao = ultils.obter_string('Confederação: ').upper().strip()
        grupo = ultils.obter_string('Grupo: ').upper()
        rank = ultils.obter_inteiro('Ranking FIFA: ')
        titulos = ultils.obter_inteiro('Títulos: ')

        dicionario = {
            'id': id,
            'seleção': nome,
            'confederação': confederacao,
            'grupo': grupo,
            'ranking': rank,
            'títulos': titulos
        }
        lista.append(dicionario)
        print(f"Seleção '{nome}' cadastrada com sucesso!")

        if ultils.validacao():
            break
    return lista


def obter_id(lista):
        if len(lista) == 0:
            id = 1
        else:
            maior_id = 0
            for selecao in lista:
                if selecao['id'] > maior_id:
                    maior_id = selecao['id']
            id = maior_id + 1
        
        return id



def cadastrar_selecao(lista):
    ultils.limpar_tela_automatico()
    criar_listas_dicionarios(lista)
    persistência.salvar_selecoes('seleções.txt', lista)
    ultils.limpar_tela('Digite ENTER para voltar ao menu...')
    return lista



def obter_selecao_para_ordenacao(selecao):
    return selecao['seleção']


def obter_ranking_para_ordenacao(selecao):
    return selecao['ranking']


def obter_titulos_para_ordenacao(selecao):
    return selecao['títulos']


def ordenar_selecoes(lista):
    if len(lista) == 0:
        print("Lista vazia!")
        return lista
    
    msg = 'Como quer ordenar? (seleção, ranking, títulos, não ordenar): '
    opcao = ultils.obter_string(msg).lower().strip()
    
    if opcao in ['não', 'nao', 'não ordenar', 'nao ordenar']:
        return lista
    
    escolha = ultils.valorboll('Ordem inversa? (S/N): ')
    
    if opcao == 'seleção' or opcao == 'selecao':
        return sorted(lista, key=obter_selecao_para_ordenacao, reverse=escolha)
    elif opcao == 'ranking':
        return sorted(lista, key=obter_ranking_para_ordenacao, reverse=escolha)
    elif opcao == 'títulos' or opcao == 'titulos':
        return sorted(lista, key=obter_titulos_para_ordenacao, reverse=escolha)
    else:
        print('Opção inválida! Mantendo ordem original.')
        return lista


def criar_tabela_selecao(lista):
    linhas_tabelas = []
    cabecalho = ['id', 'seleção', 'Confederação', 'Ranking na FIFA', 'Títulos', 'Grupo']
    for resultado in lista:
        lista_resultado = [
            resultado['id'],
            resultado['seleção'],
            resultado['confederação'],
            resultado['ranking'],
            resultado['títulos'],
            resultado['grupo']
        ]
        linhas_tabelas.append(lista_resultado)
    
    tabela = tabulate(linhas_tabelas, headers=cabecalho, tablefmt='fancy_grid')
    print(tabela)


def listar_ord_selecoes(lista):
    ultils.limpar_tela_automatico()
    lista_ordenada = ordenar_selecoes(lista)
    print('-'*70)
    print(f"{'Seleções da copa':>35}")
    criar_tabela_selecao(lista_ordenada)
    ultils.limpar_tela('Digite ENTER para voltar ao menu...')


def buscar_selecao(lista_selecao):
    ultils.limpar_tela_automatico()
    selecao = ultils.obter_string('Digite o nome da seleção: ').lower().strip()
    texto_resposta = ultils.remover_acentos(selecao)
    lista_escolhidos = []
    
    if len(selecao) > 0:
        for i in range(len(lista_selecao)):
            original = lista_selecao[i]['seleção'].lower()
            comparacao = ultils.remover_acentos(original)
            if texto_resposta in comparacao:
                lista_escolhidos.append(lista_selecao[i])
        
        print(f'Resultados possíveis para "{selecao}":')
        criar_tabela_selecao(lista_escolhidos)
    else:
        print('Nenhuma seleção foi cadastrada!')
    
    ultils.limpar_tela('Digite ENTER para voltar ao menu')


def filtrar_selecao(lista):
    ultils.limpar_tela_automatico()
    if len(lista) > 0:
        resposta = ultils.obter_string('Nome do Grupo ou confederação: ').strip().upper()
        lista_filtrados = []
        for i in range(len(lista)):
            if lista[i]['confederação'] == resposta or lista[i]['grupo'] == resposta:
                lista_filtrados.append(lista[i])
        
        print(f'Resultados possíveis para "{resposta}":')
        criar_tabela_selecao(lista_filtrados)
    else:
        print('Nenhuma seleção foi cadastrada!')
    
    ultils.limpar_tela('Digite ENTER para voltar ao menu')