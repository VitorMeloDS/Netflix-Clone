# n = [1,2,3,4,5]
# n.reverse()
# print(n)

# frase = input()

# frase_feita = set(frase)
# frase_ordenada = sorted(frase_feita)

# for palavra in reversed(frase_ordenada):
#     qtd = frase.count(palavra)
#     print(palavra, qtd)



# valor_acidez = int(input())

# if valor_acidez < 0 or valor_acidez > 14:
#     print("Digite o pH da solucao:\nValor deve estar entre 0 e 14.")
# elif valor_acidez > 7 and valor_acidez <= 14 :
#     print("Digite o pH da solucao:\nEssa solucao e acida.")
# elif valor_acidez == 7:
#     print("Digite o pH da solucao:\nEssa solucao e neutra.")
# elif valor_acidez < 7 and valor_acidez >= 0:
#     print("Digite o pH da solucao:\nEssa solucao e basica.")


# n = 2

# while n < 1000:
#     n*=2
# print(n)




possives_vg = {}

while True:
    cidades = input()
    if cidades == "Fim":
        break
    distancia = int(input())
    passagem = float(input())
    if passagem * 2 <=300:
        possives_vg[cidades] = distancia
    # cidades = input()
    
if len(possives_vg) == 0:
    print("SEM DESTINO")
    
else:
    viagem_longa = max(possives_vg.values())
    for lugar, preço in possives_vg.items():
        if viagem_longa == lugar:
            melhor_viagem = lugar.upper()
            print(melhor_viagem)
            break
