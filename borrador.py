#Ejercicio 2 ------------------------------------------------------------
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


print(estudiantes)
#[{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}, {'first_name': 'Mark', 'last_name': 'Guillen'}, {'first_name': 'KB', 'last_name': 'Tonel'}]


for i in estudiantes:
    print(i) #no se necesita imprimirlo porque con arriba ya tienes las respuesta print a

'''
{'first_name': 'Michael', 'last_name': 'Jordan'}
{'first_name': 'John', 'last_name': 'Rosales'}
{'first_name': 'Mark', 'last_name': 'Guillen'}
{'first_name': 'KB', 'last_name': 'Tonel'}
'''

#2. a)

for i in estudiantes: #itero en la lista estudiantes y obtengo los elementos de la lista con su respectivo {}, los elementos son 'i'
    for e in i:    #itero 'e' en los elementos {} y ahora estoy dentro de cada llave {}
        print (e, '-', i[e]) # 'e' es cada clave 'first_name' y 'last_name' 
#imprimo la clave, pongo coma, y coloco i[e] que es su respectivo valor ya que para obtener el 
#valor de la clave es diccionario[clave], entonces i es el dicc y 'e'es clave, entonces por eso resulta
'''
first_name - Michael
last_name - Jordan
first_name - John
last_name - Rosales
first_name - Mark
last_name - Guillen
first_name - KB
last_name - Tonel
'''
#Plus first_name - Michael, last_name - Jordan
for i in estudiantes:
    for e in i:
        if e == 'first_name':
            a=e
        else:
            b=e
    print(i[a],i[b])

'''
Michael Jordan
John Rosales  
Mark Guillen  
KB Tonel
'''

#Plus Valor first_name, valor last_name

for i in estudiantes:
    for e in i:
        if e == 'first_name':
            a=e
        else:
            b=e
    print(a,'-',i[a],',',b,'-',i[b])

'''
first_name - Michael , last_name - Jordan
first_name - John , last_name - Rosales
first_name - Mark , last_name - Guillen
first_name - KB , last_name - Tonel
'''



#2. b)
for i in estudiantes:
    for e in i:
        if e == 'first_name': #'e' es clave entonces filtro solo la clave first
            print (i[e])   #imprimo los valores de la clave first que he filtrado
'''
Michael
John
Mark
KB
'''
#2. c)
for i in estudiantes:
    for e in i:
        if e == 'last_name':
            print (i[e])

'''
Jordan
Rosales
Guillen
Tonel
'''


#Ejercicio 3 ------------------------------------------------------------

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#diccionario{clave: lista[valores]}

#3. a) valor de cada clave 'ubicaciones'

def ubicaciones(diccionario):
    for i in diccionario: #itero en el diccionario dojo, entonces hasta acá tengo clave: valor, el 'i' representa los valores que hay dentro que es clave:valor
        if i == 'ubicaciones':
            print (i.upper())  #Mayuscula a ubicaciones que es el i
            a = diccionario.get(i) #obtengo los valores de la clave i == 'ubicaciones', todos esos valores de ubicacion le llamo 'a'
            for e in a: #itero los valores para imprimirlo cada uno, 'e' son los elementos que obtengo de los valores ya que hice iteracion
                print(e) #imprimo solo los valores de ubicación

'''Mandamos a llamar a la funcion'''
ubicaciones(dojo)
'''
UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
'''

#3. b)valor de cada clave 'ubicaciones'

def instructores(diccionario):
    for i in diccionario:
        if i == 'instructores':
            print (i.upper())
            a = diccionario.get(i)
            for e in a:
                print(e)

'''Mandamos a llamar a la funcion'''
instructores(dojo)
'''
INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''