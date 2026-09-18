SEPARADOR = ";"
def montar_linha_selecao(s):
    valores = [
    str(s["id"]),
    s["seleção"],
    s["confederação"],
    s["grupo"],
    str(s["ranking"]),
    str(s["títulos"]),
    ]
    return SEPARADOR.join(valores) 

def salvar_selecoes(caminho, selecoes):
    arquivo = open(caminho, "w", encoding="utf-8")
    for s in selecoes:
     linha = montar_linha_selecao(s)
     arquivo.write(linha + "\n") # uma linha por registro
    arquivo.close()
    print("Seleções salvas com sucesso!")


def montar_selecao_da_linha(linha):
    partes = linha.split(SEPARADOR) # separa a linha de volta em uma lista
    selecao = {
    "id": int(partes[0]), # converte para int o que é número!
    "seleção": partes[1],
    "confederação": partes[2],
    "grupo": partes[3],
    "ranking": int(partes[4]),
    "títulos": int(partes[5]),
    }
    return selecao
def carregar_selecoes(caminho,selecoes):
    try:
         arquivo = open(caminho, "r", encoding="utf-8")
         for linha in arquivo:
              linha = linha.strip() # remove o "\n" e espaços
              if linha_valida(linha,6): # pula linhas em branco
                selecoes.append(montar_selecao_da_linha(linha))
              else:
                 if linha:
                    print(f'[AVISO] linha corrompida ignorada no arquivo {caminho}')
         arquivo.close()
    except FileNotFoundError:
     print(f"Arquivo {caminho} ainda não existe. Começando com lista vazia.")
    
    return selecoes
    

def linha_valida(linha, qtd_campos):
    partes = linha.split(SEPARADOR)
    return len(partes) == qtd_campos


def montar_linha_jogadores(lista_jogadores):
    valores = [
    str(lista_jogadores["id"]),
    lista_jogadores["nome"],
    str(lista_jogadores["selecao_id"]),
    lista_jogadores["posicao"],
    str(lista_jogadores["idade"]),
    str(lista_jogadores["gols"]),
    ]
    return SEPARADOR.join(valores) 



def salvar_jogadores(caminho, lista_jogadores):
    arquivo = open(caminho, "w", encoding="utf-8")
    for jogadores in lista_jogadores:
     linha = montar_linha_jogadores(jogadores)
     arquivo.write(linha + "\n") 
    arquivo.close()
    print("Jogadores salvos com sucesso!")


def montar_jogadores_da_linha(linha):
    partes = linha.split(SEPARADOR) # separa a linha de volta em uma lista
    jogadores = {
    "id": int(partes[0]), # converte para int o que é número!
    "nome": partes[1],
    "selecao_id":int( partes[2]),
    "posicao": partes[3],
    "idade": int(partes[4]),
    "gols": int(partes[5]),
    }
    return jogadores


def carregar_jogadores(caminho,lista_jogadores):
    try:
         arquivo = open(caminho, "r", encoding="utf-8")
         for linha in arquivo:
              linha = linha.strip()
              if linha_valida(linha,6): 
                lista_jogadores.append(montar_jogadores_da_linha(linha))
              else:
                 if linha:
                    print(f'[AVISO] linha corrompida ignorada no arquivo {caminho}')
         arquivo.close()
    except FileNotFoundError:
     print(f"Arquivo {caminho} ainda não existe. Começando com lista vazia.")
    
    return lista_jogadores
    

def montar_linha_partida(partida):
    valores = [
        str(partida["id"]),
        str(partida["selecao_casa_id"]),
        str(partida["selecao_fora_id"]),
        str(partida["gols_casa"]),
        str(partida["gols_fora"]),
        partida["fase"],
    ]
    return SEPARADOR.join(valores)


def salvar_partidas(caminho, partidas):
        arquivo = open(caminho, "w", encoding="utf-8")
        for p in partidas:
            linha = montar_linha_partida(p)
            arquivo.write(linha + "\n")
        arquivo.close()
        print(" Partidas salvas com sucesso!")


def montar_partida_da_linha(linha):
    partes = linha.split(SEPARADOR)
    partida = {
        "id": int(partes[0]),
        "selecao_casa_id": int(partes[1]),
        "selecao_fora_id": int(partes[2]),
        "gols_casa": int(partes[3]),
        "gols_fora": int(partes[4]),
        "fase": partes[5],
    }
    return partida


def carregar_partidas(caminho, partidas):
    try:
        arquivo = open(caminho, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha and linha_valida(linha, 6):
                partidas.append(montar_partida_da_linha(linha))
            elif linha:
                print(f'[AVISO] Linha corrompida ignorada: {linha}')
        arquivo.close()
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado. Criando nova lista.")
    return partidas