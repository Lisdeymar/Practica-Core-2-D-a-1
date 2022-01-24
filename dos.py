

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


