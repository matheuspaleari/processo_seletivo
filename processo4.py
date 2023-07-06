
texto2 = ""
i = 0
input1 = input("insira uma frase")

texto = input1.split( ". ")
for palavra in texto:
    input1[0].capitalize()
    texto2 += texto[i].capitalize() +". "
    i += 1
print(texto2)
print(texto)
