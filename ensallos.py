#a aqui se iportan las librerias 
import tkinter as tk 
import webbrowser as we
import emoji
# se crea una clase
class App:

# definir metodos 
    def __init__(self, master):
#  aqui se inserta el titulo de la ventana 
        self.titulo = master
        master.title("Ejemplo de Programación Orientada a Eventos")
# botones
        
        self.label = tk.Label(master, text="Haz clic en cualquier botón para para vel el link")
        self.label.pack()
        spotify_emoji = emoji.emojize(":green_circle:")
        self.button = tk.Button(master, text=f"spotyfy wizarhub{spotify_emoji} ",command=self.abrir_url)
        self.button.pack()
        youtube_emoji = emoji.emojize(":red_circle:")
        self.button = tk.Button(master, text= f"youtube{youtube_emoji} ",command=self.abrir_url1)
        self.button.pack()
        
# Asociamos la función update_text al evento de hacer clic en el botón
    def abrir_url(self):
        url = "https://open.spotify.com/playlist/5qouHO5XTbEmCXu5D5t4DG?si=bee4b14356e64e75"  # Aquí puedes cambiar la URL deseada
        we.open(url)


        
    def abrir_url1(self):
        url = "https://www.youtube.com"  # Aquí puedes cambiar la URL deseada
        we.open(url)

        
    
  
    
#llamar la ventana 
root = tk.Tk()
#   crear intancia y ansignar la variable 
app = App(root)
# matener la ventana abierta 
root.mainloop()