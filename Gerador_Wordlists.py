import itertools

string = input('Insera a palavra a ser permutada: ')

resultado = itertools.permutations(string, len(string)) #Faz a permutação dos caracteres na wordlist

for i in resultado:
    print(''.join(i))
