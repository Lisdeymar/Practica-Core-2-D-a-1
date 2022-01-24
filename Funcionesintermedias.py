#Listas Anidadas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]["last_name"] = 'Bryant'
print(estudiantes)

#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes["fútbol"][0] = "Andrés"
print(directorio_deportes)


#Cambia el valor 20 en z a 30

z[0]["y"]= 30
print( z )




estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#2)Iterar a través de una lista de diccionarios

for estudiante in estudiantes:
    print(estudiante)

# 3)Obtener valores de una lista de diccionarios

for i in range (0, len(estudiantes)):
    for clave,valor in estudiantes[i].items():
        if clave == "first_name":
            print(valor)


for i in range (0, len(estudiantes)):
    for clave,valor in estudiantes[i].items():
        if clave == "last_name":
            print(valor)


dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#4) Iterar a través de un diccionarios con valores de lista

for clave,valor in dojo.items():
    for i in range (0, len(valor)):
        if clave == "ubicaciones":
            print(valor[i])

for clave,valor in dojo.items():
    for i in range (0, len(valor)):
        if clave == "instructores":
            print(valor[i])


