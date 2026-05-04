def jogar_cara_coroa ():
  import random

  print("""                                           
    ___ __ _ _ __ __ _    ___  _   _    ___ ___  _ __ ___   __ _ 
  / __/ _` | '__/ _` |  / _ \| | | |  / __/ _ \| '__/ _ \ / _` |
  | (_| (_| | | | (_| | | (_) | |_| | | (_| (_) | | | (_) | (_| |
  \___\__,_|_|  \__,_|  \___/ \__,_|  \___\___/|_|  \___/ \__,_|                        
    
        
                          
                      ..;;;--'~~~`--;;;..
                      /;-~IN GOD WE TRUST~-.\
                    //      ,;;;;;;;;      \\
                  .//      ;;;;;    \       \\
                  ||       ;;;;(   /.|       ||
                  ||       ;;;;;;;   _\      ||
                  ||       ';;  ;;;;=        ||
                  ||LIBERTY | ''\;;;;;;      ||
                    \\     ,| '\  '|><| 1995 //
                    \\   |     |      \  A //
                      `;.,|.    |      '\.-'/
                        ~~;;;,._|___.,-;;;~'
                          ''=--<dcau>'

                                                                
        """)

  escolha= input("escolha cara ou coroa").lower()
  aleatorio= random.choice(["cara","coroa"])
  if escolha== aleatorio:
      print ('parabens você ganhou')
  else:
      print("você perdeu hahahahaha")
  print(f"o certo seria {aleatorio}")