from random import choice

vocabulario =["deveras", "daphne", "dezembro", "eletricidade", "complexo"]

palavra = choice(vocabulario)

print("Jogo da Forca 1.0\n")
print("Se prepare para a Forca\n")

chances = 6
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []

for letra in palavra: 
    print('_', end= ' ')
    
while True:
	print(tentativas)
	print("Chances: ",chances)

	for letra in palavra:
		if letra in tentativas:
			print(letra, end = ' ')
		else:
			print('_', end= ' ')

	palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
	if palpite == "sair":
		break	
	elif palpite not in alfabeto or palpite == '':
		print("Hein!? Fala direito! Isso não é uma letra!")
		continue	
	elif palpite in tentativas:
		print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
		continue
	tentativas.append(palpite)
	if palpite in palavra:
		print("ACERTÔ, MIZERAVI!")
	else:
		print("Errou feio, errou rude!")
      
    