def jogar_genius():
    import os
    import time
    import random
    dicionario_cores={"VERDE" : "A0",
                    "AZUL"  :  "90", 
                    "AMARELO" :"E0",
                    "VERMELHO" :"C0"}

    lista_sequencia= []

    def limpar_tela():
        os.system("color 07")
        os.system("cls")


    def mudar_cor(cor):
        codigo_cor= dicionario_cores[cor]
        os.system(f"color {codigo_cor}")
        time.sleep(1)
        limpar_tela()

    print("""
            (`-')  _<-. (`-')_  _                 (`-').->    
        .->    ( OO).-/   \( OO) )(_)         .->    ( OO)_      
    ,---(`-')(,------.,--./ ,--/ ,-(`-'),--.(,--.  (_)--\_)     
    '  .-(OO ) |  .---'|   \ |  | | ( OO)|  | |(`-')/    _ /     
    |  | .-, \(|  '--. |  . '|  |)|  |  )|  | |(OO )\_..`--.     
    |  | '.(_/ |  .--' |  |\    |(|  |_/ |  | | |  \.-._)   \    
    |  '-'  |  |  `---.|  | \   | |  |'->\  '-'(_ .'\       /    
    `-----'   `------'`--'  `--' `--'    `-----'    `-----'     
    ---------------Repita as Cores sem Errar------------------
        
                    ********************
                    #  G PARA VERDE    #    
                    #  B PARA AZUL     # 
                    #  Y PARA AMARELO  #
                    #  R PARA VERMELHO #
                    ********************

        """)
    input("precione qualquer tecla para começar.....")
    limpar_tela()
    lista_cores=["VERDE","AZUL","AMARELO","VERMELHO"]

    while True:
        cor_aleatoria = random.choice(lista_cores)
        lista_sequencia.append(cor_aleatoria)
        for cor_lista in lista_sequencia:
            mudar_cor (cor_lista)


        resposta = input ("Digite a sequencia de Cores Correta:").upper()
        dicionario_apreviacoes= {"G" : "VERDE",
                                "B" : "AZUL",
                                "Y" : "AMARELO",
                                "R" : "VERMELHO" }
        lista_resposta = []
        for letra in resposta:
            cor = dicionario_apreviacoes.get [letra]
            lista_resposta.append (cor)
        if lista_resposta != lista_sequencia:
            print("Você errou.") 
            print ("a sequencia era:")
            print(*lista_sequencia)
            break
        else:
            print("Você acertou!")
            print ("Vamos para a proxima fase")
            input ("Aperte ENTER quando estiver pronto....")
            limpar_tela()

