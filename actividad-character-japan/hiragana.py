import tkinter as tk
import os
import random

imagenes_directorio = "imagenes"
imagenes = []

for nombrearchivo in os.listdir(imagenes_directorio):
    imagenes.append(nombrearchivo)

respuestas_correctas = 0
imagen_actual = None
respuesta_correcta = None
contador_imagenes=0

def mostrar_imagen():
    global imagen_actual, respuesta_correcta, contador_imagenes
    
    if contador_imagenes < 10:  

        imagen_actual = random.choice(imagenes)
        respuesta_correcta = os.path.splitext(imagen_actual)[0]  #1

        imagen_path=os.path.join("imagenes", imagen_actual)      #2
        imagen = tk.PhotoImage(file=imagen_path)                 #3
        label_imagen.config(image=imagen)
        label_imagen.image = imagen

        contador_imagenes += 1

    else:
        calcular_calificacion()
        root.destroy()


def comprobar_respuesta():
    global respuestas_correctas,calificacion
    respuesta_usuario = entrada_respuesta.get().lower()

    if respuesta_usuario == respuesta_correcta:
        respuestas_correctas += 1
        print("Correcto", "¡Respuesta correcta!")
    else:
        print("Incorrecto", f"La respuesta correcta es: {respuesta_correcta}")

    mostrar_imagen()
    calificacion=respuestas_correctas


def calcular_calificacion():
    global calificacion
    if calificacion < 5:
        calificacion_texto = f"Ha obtenido {calificacion} sobre 10. Suspenso"
    elif calificacion == 5:
        calificacion_texto = f"Ha obtenido {calificacion} sobre 10. Suficiente"
    elif calificacion == 6:
        calificacion_texto = f"Ha obtenido {calificacion} sobre 10. Bien"
    elif calificacion in (7, 8):
        calificacion_texto = f"Ha obtenido {calificacion} sobre 10. Notable"
    else:
        calificacion_texto = f"Ha obtenido {calificacion} sobre 10. Sobresaliente"

    print("Resultados", f"Tu calificación: {calificacion_texto}")



#-----------------------------#
root = tk.Tk()
root.title("Traduccion Hiragana")
root.config(height=300, bg="#f0f0f0")

label_imagen = tk.Label(root, bg="#f0f0f0")
label_imagen.pack()

entrada_respuesta = tk.Entry(root, width=5, borderwidth=0.5)
entrada_respuesta.pack()

boton_comprobar = tk.Button(root, text="Comprobar", command=comprobar_respuesta,bg="#4CAF50", font=("Arial", 12)) 
boton_comprobar.pack()

mostrar_imagen()

root.mainloop()


#1.bibliografia de os.path.splitext que use para poder coger el nombre del archivo sin la extension https://www.techiedelight.com/es/get-filename-without-extension-python/
#2.bibliografia de os.path.join que tuve que buscar para poder crear la ruta al directorio https://docs.python.org/es/3.8/library/os.path.html
#3.es para cargar la imagen desde la ruta que use antes https://programacionpython80889555.wordpress.com/2018/04/15/visualizando-imagenes-con-python-y-tkinter/ 
#Agregar que el orden en el que lo hice fue al reves es decir primero encontré la #3 y despues fui mirando como podia hacer lo demás

#Nota:No he podido hacer que no se repitiese ya que tarde mucho con otras cosas investigando etc y noi me dio tiempo