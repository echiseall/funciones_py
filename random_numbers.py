
import random 

## Genera numeros aleatorios en un rango deseado
def random_number(i=int(input("Ingrese un numero inicial:")),f=int(input("Ingrese un numero final:")),r=int(input("Ingrese el rango:"))):
  new = 0
  for x in range(r):
    old = new
    while old == new:
      new = random.randint(i,f)
    print(new)
  return

## MAIN CODE

print("Sus numeros son:")
random_number()
