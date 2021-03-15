from tkinter import*
root = Tk()

usuario= "Lit Killah"
Clave= "caminando por la street"
edad= 18

frame_usuario=Frame(root, width=400, height=200, bg="#F0E68C")
frame_usuario.grid(row=0, column=0)
frame_usuario_2= Frame(root, width=400, height=200, bg="#E6E6FA")
frame_usuario_2.grid(row=1, column=0)

def enviar_1():
    mensaje_emisor= mensaje_1.get()
    label_emisor.config(text=mensaje_emisor)
    label_emisor.grid(row=0, column=0)
    mensaje_1.delete(0,END)
def enviar_2():
    mensaje_receptor = mensaje_2.get()
    label_receptor.config(text=mensaje_receptor)
    label_receptor.grid(row=0, column=0)
    mensaje_2.delete(0, END)
root.mainloop()