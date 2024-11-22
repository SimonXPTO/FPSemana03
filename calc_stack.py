from collections import deque

num = input("numeros inteiros separados: ")  
stack = deque()

numeros = num.split()

for i in numeros:
     a=int(i)
     stack.append(a)

print(stack)

for i in range(len(stack)):
     elt= stack.pop()
     print (int(elt) ** 2)