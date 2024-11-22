from collections import deque

sepalavras=(input("palavras separadas: "))
pal=sepalavras.split()
palavras=deque()
for lt in pal:
    palavras.appendleft(lt)

print(palavras)

for i in range(len(palavras)):
    elt= palavras.pop()
    if "o" in elt:
        print(elt)