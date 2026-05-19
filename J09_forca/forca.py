import random
import os

def limpar():
    os.system("cls")

def escolher_palavra() -> str :
    palavras = ["abacaxi", "biblioteca","coruja", "diamante", "elefante", "fogueira", "girassol",  
                "internet", "jangada", "lâmpada", "montanha", "nuvem", "oceano", "planeta", "relógio", "sorvete", "tartaruga"]

    palavra_aleatoria = random.choice(palavras).upper()

    #retorna a palavra para quem chamou a função
    return palavra_aleatoria

def desenhar_forca(erro:int):
    limpar()

    if erro == 0:
        print("""
                ---------
                |       !
                |   
                |
                |
                |
            """)
    elif erro == 1:
        print("""
                ---------
                |        !
                |      (>ლ)
                |
                |
                |
            """)
    elif erro == 2:
        print("""
                ---------
                |        !
                |      (>ლ)
                |        |
                |        |
                |
            """)
    elif erro == 3:
        print("""
                ---------
                |        !
                |      (>ლ)
                |     -- | 
                |        |
                |
            """)
    elif erro == 4:
        print("""
                ---------
                |        !
                |      (>ლ)
                |     -- | --
                |        |
                |
            """)
    elif erro == 5:
        print("""
                ---------
                |        !
                |      (>ლ)
                |     -- | --
                |        |
                |       /
            """)
    elif erro == 6:
        print(r"""
                ---------
                |        !
                |      (>ლ)
                |     -- | --
                |        |
                |       / \
            """)
        
def gerar_tracos(palavra: str) ->list:   
    quantidade_de_letras = len (palavra)
    tracos = []
    while len(tracos)< quantidade_de_letras:
        tracos.append("_")
    return tracos


def perguntar_letra() -> str:
    resposta = input("Digite UMA letra:").upper()
    while len (resposta) != 1:
        resposta = input ("Eu disse penas UMA letra:").upper()
    return resposta

def jogar_forca():

    print(r"""
                                                        _ .-') _     ('-.                                  _  .-')              ('-.     
                                                        ( (  OO) )   ( OO ).-.                             ( \( -O )            ( OO ).-. 
        ,--. .-'),-----.   ,----.     .-'),-----.        \     .'_   / . --. /         ,------. .-'),-----. ,------.   .-----.  / . --. / 
    .-')| ,|( OO'  .-.  ' '  .-./-') ( OO'  .-.  '       ,`'--..._)  | \-.  \       ('-| _.---'( OO'  .-.  '|   /`. ' '  .--./  | \-.  \  
    ( OO |(_|/   |  | |  | |  |_( O- )/   |  | |  |       |  |  \  '.-'-'  |  |      (OO|(_\    /   |  | |  ||  /  | | |  |('-..-'-'  |  | 
    | `-'|  |\_) |  |\|  | |  | .--, \\_) |  |\|  |       |  |   ' | \| |_.'  |      /  |  '--. \_) |  |\|  ||  |_.' |/_) |OO  )\| |_.'  | 
    ,--. |  |  \ |  | |  |(|  | '. (_/  \ |  | |  |       |  |   / :  |  .-.  |      \_)|  .--'   \ |  | |  ||  .  '.'||  |`-'|  |  .-.  | 
    |  '-'  /   `'  '-'  ' |  '--'  |    `'  '-'  '       |  '--'  /  |  | |  |        \|  |_)     `'  '-'  '|  |\  \(_'  '--'\  |  | |  | 
    `-----'      `-----'   `------'       `-----'        `-------'   `--' `--'         `--'         `-----' `--' '--'  `-----'  `--' `--' 
            """)

    input("precione ENTER  para começar.....")
    
    contador_erro = 0 
    palavra = escolher_palavra()

    lista_tracos = gerar_tracos(palavra)
 
    while True:
        limpar()

        desenhar_forca(contador_erro)

        print(*lista_tracos)

        if "_" not in lista_tracos:
            print("parabens você ganhou!!!!!!")
            break

        letra = perguntar_letra()

        print(letra)

        if letra not in palavra:
            contador_erro += 1 
        tentativas.appe(letra) 

        if contador_erro == 7:
            print("Você perdeu hahahha")
            print (f"a palavra era {palavra}")
            break

        if letra in palavra:
            contador = 0
            for letra_palavra in palavra:
                if letra_palavra == letra:
                    lista_tracos[contador] = letra
                contador = contador + 1 


if __name__ == "__main__" :
    jogar_forca()