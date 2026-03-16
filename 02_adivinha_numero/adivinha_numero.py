
print(""" ____  _____  ___  _____    ____  ____      __    ____  ____  _  _  ____  _  _  _   _    __     
 (_  _)(  _  )/ __)(  _  )  (  _ \( ___)    /__\  (  _ \(_  _)( \/ )(_  _)( \( )( )_( )  /__\    
.-_)(   )(_)(( (_-. )(_)(    )(_) ))__)    /(__)\  )(_) )_)(_  \  /  _)(_  )  (  ) _ (  /(__)\   
\____) (_____)\___/(_____)  (____/(____)  (__)(__)(____/(____)  \/  (____)(_)\_)(_) (_)(__)(__)  
      """)
    
print("""
      
      
      
 *******************************
 *   1- Noob (de 1 a 10)       *
 *   2- Medio(de 1 a 20)       *
 *   3-profissional ( 1 a 50)  *
 *   4-SENAI (1 a 200)         *
 *******************************
      """)

import random

pergunta = int(input("escolha o seu nivel:"))


if pergunta == 1:

    numero_aleatorio = random.randrange(1,11)
    pergunta = int(input(" escolha o seu numero:"))
    if pergunta == numero_aleatorio:
        print (f"voce acertou!!!")
    else:
        print(f"voce errou, eu estava pensando em {numero_aleatorio}")

if pergunta == 2:

    numero_aleatorio = random.randrange(1,21)
    pergunta = int(input(" escolha o seu numero:"))
    if pergunta == numero_aleatorio:
        print (f"voce acertou!!!")
    else:
        print(f"voce errou, eu estava pensando em {numero_aleatorio}")

if pergunta == 3:

    numero_aleatorio = random.randrange(1,51)
    pergunta = int(input(" escolha o seu numero:"))
    if pergunta == numero_aleatorio:
        print (f"voce acertou!!!")
    else:
        print(f"voce errou, eu estava pensando em {numero_aleatorio}")

if pergunta == 4:

    numero_aleatorio = random.randrange(1,201)
    pergunta = int(input(" escolha o seu numero:"))
    if pergunta == numero_aleatorio:
        print (f"voce acertou!!!")
    else:
        print(f"voce errou, eu estava pensando em {numero_aleatorio}")

if pergunta > 4 :
    print("esse nivel não existe")
else:
    print(" esse video não exite ")