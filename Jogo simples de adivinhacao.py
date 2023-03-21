import random

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu número: "))
while(sorteado!=jogador):
    
    if(sorteado>jogador):
        print("ERRO, o numero é maior")
        
    elif(sorteado<jogador):
        print("ERRO, o numero é menor")
        
        erros+=1
        jogador=int(input("Digite seu número: "))
        
print("Numero " + str(jogador) + ", você acertou em " + str(erros+1)  + " tentativas")