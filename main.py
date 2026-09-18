import jogadores, partidas, persistência, seleções, ultils

def main():
    lista_partidas=[]
    lista_jogadores=[]
    lista_selecoes=[]
    lista_jogadores=persistência.carregar_jogadores("jogadores.txt",lista_jogadores)
    lista_selecoes=persistência.carregar_selecoes("seleções.txt",lista_selecoes)
    lista_partidas = persistência.carregar_partidas("partidas.txt", lista_partidas)
    while True:
        qtde_selecoes=len(lista_selecoes)
        qtde_jogadores=len(lista_jogadores)
        qtde_partidas=len(lista_partidas)
        ultils.limpar_tela_automatico()

        try:
            menu=f'''{"⚽ COPA MANAGER 2026 — FIFA ⚽":=^50}
    {f'Nmº seleções:{qtde_selecoes}/Nmº de jogadores:{qtde_jogadores}/Nmº de partidas:{qtde_partidas}':^50}
    {"SELECOES":-^50}
    1. Cadastrar selecao
    2. Listar / ordenar selecoes
    3. Buscar selecao por nome
    4. Filtrar por grupo ou confederacao
    --- JOGADORES ---
    5. Cadastrar jogador (vinculado a uma selecao)
    6. Listar / ordenar jogadores
    7. Filtrar jogadores
    8. Artilheiros e estatisticas (media de idade, total de gols)
    --- PARTIDAS ---
    9. Cadastrar partida
    10. Listar partidas
    11. Tabela de classificacao por grupo
    --- SISTEMA ---
    12. Salvar dados em arquivo
    0. Sair (salva automaticamente)

    Escolha uma opcao: '''
            
            resposta=ultils.obter_inteiro(menu)
            if resposta==0:
             persistência.salvar_selecoes("seleções.txt", lista_selecoes)
             persistência.salvar_jogadores("jogadores.txt", lista_jogadores)
             persistência.salvar_partidas("partidas.txt", lista_partidas)
             break
            elif resposta==1:
                seleções.cadastrar_selecao(lista_selecoes)
            elif resposta==2:
                seleções.listar_ord_selecoes(lista_selecoes)
            elif resposta==3:
                seleções.buscar_selecao(lista_selecoes)
            elif resposta==4:
                seleções.filtrar_selecao(lista_selecoes)
            elif resposta==5:
                jogadores.cadastrar_jogador(lista_selecoes,lista_jogadores)
            elif resposta==6:
                jogadores.listar_ord_jogadores(lista_jogadores, lista_selecoes)
            elif resposta==7:
                jogadores.filtrar_jogadores(lista_jogadores,lista_selecoes)
            elif resposta==8:
                jogadores.estatisticas_artilheiros(lista_jogadores, lista_selecoes)
            elif resposta==9:
                partidas.cadastrar_partida(lista_partidas, lista_selecoes)
            elif resposta==10:
                partidas.listar_partidas(lista_partidas, lista_selecoes)
            elif resposta==11:
                partidas.tabela_classificacao_grupo(lista_partidas, lista_selecoes)
            elif resposta==12:
                persistência.salvar_selecoes("seleções.txt", lista_selecoes)
                persistência.salvar_jogadores("jogadores.txt", lista_jogadores)
                persistência.salvar_partidas("partidas.txt", lista_partidas)
                ultils.mensagem_salvamento()

        except ValueError:
            print('opção inadequada')

            
main()