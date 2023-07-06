
i=0
new_string = []
frase = input('Digite uma frase: ') #A função input retorna sempre uma string
print(' Você digitou: {}'.format(frase))
for palavra in frase.split(" "):
    new_string += palavra

new_string = list(dict.fromkeys(new_string))
string = " "
for letra in new_string:
    if new_string[i] != " ":
        string += new_string[i]
        i = i + 1
    else :
        string += " "
        i = i +1
print(string)