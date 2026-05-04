def jogar_pedra_papel_tesoura ():
    import random 
    print("""\033[35m
                _           _                   _                _                            
    __ _ __ _| |_ ___    | |__  __ _ _ _ __ _| |_ __ _   ___  | |_ _  _ _ __  __ _ _ _  ___ 
    / _` / _` |  _/ _ \_  | '_ \/ _` | '_/ _` |  _/ _` | / -_) | ' \ || | '  \/ _` | ' \/ _ -
    \__, \__,_|\__\___( ) |_.__/\__,_|_| \__,_|\__\__,_| \___| |_||_\_,_|_|_|_\__,_|_||_\___/
    |___/             |/                                                                     
        """)


    escolha_computador= random.choice (["gato","barata","humano"])
    escolha_jogador= input("você escolhe gato,barata ou humano?")
    print(f'Eu escolhi {escolha_computador}!')
    if escolha_jogador == "gato":
        if escolha_computador == "gato":
            print('empate')
        elif escolha_computador == 'barata':
            print('parabens você venceu')
        else:
            print('você perdeu hahah')

    if escolha_jogador == "barata":
        if escolha_computador == "barata":
            print('empate')
        elif escolha_computador == 'humano':
            print('parabens você venceu')
        else:
            print('você perdeu hahaha')

    if escolha_jogador == "humano":
        if escolha_computador == "humano":
            print('empate')
        elif escolha_computador == 'gato':
            print('parabens você venceu')
        else:
            print('você perdeu hahaha')