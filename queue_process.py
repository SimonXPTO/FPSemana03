from collections import deque

sepalavras=(input("palavras separadas: "))

palavras=deque(sepalavras.split())

print(palavras)

for i in palavras:
    if "o" in i:
        print(i)