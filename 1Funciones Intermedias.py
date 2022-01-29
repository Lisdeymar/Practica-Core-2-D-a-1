#EJERCICIO 1) Actualizar valores en diccionarios y listas 

#1)----------------------------------------------------------
x = [ [5,2,3], [10,8,9] ] 

#tipo de datos Arreglo o listas de Listas
print(type(x))
#<class 'list'>

#1.Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#2)----------------------------------------------------------
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

#tipo de datos lista=[ diccionario{key:valor}]
print(type(estudiantes))
#<class 'list'>

#2.Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name']= 'Bryant'
print(estudiantes)

#3)----------------------------------------------------------
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

#tipo de datos Diccionario{key:[valor]}
print(type(directorio_deportes))
#<class 'dict'>

#3.En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0]= 'Andrés'
print(directorio_deportes)

#4)----------------------------------------------------------
z = [ {'x': 10, 'y': 20} ]
#tipo de datos lista=[ diccionario{key:valor}]
print(type(z))
#<class 'list'>

#4.Cambia el valor 20 en z a 30

z[0]['y']= 30
print(z)


#-------------------------------------------------------------------
#EJERCICIO 2) Iterar a través de una lista de diccionarios

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterar(lista):
    for i in lista:
        for e in i:
            print (e, '-', i[e])

'''Mandamos a llamar a la funcion'''
iterar(estudiantes)

#2. b)
def clave1(lista):
    for i in lista:
        for e in i:
            if e == 'first_name':
                print (i[e])

'''Mandamos a llamar a la funcion'''
clave1(estudiantes)

#2. c)
def clave2(lista):
    for i in lista:
        for e in i:
            if e == 'last_name':
                print (i[e])

'''Mandamos a llamar a la funcion'''
clave2(estudiantes)


#-------------------------------------------------------------------
#EJERCICIO 3) Iterar a través de un diccionarios con valores de lista

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#diccionario{clave: lista[valores]}

#valor de cada clave 'ubicaciones'

def ubicaciones(diccionario):
    for i in diccionario:
        if i == 'ubicaciones':
            print (i.upper())
            a = diccionario.get(i)
            for e in a:
                print(e)

'''Mandamos a llamar a la funcion'''
ubicaciones(dojo)


#valor de cada clave 'instructores'

def instructores(diccionario):
    for i in diccionario:
        if i == 'instructores':
            print (i.upper())
            a = diccionario.get(i)
            for e in a:
                print(e)

'''Mandamos a llamar a la funcion'''
instructores(dojo)

