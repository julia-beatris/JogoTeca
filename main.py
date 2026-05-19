from J01_mad_libs.madlibs import jogar_mad_libs
from J02_adivinha_numero.adivinha_numero import jogar_adivinha_numero
from J03_jogo_tabuada.jogo_tabuada import jogar_jogo_tabuada
from J04_par_ou_impar.par_ou_impar import jogar_par_ou_impar
from J05_pedra_papel_tesoura.pedra_papel_tesoura import jogar_pedra_papel_tesoura
from J06_cara_coroa.cara_coroa import jogar_cara_coroa
from J07_adivinhação.adivinhação import jogar_adivinhação
from J08_genius.genius import jogar_genius
from J09_forca.forca import jogar_forca

while True:
    print("""
        .-./` )     ,-----.      .-_'''-.       ,-----.            ,---------.    .-''-.      _______      ____            
        \ '_ .') .'  .-,  '.   '_( )_   \    .'  .-,  '.          \          \ .'_ _   \    /   __  \   .'  __ `.         
        (_ (_) _)/ ,-.|  \ _ \ |(_ o _)|  '  / ,-.|  \ _ \          `--.  ,---'/ ( ` )   '  | ,_/  \__) /   '  \  \        
        / .  \;  \  '_ /  | :. (_,_)/___| ;  \  '_ /  | :            |   \  . (_ o _)  |,-./  )       |___|  /  |        
    ___  |-'`| |  _`,/ \ _/  ||  |  .-----.|  _`,/ \ _/  |            :_ _:  |  (_,_)___|\  '_ '`)        _.-`   |        
    |   | |   ' : (  '\_/ \   ;'  \  '-   .': (  '\_/ \   ;           (_I_)  '  \   .---. > (_)  )  __ .'   _    |        
    |   `-'  /   \ `"/  \  ) /  \  `-'`   |  \ `"/  \  ) /            (_(=)_)  \  `-'    /(  .  .-'_/  )|  _( )_  |        
    \      /     '. \_/``".'    \        /   '. \_/``".'              (_I_)    \       /  `-'`-'     / \ (_ o _) /        
    `-..-'        '-----'       `'-...-'      '-----'                 '---'     `'-..-'     `._____.'   '.(_,_).'         
                                                                    
                                                                                Desenvolvido por: Julia Beatris 

        
    _.______
    | _______ |   * * * * * * * * * * * * * * * * * * *# 
    ||,-----.||   *        01-mad libs                 *
    |||     |||   *        02-adivinha                 *
    |||_____|||   *        03-tabuada                  *
    |`-------'|   *        04-par ou impar             *
    | +     O |   *        05-pedra,papel ou tesoura   *
    |      O  |   *        06-cara ou coroa            *
                  *        07-adivinhação              *
                  *        08-genius                   *
                  *        09-forca                    *
                  *        0- sair                     *
    | / /  ##,"   * * * * * * *  * * * * * * * * * * * * 
    `------"

    """)
    escolha=int(input("Com qual jogo você vai querer se divertir?"))

    if escolha == 1:
        jogar_mad_libs()
    elif escolha == 2:
        jogar_adivinha_numero()
    elif escolha == 3:
        jogar_jogo_tabuada()
    elif escolha == 4:
        jogar_par_ou_impar()
    elif escolha == 5:
        jogar_pedra_papel_tesoura()
    elif escolha == 6:
        jogar_cara_coroa()
    elif escolha == 7:
        jogar_adivinhação()
    elif escolha == 8:
        jogar_genius()
    elif escolha == 9:
        jogar_forca()
    elif escolha == 0:
        print("Foi otimo jogar com você!")
        break