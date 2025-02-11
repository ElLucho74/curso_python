from appJar import gui
import subprocess

def abrir_notepad():
    subprocess.Popen(["D:\SteamLibrary\steamapps\common\ELDEN RING\Game\eldenring.exe"])  

app = gui("Abrir Aplicación", "300x200")
app.addButton("Puchale aver", abrir_notepad)  # Botón que ejecuta la función
app.go()
