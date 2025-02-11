import os
from appJar import gui
app=gui()

archivo_agenda = "agenda.txt"

def agregar_contacto():
    nombre= app.getEntry("Nombre")
    telefono = app.getEntry("Telefono")
    email = app.getEntry("Email")

    if len(nombre) == 0:
        app.errorBox("Error Nombre", "El nombre no debe de estar vacio")
        return
    
    if telefono == None:
        app.errorBox("Error Telefono", "El telefono no debe de estar vacio")
        return
    
    if len(email) == 0:
        app.errorBox("Error Email", "El email no debe de estar vacio")
        return

    with open(archivo_agenda,'a') as archivo:
        archivo.write(f"{nombre} - {telefono} - {email}\n")
    
    app.clearAllEntries()
    app.retryBox("Aviso", "Su contacto ha sido guardado")
    
def mostrar_contactos():
    if not os.path.exists(archivo_agenda):
        app.retryBox("Contactos", "No hay contactos")
        return
    
    with open(archivo_agenda,'r') as archivo:
        lineas = archivo.readlines()

    if not lineas:
        app.retryBox("Contactos lineas", "No hay contactos")
        return

    mensaje = ""
    for linea in lineas:
        mensaje = mensaje+linea

    app.addMessage("lista_contactos", mensaje)
                   
app.addLabel("Agenda de contactos")
app.addLabelEntry("Nombre")
app.setEntryUpperCase("Nombre")
app.addLabelNumericEntry("Telefono")
app.setEntryMaxLength("Telefono",10)
app.addLabelEntry("Email")
app.setEntryLowerCase("Email")

app.addButton("Guardar",agregar_contacto)
app.addButton("Mostrar",mostrar_contactos)

app.setFont(20)
app.addTable("g1",
    [["Name", "Age", "Gender"],
    ["Fred", 45, "Male"],
    ["Tina", 37, "Female"],
    ["Clive", 28, "Male"],
    ["Betty", 51, "Female"]])
app.go()

app.go()