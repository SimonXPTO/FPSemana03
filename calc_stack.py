from collections import deque

num = input("numeros inteiros separados: ")  


numeros = num.split()

stack = deque(numeros)

print(stack)

for i in range(len(stack)):
     elt= stack.pop()
     print (int(elt) ** 2)