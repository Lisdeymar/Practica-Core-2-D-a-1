#---------------------------------------------------------------------------
#Iterar a través de una lista de diccionarios

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterate_dictionary(list):
    for i in range(0, len(list)): #hasta acá como son 4 elementos me aparece del 0 al 3
        for key,values in list[i].items(): #hasta acá regresa lista de clave y valor
            print(f" {key} - {values}")

'''Llamando a la funcion'''
iterate_dictionary(estudiantes)


#valor de cada clave 'first_name'

def valorclave1(list):
    for i in range(0, len(list)): #hasta acá como son 4 elementos me aparece del 0 al 3
        for key,values in list[i].items(): #hasta acá regresa lista de clave y valor
            if key == 'first_name': #filta solo first_name
                print(values)


'''Llamando a la funcion'''
valorclave1(estudiantes)


#valor de cada clave 'last_name'
def valorclave2(list):
    for i in range(0, len(list)): #hasta acá como son 4 elementos me aparece del 0 al 3
        for key,values in list[i].items(): #hasta acá regresa lista de clave y valor
            if key == 'last_name': #filta solo last_name
                print(values)


'''Llamando a la funcion'''
valorclave2(estudiantes)


