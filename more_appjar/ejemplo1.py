from appJar import gui

app=gui()

def mostrar_pass():
    print
    
app.addEmptyLabel("el")
app.addSecretEntry("pass")
app.addButton("Mostrar", mostrar_pass)
app.go()