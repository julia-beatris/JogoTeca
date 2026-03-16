import random
n1 = random.randrange(21)
n2 = random.randrange(21)
conta = n1 * n2 
pergunta = int (input (f"quanto é {n1} x {n2}?"))
if pergunta == conta:
    print("parabens voce conseguiu ")
else :
    print ("você errou!")
    print (f"a resposta era: {conta}")