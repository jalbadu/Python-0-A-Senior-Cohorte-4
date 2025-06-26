from prettytable import PrettyTable

# base de datos en memoria
libros = [
    {
        'isbn': '1',
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '2',
        'titulo': 'Rayuela',
        'autor': 'Julio Cortázar',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '3',
        'titulo': 'La sombra del viento',
        'autor': 'Carlos Ruiz Zafón',
        'estado': 'Prestado',
        'socio_prestado': 'Socio-003'
    },
    {
        'isbn': '4',
        'titulo': 'El nombre del viento',
        'autor': 'Patrick Rothfuss',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '5',
        'titulo': 'Ficciones',
        'autor': 'Jorge Luis Borges',
        'estado': 'Disponible',
        'socio_prestado': None
    }
]
socios = []
axuContador = 1

def mostrar_menu():
    '''Muestra las opciones de menu'''
    print(" MINIBIBLIOTECA ")
    print("1. Registrar Libro")
    print("2. Registrar un Socio")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Ver libros Pestados")
    print("6. Ver todos los Libros")
    print("7. Ver todos los Socios")
    print("0. Salir")

def registar_libro():
    global libros

    print("================================================================")
    print("Registrar Libros 📖")
    print("================================================================")
    print("Digite 0 si quiere cancelar la creacion")

    titulo = input("Título del libro: ").strip().lower()
    
    if titulo == "0":  return

    if not titulo:
        print("❌ El Título no puede estar vacío ❌")
        return

    autor = input("Autor del Libro: ").strip().lower()

    if autor == "0": return

    if not autor:
        print("❌ El Autor no puede estar vacío ❌")
        return

    isbn = input("ISBN del Libro: ").strip().lower()

    if isbn == "0": return

    if not isbn:
        print("❌ El ISBN no puede estar vacío ❌")
        return
    
    for libro in libros:
        if libro['isbn'] == isbn:
            print(f"❌ Ya existe un libro con el ISBN {isbn} ❌")

    #Crear el nuevo libro
    nuevo_libro = {
        'isbn': isbn,
        'titulo': titulo,
        'autor': autor,
        'estado': 'Disponible',
        'socio_prestado': None
    }

    # nuevo_libro_lista = [isbn,titulo,autor,'Disponible',None]

    libros.append(nuevo_libro)
    print("✅ Libro Registrado Exitosamente 📖")
    print(f"📚 {titulo} - {autor}")
    print(f"ISBN: {isbn}")

    print("================================================================")
    
    

def registar_socio():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def ver_libro_prestado():
    pass

def ver_todos_libros():

    table = PrettyTable()

    table.field_names = ["titulo", "autor", "isbn", "estado"]

    table.title = "📖 Mostrando Libros 📖"

    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])

    print(table)


    """
    print("================================================================")
    print("Mostrando todo los libros")
    print("================================================================")

    if not libros:
        print("No hay libros registrados en la biblioteca")
        return
    
    for i, libro in enumerate(libros, 1):
        print("================================================================")
        print(f"{i}. Nombre del Libro: {libro["titulo"]}")
        print(f"     Autor: {libro["autor"]}")
        print(f"     ISBN: {libro["isbn"]}")
        print(f"     Estado: {libro["estado"]}")
        print("================================================================")
    """

    

def ver_todo_socios():
    pass

def main():
    '''Funcion principal del programa'''
    while True:
        mostrar_menu()

        opcion = input("Seleccion una opción(0-7): ").strip()
        
        match opcion:
            case '1':
                registar_libro()
            case '2':
                pass # Tarea
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                ver_todos_libros()
            case '7':
                pass # Tarea
            case '0':
                print("📚 Gracias por usar MiniBiblio! 📚")
                print("📚 Hasta Luego 📚")
                break
            case _:
                print("Opcion no válida. Por favor, selecion una opción dek 0 al 7")

main()