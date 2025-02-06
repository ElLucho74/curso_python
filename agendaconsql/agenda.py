import sqlite3

conexion = sqlite3.connect("agenda.db")

cursor = conexion.cursor() #Ejecutar sentencias SQL

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS agenda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(15) NOT NULL,
        email VARCHAR(100)
        );
        '''
        
)
#Funcion para agregar un contacto

def agregar_contacto(nombre, telefono, email):
    cursor.execute(
        '''
        INSERT INTO agenda (nombre, telefono, email) VALUES (?, ?, ?);
        ''', (nombre, telefono, email)
    )
    conexion.commit()
    print("Contacto agregado correctamente")
    
#Funcion para mostrar los contactos
def mostrar_contactos():
    cursor.execute("SELECT * FROM agenda")
    contactos = cursor.fetchall()
    print("Lista de contactos")
    if contactos:
        for contacto in contactos:
            print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Telefono: {contacto[2]}, Email: {contacto[3]}")
    else:
        print("No hay contactos registrados")
       

#eliminar contacto
def eliminar_contacto(contacto_id):
    cursor.execute("DELETE FROM agenda WHERE id = ?", (contacto_id,))
    conexion.commit()
    print("Contacto eliminado correctamente")
    

#Actualizar contacto
def actualizar_contacto(contacto_id, nuevo_nombre, nuevo_telefono, nuevo_email):
    cursor.execute("UPDATE agenda SET nombre = ?, telefono = ?, email = ? WHERE id = ?", (nuevo_nombre, nuevo_telefono, nuevo_email, contacto_id))
    conexion.commit()
    print("Contacto actualizado correctamente")
    
    
    
#Buscar contacto
def buscar_contacto(nombre_buscar):
    cursor.execute("SELECT * FROM agenda WHERE nombre = ?", (nombre_buscar,))
    contacto = cursor.fetchall()
    if contacto:
        for c in contacto:
            print(f"ID: {c[0]}, Nombre: {c[1]}, Telefono: {c[2]}, Email: {c[3]}")
    else:
        print("Contacto no encontrado")
        
#Menu de seleccion 
while True:
    print("\n")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Eliminar contacto")
    print("4. Actualizar contacto")
    print("5. Buscar contacto")
    print("6. Salir")
    
    opcion = input("Selecciona una opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        agregar_contacto(nombre, telefono, email)
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        contacto_id = input("ID del contacto a eliminar: ")
        eliminar_contacto(contacto_id)
    elif opcion == "4":
        contacto_id = input("ID del contacto a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_telefono = input("Nuevo telefono: ")
        nuevo_email = input("Nuevo email: ")
        actualizar_contacto(contacto_id, nuevo_nombre, nuevo_telefono, nuevo_email)
    elif opcion == "5":
        nombre_buscar = input("Nombre del contacto a buscar: ")
        buscar_contacto(nombre_buscar)
    elif opcion == "6":
        break
    else:
        print("Opcion no valida")

            
conexion.close()
print("Programa finalizado")
    
    