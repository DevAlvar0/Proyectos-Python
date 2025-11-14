alumnos = [
    {'nombre': 'Álvaro', 'grupo': 'A', 'notas': [10, 10, 10], 'aprobado': False},
    {'nombre': 'Elías', 'grupo': 'B', 'notas': [3, 5, 8], 'aprobado': False},
    {'nombre': 'Izan', 'grupo': 'C', 'notas': [2, 2, 2], 'aprobado': False}
]

def añadirAlumno(nombre, grupo):
    if grupo not in ['A', 'B', 'C']: #TIENE QUE SER DE ALGUNO DE ESTOS 3 GRUPOS
        print('ERROR: El grupo solo puede ser A, B o C')
        return #SE CANCELA SI N0 ES DE NINGUN GRUPO

    if nombre == '':
        print('ERROR: Debe introducir un nombre no vacío.')
        return
    
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            print('ERROR: El alumno ya existe')
            return #SI EL ALUMNO YA EXISTÍA, SE CANCELA LA OPERACIÓN
    nuevoAlumno = {'nombre': nombre, 'grupo': grupo, 'notas': [], 'aprobado': False} #SI NO EXISTÍA, SE AÑADE
    alumnos.append(nuevoAlumno)
    print('ALUMNO AÑADIDO CORRECTAMENTE')


def buscarAlumno(nombre):
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            print('Alumno encontrado')
            nota = int(input('Ingrese una nueva nota para el alumno: ')) #FUERZO LA NOTA A UN ENTERO
            if( nota >= 0 and nota <= 10): #SI LA NOTA ESTÁ ENTRE 0-10, SE AÑADE
                alumno['notas'].append(nota)
                print('NOTA AÑADIDA CORRECTAMENTE')
                return
            else:
                print('NOTA INVÁLIDA')
                return
    print('ERROR: El alumno no existe')


def listarAlumnos():
    print('Lista de Alumnos:')
    print('NOMBRE - GRUPO - NOTAS - APROBADO')
    for alumno in alumnos:
        notaMedia = calcularMedia(alumno['nombre'])
        print(f'{alumno['nombre']} - {alumno['grupo']} - {alumno['notas']} - {notaMedia} - {'Aprobado' if alumno['aprobado'] else 'Suspenso'}')
        print('---------------------')


def eliminarAlumno(nombre):
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            print('Alumno encontrado')
            alumnos.remove(alumno)
            print('Alumno eliminado')
            return
    print('ERROR: El alumno no existe')


def calcularMedia(nombre):
    notaTotal = 0
    notaMedia = 0
    cantidadAsignaturas = 0
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            for nota in alumno['notas']:
                notaTotal += nota
                cantidadAsignaturas += 1
            notaMedia = notaTotal / cantidadAsignaturas
            if notaMedia >= 5:
                alumno['aprobado'] = True
    return notaMedia


def estadisticasGenerales():
    #INICIALIZACIÓN DE DATOS
    mediaPeor = 10 #SE INICIALIZA EN LA MAYOR NOTA POSIBLE PARA QUE LA COMPARACIÓN SEA EFECTIVA
    mediaMejor = 0 #SE INICIALIZA EN LA MENOR NOTA POSIBLE PARA QUE LA COMPARACIÓN SEA EFECTIVA
    cantidadAlumnos = 0
    mediaTotal = 0
    numeroAprobados = 0
    numeroSuspensos = 0
    porcentajeAprobados = 0

    for alumno in alumnos:
        cantidadAlumnos += 1 #POR CADA ALUMNO QUE EXISTA, SE INCREMENTA EN 1
        mediaAlumno = calcularMedia(alumno['nombre']) #OBTENER LA MEDIA DEL ALUMNO ACTUAL EN LA ITERACIÓN

        #LOGARITMO DE CÁLCULO DE MEJOR Y PEOR MEDIA
        if mediaAlumno > mediaMejor:
            mediaMejor = mediaAlumno

        if mediaAlumno < mediaPeor:
            mediaPeor = mediaAlumno

        mediaTotal += calcularMedia(alumno['nombre']) # "CONCATENAR" MEDIAS PARA SU POSTERIOR CÁLCULO

        #SI ESTÁ APROBADO, INCREMENTA APROBADOS, SINO, INCREMENTA SUSPENSOS
        if alumno['aprobado'] == True:
            numeroAprobados += 1

        else:
            numeroSuspensos += 1
    
    #IMPRESIÓN DE DATOS POR PANTALLA Y ÚLTIMOS CÁLCULOS
    porcentajeAprobados = (numeroAprobados * 100) / cantidadAlumnos #REGLA DE 3
    mediaTotal = mediaTotal / cantidadAlumnos
    print('Media total: ', mediaTotal)
    print('Cantidad de aprobados: ', numeroAprobados)
    print('Cantidad de suspensos: ', numeroSuspensos)
    print('Porcentaje de aprobados: ', porcentajeAprobados, '%')
    print('Peor media: ', mediaPeor)
    print('Mejor media: ', mediaMejor)
    print()


def main():
    while True:
        print('\nGestor de Tareas')
        print('1. Añadir alumno')
        print('2. Buscar alumno')
        print('3. Listar alumnos')
        print('4. Eliminar alumno')
        print('5. Estadisticas generales')
        print('0. Salir')
        opcion = input('Seleccione una opción (0-5): ')

        if opcion == '1': # Añadir tarea
            nombre = input('Ingrese el nombre del nuevo alumno: ')
            grupo = input('Ingrese el grupo del nuevo alumno: ')
            añadirAlumno(nombre, grupo)
            input('Presione Enter para continuar...')

        elif opcion == '2': #Buscar alumno
            nombre = input('Ingrese el nombre del alumno: ')
            buscarAlumno(nombre)
            input('Presione Enter para continuar...')
        
        elif opcion == '3': #Listar alumnos
            listarAlumnos()
            input('Presione Enter para continuar...')

        elif opcion == '4': #Eliminar alumno
            nombre = input('Ingrese el nombre del alumno a eliminar: ')
            eliminarAlumno(nombre)
            input('Presione Enter para continuar...')

        elif opcion == '5':
            estadisticasGenerales()
            input('Presione Enter para continuar...')

        elif opcion == '0': # Salir
            print('Saliendo del programa...')
            break

        else: # Opción no válida
            print('Opción no válida, por favor intente de nuevo.')
            input('Presione Enter para continuar...')

if __name__ == '__main__':
    main()