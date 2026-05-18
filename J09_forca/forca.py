import random
import os

def limpar():
  os.system("cls")

def escolher_palavra() -> str :
    palavras = ["abacaxi", "biblioteca","coruja", "diamante", "elefante", "fogueira", "girassol", "helicóptero", 
                "internet", "jangada"," koala", "lâmpada", "montanha", "nuvem", "oceano", "planeta", "quartzo", "relógio", "sorvete", "tartaruga"]

    palavra_aleatoria = random.choice(palavras)

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

lista_tracos = gerar_tracos("jangada")
print(*lista_tracos)

def perguntar_letra() -> str:
    resposta = input("Digite UMA letra:").upper()
    while len (resposta) != 1:
        resposta = input ("Eu disse penas UMA letra:").upper()
        return resposta
letra = perguntar_letra()
print(letra)

def jogar_forca():
    
if __name__ == "__main__":
    jogar_forca()
    pass

print("""
      _            __ _                       _                       ___                                  
   _ | |   ___    / _` |   ___      o O O  __| |   __ _      o O O   | __|   ___      _ _    __     __ _   
  | || |  / _ \   \__, |  / _ \    o      / _` |  / _` |    o        | _|   / _ \    | '_|  / _|   / _` |  
  _\__/   \___/   |___/   \___/   TS__[O] \__,_|  \__,_|   TS__[O]  _|_|_   \___/   _|_|_   \__|_  \__,_|  
_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""| {======|_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
      """)

