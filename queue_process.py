from collections import deque

sepalavras=(input("palavras separadas: "))

palavras=deque(sepalavras.split())

print(palavras)

for i in range(len(palavras)):
    elt= palavras.pop()
    if "o" in elt:
        print(elt)