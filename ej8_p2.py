lista = []
letras_primas = []

string = input('Ingrese un string').lower()

string = string.replace(' ','')     #Sacamos espacios
letras_sin_repetir = set(string)

for l in letras_sin_repetir:
    lista.append (([l,string.count(l)]))
print(lista)

def es_primo (num):
    if (num <= 1):
        return False
    else:
        for i in range(2,num):
            if (num%i==0 and i != num):
                return False
        return True

aux = 0
for i in lista:
    ok = es_primo(lista[aux][1])
    if (ok == True):
        letras_primas.append(lista[aux][0])
    print('La letra ',lista[aux][0],' aparecio ',lista[aux][1],' veces')
    aux += 1
for y in letras_primas:
    dato = ' - '.join(letras_primas)
print('Las letras ',dato,' aparecieron un numero primo de veces')
