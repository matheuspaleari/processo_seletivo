new_string = [""]
frase = input('Digite uma frase: ') #A função input retorna sempre uma string
print(' Você digitou: {}'.format(frase))
for palavra in frase.split(" "):
    new_string.append(palavra)
rev = list(reversed(new_string))
s = " ".join((rev))
print(rev)
print('A frase que você digitou invertida fica: {}'.format(s))