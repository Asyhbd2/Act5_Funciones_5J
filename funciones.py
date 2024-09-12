print("Ejemplo de funciones")
# Declarando funciones
def hola():
    print("Alguien uso la funcion 'Hola'")
def chat(mensa):
    print(f"Chat: {mensa}") 
def ellacontesta(mensa):
    print(f"Chat: {mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s=a+b
    return s    

def resta(a,b):
    r=a-b
    return r

def multiplicacion(a,b):
    m=a*b
    return m

def division(a,b):
    d=a/b
    return d
# Llamadas a funciones
hola()
chat("Que bonita estas")
ellacontesta("Gracias")
escribenombre("De Leon Ceniceros","Angel Tadeo")

print("Operacion suma")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa un numero: "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c3=int(input("Ingresa un numero: "))
c4=int(input("Ingresa un numero: "))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion multiplicacion")
c5=int(input("Ingresa un numero: "))
c6=int(input("Ingresa un numero: "))
damemultiplicacion=multiplicacion(c5,c6)
print(f"La multiplicacion de {c5} x {c6} = {damemultiplicacion}")

print("Operacion division")
c7=float(input("Ingresa un numero: "))
c8=float(input("Ingresa un numero: "))
damedivision=division(c7,c8)
print(f"La division de {c7} / {c8} = {damedivision}")