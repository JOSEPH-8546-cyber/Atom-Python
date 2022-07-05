##################
-
#usando .upper()
vq = "joseph blanco"
print(vq.upper())

#usando .lower()
vw = "Joseph Blanco"
print(vw.lower())

#usando .strip() para quitar espacios adelante o atras
ve = " joseph blanco "
print(ve.strip())

#usando .replace("","") para remplazar una cadena
vr = "Joseph Blanco"
print(vr.replace("Joseph", "Manuel"))

#usando .split(",") para devolver una lista
vt = "Joseph Blanco"
vy = vt.split(",")
print(vy)

#concatenacion con +
vu = "Hola "
vi = "Joseph"
vo = vu + vi

print(vo)

#usando .format() {}
vp = 21
va = "I am {} years old"
print(va.format(vp))

#usando varias veces format()
vs = 21
vd = "Joseph"
vf = "make code"
vg = "My name is {}, I'm {} years old and my favorite hobbie is {}"

print(vg.format(vd, vs, vf))

#usando format con indice
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#usando \ para colocar palabras entre comillas
vh = "Hola joseph Blanco alias \"Mr. White\"."
print(vh)

#usando booleanos
print(10 > 20) #False
print(8 == 5) #False
print(7 < 1) #True

#usando if y else
t = 52 + 7
p = 87 + 2

if p < t :
    print("hola joseph")
else :
    print("hola")

#ejemplo usando una clase para evaluar True or False
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#usando funciones para imprimir True or False
def myFuntion():
    return True

print(myFuntion)

#otro ejemplo de lo anterior
def myFuntion1():
    return True #False

if myFuntion1():
    print(◘)
else :
    print(♣)

#usando la funcion isinstance(var_name, type)
u = 200
print(isinstance(u, int))

#
