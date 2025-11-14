tareas = [
    {'id': 1, 'titulo': 'Comprar leche', 'estado': False, 'prioridad': 'Baja', 'categoria': 'Casa'},
    {'id': 2, 'titulo': 'Estudiar para el examen', 'estado': False, 'prioridad': 'Alta', 'categoria': 'Estudios'}
]

def añadirTarea(descripcion, prioridad, categoria):
    id_mayor = 0
    nueva_tarea = []
    for tarea in tareas:
        if tarea['id'] > id_mayor:
            id_mayor = tarea['id']
    nueva_tarea = {'id': id_mayor + 1, 'titulo': descripcion, 'estado': False, 'prioridad': prioridad, 'categoria': categoria}
    tareas.append(nueva_tarea)
    print('Tarea añadida')
    print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
    imprimir(nueva_tarea)

def listarTareas():
    print('Lista de Tareas:')
    print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
    for tarea in tareas:
        imprimir(tarea)

def completarTarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            if tarea['estado']:
                print('La tarea ya está completada')
                return
            else:
                tarea['estado'] = True
                print('Tarea completada')
                print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
                imprimir(tarea)
                return
    print('Tarea no encontrada')

def eliminarTarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tareas.remove(tarea)
            print('Tarea eliminada')
            return
    print('Tarea no encontrada')

def editarTarea(id, nueva_descripcion, nueva_prioridad, nueva_categoria):
    for tarea in tareas:
        if tarea['id'] == id:
            if nueva_descripcion:
                tarea['titulo'] = nueva_descripcion
            if nueva_prioridad:
                tarea['prioridad'] = nueva_prioridad
            if nueva_categoria:
                tarea['categoria'] = nueva_categoria
            print('Tarea editada')
            print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
            imprimir(tarea)
            return
    print('Tarea no encontrada')

def filtrarPrioridad(prioridad):
    print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
    for tarea in tareas:
        if tarea['prioridad'] == prioridad.lower().capitalize():
            imprimir(tarea)

def filtrarCategoria(categoria):
    print('ID - TÍTULO - ESTADO - PRIORIDAD - CATEGORÍA')
    for tarea in tareas:
        if tarea['categoria'] == categoria.lower().capitalize():
            imprimir(tarea)
            

def resumenTareas():
    resumen = {} # Diccionario para almacenar el resumen por categoría
    for tarea in tareas:
        cat = tarea['categoria'] # Obtener la categoría de la tarea
        
        if cat not in resumen: # Si la categoría no está en el resumen, inicializarla
            resumen[cat] = {'total': 0, 'completadas': 0, 'pendientes': 0} # Inicializar el resumen para la categoría

        resumen[cat]['total'] += 1 # Incrementar el total de tareas en esa categoría
        if tarea['estado']: # Si la tarea está completada, incrementar el contador de completadas
            resumen[cat]['completadas'] += 1
        else: # Si la tarea está pendiente, incrementar el contador de pendientes
            resumen[cat]['pendientes'] += 1
    
    for categoria, datos in resumen.items(): # Imprimir el resumen por categoría
        print(f'Categoría: {categoria} - Total: {datos['total']}, Completadas: {datos['completadas']}, Pendientes: {datos['pendientes']}')
            

def imprimir(tarea):
    print(f'{tarea['id']} - {tarea['titulo']} - {'Completada' if tarea['estado'] else 'Pendiente'} - {tarea['prioridad']} - {tarea['categoria']}')

def main():
    while True:
        print('\nGestor de Tareas')
        print('1. Añadir tarea')
        print('2. Listar tareas')
        print('3. Completar tarea')
        print('4. Eliminar tarea')
        print('5. Editar tarea')
        print('6. Filtrar por prioridad')
        print('7. Filtrar por categoría')
        print('8. Resumen de tareas')
        print('0. Salir')
        opcion = input('Seleccione una opción (0-8): ')

        if opcion == '1': # Añadir tarea
            descripcion = input('Ingrese la descripción de la tarea: ')
            prioridad = input('Ingrese la prioridad de la tarea (Baja, Media, Alta): ').lower().capitalize()
            if prioridad not in ['Baja', 'Media', 'Alta']:
                print('Prioridad inválida. Debe ser "Baja", "Media" o "Alta".')
                input('Presione Enter para continuar...')
                continue
            categoria = input('Ingrese la categoría de la tarea (Casa, Estudios, Trabajo, Otros): ').lower().capitalize()
            if categoria.isdigit():
                print('Categoría inválida. Debe introducir texto.')
                input('Presione Enter para continuar...')
                continue
            añadirTarea(descripcion, prioridad, categoria)
            input('Presione Enter para continuar...')

        elif opcion == '2': # Listar tareas
            listarTareas()
            print('\n')
            input('Presione Enter para continuar...')

        elif opcion == '3': # Completar tarea
            try:
                id = int(input('Ingrese el ID de la tarea: '))
            except ValueError:
                print('ID inválido, debe ser un número entero.')
                input('Presione Enter para continuar...')
                continue
            completarTarea(id)
            input('Presione Enter para continuar...')

        elif opcion == '4': # Eliminar tarea
            try:
                id = int(input('Ingrese el ID de la tarea: '))
            except ValueError:
                print('ID inválido, debe ser un número entero.')
                input('Presione Enter para continuar...')
                continue
            eliminarTarea(id)
            input('Presione Enter para continuar...')

        elif opcion == '5': # Editar tarea
            try:
                id = int(input('Ingrese el ID de la tarea a editar: '))
            except ValueError:
                print('ID inválido, debe ser un número entero.')
                input('Presione Enter para continuar...')
                continue
            nueva_descripcion = input('Ingrese la nueva descripción (deje en blanco para no cambiar): ')
            nueva_prioridad = input('Ingrese la nueva prioridad (Baja, Media, Alta) (deje en blanco para no cambiar): ').lower().capitalize()
            if nueva_prioridad and nueva_prioridad not in ['Baja', 'Media', 'Alta']:
                print('Prioridad inválida. Debe ser "Baja", "Media" o "Alta".')
                input('Presione Enter para continuar...')
                continue
            nueva_categoria = input('Ingrese la nueva categoría (Casa, Estudios, Trabajo, Otros) (deje en blanco para no cambiar): ').lower().capitalize()
            if nueva_categoria and nueva_categoria.isdigit():
                print('Categoría inválida. Debe introducir texto.')
                input('Presione Enter para continuar...')
                continue
            editarTarea(id, nueva_descripcion, nueva_prioridad, nueva_categoria)
            input('Presione Enter para continuar...')

        elif opcion == '6': # Filtrar por prioridad
            prioridad = input('Ingrese la prioridad para filtrar (Baja, Media, Alta): ').lower().capitalize()
            if prioridad not in ['Baja', 'Media', 'Alta']:
                print('Prioridad inválida. Debe ser "Baja", "Media" o "Alta".')
                input('Presione Enter para continuar...')
                continue
            filtrarPrioridad(prioridad)
            print('\n')
            input('Presione Enter para continuar...')

        elif opcion == '7': # Filtrar por categoría
            categoria = input('Ingrese la categoría para filtrar (Casa, Estudios, Trabajo, Otros): ').lower().capitalize()
            if categoria.isdigit():
                print('Categoría inválida. Debe introducir texto.')
                input('Presione Enter para continuar...')
                continue
            filtrarCategoria(categoria)
            print('\n')
            input('Presione Enter para continuar...')

        elif opcion == '8': # Resumen de tareas
            resumenTareas()
            print('\n')
            input('Presione Enter para continuar...')

        elif opcion == '0': # Salir
            print('Saliendo del gestor de tareas...')
            break

        else: # Opción no válida
            print('Opción no válida, por favor intente de nuevo.')
            input('Presione Enter para continuar...')

if __name__ == '__main__':
    main()