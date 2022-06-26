# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

print("****Introdução a Criptografia****")
print("****Criptografia de César****\n")

message = ("O sucesso é um professor perverso. Ele seduz as pessoas inteligentes e as faz pensar que jamais vão cair.")
message = message.lower()

key = int(input("Digite a chave de criptografia: "))

base = 'abcdefghijklmnopqrstuvwxyz'

cripto =''

while key > 26 or key < 0:  
    print(" ")
    key = input("Chave inválida, tente novamente")

for word in message:
  if word in base:
    posicion = base.index(word)
    cripto += base[(posicion+key)%len(base)]
  else:
    cripto += word

print("\nA mensagem original é: \n"+ message)
print("\nA mensagem criptografada é: \n" + cripto)
print()

commutes = pd.Series(list(cripto)).value_counts()

plt.title('Frequência de letras do texto cifrado')
plt.xlabel('Letras')
plt.ylabel('Frequência')
plt.grid(axis = 'y')
plt.bar(commutes.index,commutes, color='red', edgecolor='black')
plt.show()