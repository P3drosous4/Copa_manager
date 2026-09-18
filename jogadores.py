import ultils
import tabulate


def cadastrar_jogador(lista_selecao, lista_jogadores):
    while True:
        if len(lista_selecao) == 0:
            print('Cadastre uma seleção primeiro!')
            return lista_jogadores
        else:
            print(f"{'-Seleções disponíveis-':^20}")
            lista_validacao = listagem_selecao(lista_selecao)
            selecao = validacao_selecao(lista_validacao)
            dicionario = preenchimento_cadastro(selecao, lista_jogadores)
            lista_jogadores.append(dicionario)
        
        if ultils.validacao():
            break
    
    ultils.limpar_tela('Digite Enter para voltar ao Menu...')
    return lista_jogadores


def validacao_selecao(lista_validacao):
    while True:
        selecao = ultils.obter_inteiro('Digite o ID da seleção do jogador: ')
        id_encontrado = False
        for id_valido in lista_validacao:
            if selecao == id_valido:
                id_encontrado = True
                break
        if id_encontrado == True:
            return selecao
        else:
            print('Digite um ID adequado!')

def listagem_selecao(lista_selecao):
    lista_validacao = []
    for lista in lista_selecao:
        lista_validacao.append(lista['id'])
        print(f"-{lista['id']:<10}{lista['seleção']:>10}")
    return lista_validacao

def id_automatico(lista_jogadores):
    if len(lista_jogadores) == 0:
        id = 1
    else:
        maior_id = 0
        for jogador in lista_jogadores:
            if jogador['id'] > maior_id:
                maior_id = jogador['id']
        id = maior_id + 1
    return id

def preenchimento_cadastro(selecao, lista_jogadores):
    id = id_automatico(lista_jogadores)
    nome = ultils.obter_string('Nome do jogador: ')
    posicao = ultils.obter_string('Qual a posição do jogador? (goleiro/atacante/zagueiro/central): ')
    idade = ultils.obter_inteiro('Qual a idade do jogador: ')
    gols = ultils.obter_inteiro('Quantos gols ele fez: ')

    print(f'[OK] Jogador {nome} cadastrado com sucesso!')
    
    dicionario = {
        "id": id,
        "nome": nome,
        "selecao_id": selecao,
        "posicao": posicao,
        "idade": idade,
        "gols": gols,
    }
    return dicionario


def criar_tabela_jogadores(lista_jogadores, lista_selecao):
    ultils.limpar_tela_automatico()
    linhas_tabelas = []
    cabecalho = ['id', 'nome', 'seleção', 'posição', 'idade', 'gols']
    
    for resultado in lista_jogadores:
        for relacionamento in lista_selecao:
            if resultado['selecao_id'] == relacionamento['id']:
                selecao = relacionamento['seleção']
                lista_resultado = [
                    resultado['id'],
                    resultado['nome'],
                    selecao,
                    resultado['posicao'],
                    resultado['idade'],
                    resultado['gols']
                ]
                linhas_tabelas.append(lista_resultado)
    
    tabela = tabulate.tabulate(linhas_tabelas, headers=cabecalho, tablefmt='fancy_grid')
    print(tabela)


def obter_posicao_para_ordenacao(jogador):
    return jogador['posicao']

def obter_nome_para_ordenacao(jogador):
    return jogador['nome']

def obter_idade_para_ordenacao(jogador):
    return jogador['idade']

def obter_gols_para_ordenacao(jogador):
    return jogador['gols']

def ordenar_jogadores(lista_jogadores):
    if len(lista_jogadores) == 0:
        print('A lista de jogadores está vazia!')
        return lista_jogadores
    
    msg = 'Como você quer ordenar a listagem? (posicao, nome, idade, gols, não ordenar): '
    opcao = ultils.obter_string(msg).lower().strip()
    opc_comp = ultils.remover_acentos(opcao)
    
    if opc_comp in ['nao', 'nao ordenar']:
        return lista_jogadores
    
    escolha = ultils.valorboll('Ordem inversa? (S/N): ')
    lista_ordenada = opcoes_ordenacao(opc_comp, escolha, lista_jogadores)
    return lista_ordenada

def opcoes_ordenacao(opc_comp, escolha, lista_jogadores):
    if opc_comp == 'posicao':
        lista_ordenada = sorted(lista_jogadores, key=obter_posicao_para_ordenacao, reverse=escolha)
    elif opc_comp == 'gols':
        lista_ordenada = sorted(lista_jogadores, key=obter_gols_para_ordenacao, reverse=escolha)
    elif opc_comp == 'nome':
        lista_ordenada = sorted(lista_jogadores, key=obter_nome_para_ordenacao, reverse=escolha)
    elif opc_comp == 'idade':
        lista_ordenada = sorted(lista_jogadores, key=obter_idade_para_ordenacao, reverse=escolha)
    elif opc_comp in ['nao', 'nao ordenar']:
        lista_ordenada = lista_jogadores
    else:
        print('Opção indisponível')
        lista_ordenada = lista_jogadores
    return lista_ordenada


def listar_ord_jogadores(lista_jogadores, lista_selecao):
    lista_jogadores = ordenar_jogadores(lista_jogadores)
    criar_tabela_jogadores(lista_jogadores, lista_selecao)
    ultils.limpar_tela('Digite ENTER para voltar ao menu...')


def criar_filtro_posicao(posicao_escolhida):
    def filtro(jogador):
        return jogador['posicao'] == posicao_escolhida
    return filtro


def criar_filtro_idade(idade_min, idade_max):
    def filtro(jogador):
        if jogador['idade'] >= idade_min and jogador['idade'] <= idade_max:
            return True
        else:
            return False
    return filtro


def criar_filtro_selecao(selecao_id):
    def filtro(jogador):
        return jogador['selecao_id'] == selecao_id
    return filtro


def filtrar_jogadores(lista_jogadores, lista_selecao):
    if len(lista_jogadores) == 0:
        print('Cadastre jogadores primeiro!')
        ultils.limpar_tela('Pressione ENTER para voltar ao menu...')
        return

    ultils.limpar_tela_automatico()
    print("="*50)
    print("FILTRAR JOGADORES".center(50))
    print("="*50)
    
    msg = 'Como você quer filtrar os jogadores? (posicao/faixa de idade/nome da selecao): '
    opcao = ultils.obter_string(msg).lower().strip()
    opcao = ultils.remover_acentos(opcao)
    
    if opcao == 'posicao':
        posicao_escolhida = ultils.obter_string('Qual posição escolhida: ').lower().strip()
        funcao_filtro = criar_filtro_posicao(posicao_escolhida)
        filtrados = ultils.filter_manual(lista_jogadores, funcao_filtro)
        
    elif opcao == 'faixa de idade':
        idade_min = ultils.obter_inteiro('Idade mínima: ')
        idade_max = ultils.obter_inteiro('Idade máxima: ')
        funcao_filtro = criar_filtro_idade(idade_min, idade_max)
        filtrados = ultils.filter_manual(lista_jogadores, funcao_filtro)
        
    elif opcao == 'nome da selecao':
        filtrados = buscar_jogador(lista_selecao, lista_jogadores)
        
    else:
        print('Opção indisponível no momento!')
        ultils.limpar_tela('Pressione ENTER para voltar ao menu...')
        return
    
    if len(filtrados) > 0:
        ultils.limpar_tela_automatico()
        print(f"\n{len(filtrados)} jogadores encontrados:")
        criar_tabela_jogadores(filtrados, lista_selecao)
    else:
        print("Nenhum jogador encontrado com esse filtro.")
    
    ultils.limpar_tela('Pressione ENTER para voltar ao menu...')

def buscar_jogador(lista_selecao, lista_jogadores):
    jogadores_filtrados = []
    nome_selecao = ultils.obter_string('Digite o nome da seleção: ').lower().strip()
    
    selecao_id = -1
    for selecao in lista_selecao:
        nome_atual = selecao['seleção'].lower()
        if nome_selecao in nome_atual:
            selecao_id = selecao['id']
            break
    
    if selecao_id == -1:
        print('Seleção não encontrada!')
        ultils.limpar_tela('Pressione ENTER para voltar ao menu...')
        return []
    
    for jogador in lista_jogadores:
        if jogador['selecao_id'] == selecao_id:
            jogadores_filtrados.append(jogador)
    return jogadores_filtrados



def acumular_artilheiro(artilheiro_atual, jogador):
    if jogador['gols'] > artilheiro_atual['gols']:
        return jogador
    else:
        return artilheiro_atual


def acumular_gols(total_atual, jogador):
    return total_atual + jogador['gols']


def acumular_idade(total_atual, jogador):
    return total_atual + jogador['idade']


def encontrar_artilheiro_geral(lista_jogadores):
    if len(lista_jogadores) == 0:
        return None
    artilheiro = ultils.reduce_manual(lista_jogadores, acumular_artilheiro, lista_jogadores[0])
    return artilheiro


def calcular_total_gols(lista_jogadores):
    total = ultils.reduce_manual(lista_jogadores, acumular_gols, 0)
    return total


def calcular_media_idade(lista_jogadores):
    if len(lista_jogadores) == 0:
        return 0
    total_idades = ultils.reduce_manual(lista_jogadores, acumular_idade, 0)
    return total_idades / len(lista_jogadores)


def calcular_total_gols_selecao(jogadores_selecao):
    total = ultils.reduce_manual(jogadores_selecao, acumular_gols, 0)
    return total


def encontrar_artilheiro_selecao(jogadores_selecao):
    if len(jogadores_selecao) == 0:
        return None
    artilheiro = ultils.reduce_manual(jogadores_selecao, acumular_artilheiro, jogadores_selecao[0])
    return artilheiro


def estatisticas_artilheiros(lista_jogadores, lista_selecao):
    if len(lista_jogadores) == 0:
        print("Nenhum jogador cadastrado!")
        ultils.limpar_tela('Pressione ENTER para voltar ao menu...')
        return
    
    ultils.limpar_tela_automatico()
    print("="*70)
    print("ESTATÍSTICAS E ARTILHEIROS".center(70))
    print("="*70)

    artilheiro = encontrar_artilheiro_geral(lista_jogadores)
    total_gols = calcular_total_gols(lista_jogadores)
    media_idade = calcular_media_idade(lista_jogadores)

    exibir_estatisticas_gerais(artilheiro, total_gols, media_idade)
    exibir_artilheiros_por_selecao(lista_jogadores, lista_selecao)

    ultils.limpar_tela('Pressione ENTER para voltar ao menu...')


def exibir_estatisticas_gerais(artilheiro, total_gols, media_idade):
    print("\nARTILHEIRO DA COPA:")
    print(f"   {artilheiro['nome']} - {artilheiro['gols']} gols")
    print(f"\nESTATÍSTICAS GERAIS:")
    print(f"   Total de gols: {total_gols}")
    print(f"   Média de idade: {media_idade:.1f} anos")


def exibir_artilheiros_por_selecao(lista_jogadores, lista_selecao):
    print("\nARTILHEIROS POR SELEÇÃO:")
    for selecao in lista_selecao:
        jogadores_selecao = filtrar_jogadores_por_selecao(lista_jogadores, selecao['id'])
        if len(jogadores_selecao) > 0:
            artilheiro = encontrar_artilheiro_selecao(jogadores_selecao)
            total_gols = calcular_total_gols_selecao(jogadores_selecao)
            print(f"   {selecao['seleção']}: {artilheiro['nome']} ({artilheiro['gols']} gols) - Total: {total_gols}")


def filtrar_jogadores_por_selecao(lista_jogadores, selecao_id):
    jogadores_selecao = []
    for jogador in lista_jogadores:
        if jogador['selecao_id'] == selecao_id:
            jogadores_selecao.append(jogador)
    return jogadores_selecao

# ===== FUNÇÕES PARA MAP_MANUAL (exemplo) =====

def extrair_nome_jogador(jogador):
    return jogador['nome']

def extrair_gols_jogador(jogador):
    return jogador['gols']