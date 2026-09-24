
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
#
# window = tk.Tk()
# window.title("OLA")
# button_widget = tk.Button(window, text="Welcome tkinter")
# button_widget.pack()
# tk.mainloop()

#Tem que ter sempre root = tk.Tk() e no final um mainloop()
# root = tk.Tk()
# root.title("Tk example")
# root.configure(background="White") # as cores e fontes de texto tem que estar em ""
# # root.minsize(200, 200)
# root.maxsize(600, 700)
# root.geometry("600x600+100+100")
#
# tk.Label(root, text="Nada vai funcionar a menos que tu tentes").pack()
# tk.Label(root, text="Jorge junior").pack()
#
# #Abrir imagem original
# image_pillow = Image.open("pokemon.jpg")
# #Redimensionar passando um tuple com (largura, altura)
# image_pillow_size = image_pillow.resize((400, 400), Image.Resampling.LANCZOS)
# image = ImageTk.PhotoImage(image_pillow_size)
#
# tk.Label(root, image=image).pack()
#
# root.mainloop()


#Tkinter widgets
root = tk.Tk()
root.title("Widget")
root.maxsize(1000, 1000)
root.geometry("700x700+300+300")

widgets = [
    tk.Label,
    tk.Checkbutton,
    ttk.Combobox, 
    tk.Entry,
    tk.Button,
    tk.Radiobutton,
    tk.Scale,
    tk.Spinbox,
]

for widget in widgets:
    try:
        widget = widget(root, text=widget.__name__)
    except tk.TclError:
        widget = widget(root)
    widget.pack(padx=30, pady=5, )

root.mainloop()
