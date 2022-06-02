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

#
