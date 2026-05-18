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
                |      ( ° °)
                |
                |
                |
            """)
    elif erro == 2:
        print("""
                ---------
                |        !
                |     ( ° °)
                |        |
                |        |
                |
            """)
    elif erro == 3:
        print("""
                ---------
                |        !
                |     ( ° °)
                |     -- | 
                |        |
                |
            """)
    elif erro == 4:
        print("""
                ---------
                |        !
                |     ( ° °)
                |     -- | --
                |        |
                |
            """)
    elif erro == 5:
        print("""
                ---------
                |        !
                |     ( ° °)
                |     -- | --
                |        |
                |       /
            """)
    elif erro == 6:
        print(r"""
                ---------
                |        !
                |     ( ° °)
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