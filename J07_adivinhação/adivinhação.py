def jogar_adivinhação ():
    import random
    print("""
    ('-.     _ .-') _                 (`-.                .-') _  ('-. .-.   ('-.                 ('-.                 
    ( OO ).-.( (  OO) )              _(OO  )_             ( OO ) )( OO )  /  ( OO ).-.            ( OO ).-.             
    / . --. / \     .'_   ,-.-') ,--(_/   ,. \ ,-.-') ,--./ ,--,' ,--. ,--.  / . --. /   .-----.  / . --. / .-'),-----. 
    | \-.  \  ,`'--..._)  |  |OO)\   \   /(__/ |  |OO)|   \ |  |\ |  | |  |  | \-.  \   '  .--./  | \-.  \ ( OO'  .-.  '
    .-'-'  |  | |  |  \  '  |  |  \ \   \ /   /  |  |  \|    \|  | )|   .|  |.-'-'  |  |  |  |('-..-'-'  |  |/   |  | |  |
    \| |_.'  | |  |   ' |  |  |(_/  \   '   /,  |  |(_/|  .     |/ |       | \| |_.'  | /_) |OO  )\| |_.'  |\_) |  |\|  |
    |  .-.  | |  |   / : ,|  |_.'   \     /__),|  |_.'|  |\    |  |  .-.  |  |  .-.  | ||  |`-'|  |  .-.  |  \ |  | |  |
    |  | |  | |  '--'  /(_|  |       \   /   (_|  |   |  | \   |  |  | |  |  |  | |  |(_'  '--'\  |  | |  |   `'  '-'  '
    `--' `--' `-------'   `--'        `-'      `--'   `--'  `--'  `--' `--'  `--' `--'   `-----'  `--' `--'     `-----' 
    """)
    contador=0
    numero_aleatorio = random.randrange(101)
    while True:
        pergunta=int(input("escolha um numero de 0 a 100 para começarmos o jogo:" ))
        if pergunta == numero_aleatorio:
            print (" Parabens você acertou!!!")
            break
        elif numero_aleatorio < pergunta :
            print("o numero que eu pensei foi menor do que você digitou!")
        elif numero_aleatorio > pergunta :
            print("o numero que eu pensei foi maior do que você digitou!")
        contador += 1
        if contador == 5:
            print("acabaram suas chanches, jogue novamente e tente sua sorte!")
            break

