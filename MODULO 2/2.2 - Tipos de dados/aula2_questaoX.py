x = 5
y = 2
print (type (x))
print (type(y))

z = 5/2
print (z)
print (type (z))

r = "O resultado é"
a = 10
b = 3.5
c = a + b
print (r)
print (type (r))
print (a)
print (type (a))
print (b)
print (type(b))
print (c)
print (type(c))

v1 = 10
v2 = 20
aux = v1
v1 = v2
v2= aux
print ("valor em v1:" , v1)
print ("valor em v2:" , v2)

##juros = 1.01
##saldo = 500.0
##rendimento1 = saldo * juros
##rendimento2 = rendimento1 * juros
##rendimento3 = rendimento2 * juros
##print ("Após 3 meses meu novo saldo é")
##print (rendimento3)

juros = 1.01
rendimento = 500 * 1.01 * 1.01 * 1.01
print ("Após 3 meses meu novo saldo é" , rendimento)