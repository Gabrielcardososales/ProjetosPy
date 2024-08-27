import random
def jogar(lista):
    return random.choice(lista)

def analisar(lista, respostaMaquina):
    if(lista[0] == respostaMaquina or lista[1] == respostaMaquina):
        print("Você perdeu!!!")
    else:
        print("Você venceu!!!")

def resultado(resposta1, resposta2, opcoes):
    #Listas com os valores correspondente à sua perca
    listaPedra = ["papel", "spock"]
    listaPapel = ["tesoura", "lagarto"]
    listaTesoura = ["pedra", "spock"]
    listaSpock = ["papel", "lagarto"]
    listaLagarto = ["pedra", "tesoura"]
    #corresponde ao valor posicional de opções 
    listas = [listaPedra, listaPapel, listaTesoura, listaSpock, listaLagarto]

    #Verifica se resposta faz parte das opções
    if(resposta1 in opcoes):
        print(f"Resposta do jogador2: {resposta2}")
        if(resposta1 == resposta2):
            print("Empate!!")
    
        else:
            #O len pega o total de elementos, que não corresponde ao ultimo indice, por isso: -1
            #Então, tive que colocar item >= 0, para rodar o total, contando com 0 para isso
            item = len(opcoes) - 1
            while item >= 0:
                if(resposta1 == opcoes[item]):
                    analisar(listas[item], resposta2)
                item -= 1
    
    else:
        print("Opção invalida!!")

opcoes = ['pedra', 'papel', 'tesoura', 'spock', 'lagarto']
repetir = "sim"

print("{:^50}".format("BEM VINDO !!!"))
while (repetir == "sim"):
    print(""" Opções: 
        - pedra
        - papel 
        - tesoura
        - spock
        - lagarto """)

    escolha = input("\nQual sua escolha? ").lower()
    resultado(escolha, jogar(opcoes), opcoes)
    repetir = input("Deseja continuar? ").lower()