def jogar_par_ou_impar ():
    import random
    print("""
        _                         _                                             _                             
    (_)                       | |                                           (_)                            
        _  ___   __ _  ___     __| | ___     _ __   __ _ _ __     ___  _   _   _ _ __ ___  _ __   __ _ _ __  
    | |/ _ \ / _` |/ _ \   / _` |/ _ \   | '_ \ / _` | '__|   / _ \| | | |  | | '_ ` _ \| '_ \ / _` | '__| 
    | | (_) | (_| | (_) | | (_| | (_) |  | |_) | (_| | |     | (_) | |_| |  | | | | | | | |_) | (_| | |    
    | |\___/ \__, |\___/   \__,_|\___/   | .__/ \__,_|_|      \___/ \__,_|  |_|_| |_| |_| .__/ \__,_|_|    
    _/ |       __/ |                      | |                                          | |                
    |__/       |___/                       |_|                                          |_|                
        
    """)
    
    lado= input ("impar ou par?")
    if lado== "impar":
        print("então eu sou o par!")
    elif lado == "par":
        print("então eu sou o impar!")

    if lado!= "par" or "impar":
        print ("essa opção não existe")

        numero02= random.randrange (0,11) 

        numero01= int(input("qual sera o numero de 0 a 10 escolhido?"))

        if numero01 > 10:
            print(f"você não tem {numero01} dedos")
        else:
            print (f"{numero01} + {numero02}")
            if lado == 'par':
                if (numero01 + numero02) %2 ==0:
                    print("O número é par, você venceu!")
                else:
                    print(f"O número é Ímpar, você perdeu!")

            elif lado == 'impar':
                if (numero01 + numero02) %2 ==1:
                    print("O número é par, você perdeu!")
                else:
                    print(f"O número é impar,você ganhou!")


