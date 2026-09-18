import ultils
import persistência
from tabulate import tabulate


def cadastrar_partida(lista_partidas, lista_selecao):
    if len(lista_selecao) < 2:
        print("É necessário ter pelo menos 2 seleções cadastradas!")
        ultils.limpar_tela('Pressione ENTER para voltar...')
        return lista_partidas
    
    ultils.limpar_tela_automatico()
    print("="*50)
    print("CADASTRAR PARTIDA".center(50))
    print("="*50)
    lista_partidas,partida=lista_de_partidas(lista_partidas, lista_selecao)
    exibir_mensagem_partida(partida, lista_selecao)
    persistência.salvar_partidas("partidas.txt", lista_partidas)
    ultils.limpar_tela('Pressione ENTER para continuar...')
    return lista_partidas


def lista_de_partidas(lista_partidas, lista_selecao):
    id = calcular_proximo_id_partida(lista_partidas)
    mostrar_selecoes_disponiveis(lista_selecao)
    casa_id = selecionar_time_casa(lista_selecao)
    fora_id = selecionar_time_fora(lista_selecao, casa_id)
    gols_casa = ultils.obter_inteiro("Gols da seleção da casa: ")
    gols_fora = ultils.obter_inteiro("Gols da seleção visitante: ")
    fase = selecionar_fase()
    partida = montar_dicionario_partida(id, casa_id, fora_id, gols_casa, gols_fora, fase)
    lista_partidas.append(partida)
    return lista_partidas,partida


def calcular_proximo_id_partida(lista_partidas):
    if len(lista_partidas) == 0:
        return 1
    else:
        maior_id = 0
        for partida in lista_partidas:
            if partida['id'] > maior_id:
                maior_id = partida['id']
        return maior_id + 1


def mostrar_selecoes_disponiveis(lista_selecao):
    print("\nSeleções disponíveis:")
    for selecao in lista_selecao:
        print(f"  {selecao['id']} - {selecao['seleção']} (Grupo {selecao['grupo']})")


def selecionar_time_casa(lista_selecao):
    while True:
        casa_id = ultils.obter_inteiro("ID da seleção da casa: ")
        if id_valido_selecao(casa_id, lista_selecao) == True:
            return casa_id
        else:
            print("ID inválido!")


def selecionar_time_fora(lista_selecao, casa_id):
    while True:
        fora_id = ultils.obter_inteiro("ID da seleção visitante: ")
        if id_valido_selecao(fora_id, lista_selecao) == True and fora_id != casa_id:
            return fora_id
        elif fora_id == casa_id:
            print("A seleção visitante deve ser diferente da seleção da casa!")
        else:
            print("ID inválido!")


def id_valido_selecao(id, lista_selecao):
    for selecao in lista_selecao:
        if id == selecao['id']:
            return True
    return False


def selecionar_fase():
    fases = ["Grupos", "Oitavas", "Quartas", "Semi", "Final"]
    print("\nFases disponíveis:")
    for i in range(len(fases)):
        print(f"  {i+1} - {fases[i]}")
    while True:
        opcao = ultils.obter_inteiro("Escolha a fase (1-5): ")
        if opcao >= 1 and opcao <= 5:
            return fases[opcao-1]
        else:
            print("Opção inválida!")


def montar_dicionario_partida(id, casa_id, fora_id, gols_casa, gols_fora, fase):
    partida = {
        "id": id,
        "selecao_casa_id": casa_id,
        "selecao_fora_id": fora_id,
        "gols_casa": gols_casa,
        "gols_fora": gols_fora,
        "fase": fase
    }
    return partida


def exibir_mensagem_partida(partida, lista_selecao):
    nome_casa = buscar_nome_selecao_por_id_partida(partida['selecao_casa_id'], lista_selecao)
    nome_fora = buscar_nome_selecao_por_id_partida(partida['selecao_fora_id'], lista_selecao)
    print(f"\nPartida cadastrada: {nome_casa} {partida['gols_casa']} x {partida['gols_fora']} {nome_fora} ({partida['fase']})")


def buscar_nome_selecao_por_id_partida(id, lista_selecao):
    for selecao in lista_selecao:
        if selecao['id'] == id:
            return selecao['seleção']
    return ""


def listar_partidas(lista_partidas, lista_selecao):
    if len(lista_partidas) == 0:
        print("Nenhuma partida cadastrada!")
        ultils.limpar_tela('Pressione ENTER para voltar...')
        return
    ultils.limpar_tela_automatico()
    print("="*70)
    print("PARTIDAS CADASTRADAS".center(70))
    print("="*70)
    linhas = construir_linhas_tabela_partida(lista_partidas, lista_selecao)
    cabecalho = ['ID', 'Casa', 'Placar', 'Visitante', 'Fase']
    tabela = tabulate(linhas, headers=cabecalho, tablefmt='fancy_grid')
    print(tabela)
    ultils.limpar_tela('Pressione ENTER para voltar ao menu...')


def construir_linhas_tabela_partida(lista_partidas, lista_selecao):
    linhas = []
    for partida in lista_partidas:
        nome_casa = buscar_nome_selecao_por_id_partida(partida['selecao_casa_id'], lista_selecao)
        nome_fora = buscar_nome_selecao_por_id_partida(partida['selecao_fora_id'], lista_selecao)
        placar = f"{partida['gols_casa']} x {partida['gols_fora']}"
        linha = []
        linha.append(partida['id'])
        linha.append(nome_casa)
        linha.append(placar)
        linha.append(nome_fora)
        linha.append(partida['fase'])
        linhas.append(linha)
    return linhas



def tabela_classificacao_grupo(lista_partidas, lista_selecao):
    if len(lista_partidas) == 0:
        print("Nenhuma partida cadastrada!")
        ultils.limpar_tela('Pressione ENTER para voltar...')
        return
    ultils.limpar_tela_automatico()
    print("="*70)
    print("TABELA DE CLASSIFICAÇÃO".center(70))
    print("="*70)
    grupos = agrupar_selecoes_por_grupo(lista_selecao)
    for grupo in ordenar_grupos(grupos):
        imprimir_tabela_grupo(grupo, grupos[grupo], lista_partidas)
    ultils.limpar_tela('Pressione ENTER para voltar ao menu...')


def agrupar_selecoes_por_grupo(lista_selecao):
    grupos = {}
    for selecao in lista_selecao:
        grupo = selecao['grupo']
        if grupo not in grupos:
            grupos[grupo] = []
        grupos[grupo].append(selecao)
    return grupos


def ordenar_grupos(grupos):
    lista_grupos = []
    for grupo in grupos:
        lista_grupos.append(grupo)
    lista_grupos.sort()
    return lista_grupos


def imprimir_tabela_grupo(grupo, selecoes, lista_partidas):
    print(f"\n{'='*20} GRUPO {grupo} {'='*20}")
    estatisticas = calcular_estatisticas_grupo(selecoes, lista_partidas)
    estatisticas = ordenar_classificacao(estatisticas)
    exibir_classificacao(estatisticas)


def calcular_estatisticas_grupo(selecoes, lista_partidas):
    estatisticas = []
    for selecao in selecoes:
        stats = calcular_estatisticas_selecao(selecao['id'], lista_partidas)
        stats['nome'] = selecao['seleção']
        estatisticas.append(stats)
    return estatisticas


def ordenar_classificacao(estatisticas):
    for i in range(len(estatisticas)):
        for j in range(i + 1, len(estatisticas)):
            if estatisticas[i]['pontos'] < estatisticas[j]['pontos']:
                estatisticas[i], estatisticas[j] = estatisticas[j], estatisticas[i]
            elif estatisticas[i]['pontos'] == estatisticas[j]['pontos']:
                if estatisticas[i]['saldo'] < estatisticas[j]['saldo']:
                    estatisticas[i], estatisticas[j] = estatisticas[j], estatisticas[i]
    return estatisticas


def exibir_classificacao(estatisticas):
    print("\nPos | Seleção           | Pontos | Jogos | Vitótias | Empates | Derrotas | GP | GC | SG")
    print("-"*70)
    posicao = 1
    for stats in estatisticas:
        print(f"{posicao:2}  | {stats['nome']:<18} | {stats['pontos']:1} | {stats['jogos']:1} | "
              f"{stats['vitorias']:1} | {stats['empates']:1} | {stats['derrotas']:1} | "
              f"{stats['gols_pro']:2} | {stats['gols_contra']:2} | {stats['saldo']:+2}")
        posicao = posicao + 1


def calcular_estatisticas_selecao(selecao_id, lista_partidas):
    stats = {
        'jogos': 0,
        'vitorias': 0,
        'empates': 0,
        'derrotas': 0,
        'gols_pro': 0,
        'gols_contra': 0,
        'pontos': 0,
        'saldo': 0
    }
    for partida in lista_partidas:
        if partida['selecao_casa_id'] == selecao_id:
            atualizar_estatisticas_casa(stats, partida)
        elif partida['selecao_fora_id'] == selecao_id:
            atualizar_estatisticas_fora(stats, partida)
    stats['saldo'] = stats['gols_pro'] - stats['gols_contra']
    return stats


def atualizar_estatisticas_casa(stats, partida):
    stats['jogos'] = stats['jogos'] + 1
    stats['gols_pro'] = stats['gols_pro'] + partida['gols_casa']
    stats['gols_contra'] = stats['gols_contra'] + partida['gols_fora']
    if partida['gols_casa'] > partida['gols_fora']:
        stats['vitorias'] = stats['vitorias'] + 1
        stats['pontos'] = stats['pontos'] + 3
    elif partida['gols_casa'] == partida['gols_fora']:
        stats['empates'] = stats['empates'] + 1
        stats['pontos'] = stats['pontos'] + 1
    else:
        stats['derrotas'] = stats['derrotas'] + 1


def atualizar_estatisticas_fora(stats, partida):
    stats['jogos'] = stats['jogos'] + 1
    stats['gols_pro'] = stats['gols_pro'] + partida['gols_fora']
    stats['gols_contra'] = stats['gols_contra'] + partida['gols_casa']
    if partida['gols_fora'] > partida['gols_casa']:
        stats['vitorias'] = stats['vitorias'] + 1
        stats['pontos'] = stats['pontos'] + 3
    elif partida['gols_fora'] == partida['gols_casa']:
        stats['empates'] = stats['empates'] + 1
        stats['pontos'] = stats['pontos'] + 1
    else:
        stats['derrotas'] = stats['derrotas'] + 1