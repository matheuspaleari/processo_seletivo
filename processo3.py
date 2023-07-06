# Expanda em ambas as direções de `low` e `high` para encontrar o palíndromo de comprimento máximo
def expand(s, low, high):
    length = len(s)

    # expande em ambas as direções
    while low >= 0 and high < length and s[low] == s[high]:
        low = low - 1
        high = high + 1

    # substring palindrômica de retorno
    return s[low + 1:high]


# Função para encontrar a substring palindrômica mais longa no tempo `O(n²)` e no espaço `O(1)`
def findLongestPalindromicSubstring(s):
    # caso básico
    if not s:
        return ''

    # `max_str` armazena a substring palindrômica de comprimento máximo encontrada até agora
    max_str = ''

    # `max_length` armazena o comprimento máximo de palindrômica
    # Substring # encontrada até agora
    max_length = 0

    # considera cada caractere da string dada como um ponto médio e expande
    # em ambas as direções para encontrar o palíndromo de comprimento máximo

    for i in range(len(s)):

        # encontre o palíndromo de comprimento ímpar mais longo com `s[i]` como ponto médio
        curr_str = expand(s, i, i)
        curr_length = len(curr_str)

        # atualiza a substring palindrômica de comprimento máximo se o comprimento ímpar
        # O palíndromo # tem um comprimento maior

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

        # Encontre o palíndromo de comprimento par mais longo com `s[i]` e `s[i+1]` como
        # pontos médios #. Observe que um palíndromo de comprimento par tem dois pontos médios.

        curr_str = expand(s, i, i + 1)
        curr_length = len(curr_str)

        # atualiza substring palindrômica de comprimento máximo se for de comprimento par
        # O palíndromo # tem um comprimento maior

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

    return max_str


if __name__ == '__main__':
    s = input("escreva uma palavra: ")

    print(findLongestPalindromicSubstring(s))