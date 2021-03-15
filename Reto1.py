from tkinter import*
root=Tk()
root.geometry("700x500")
root.configure(background="#E6E6FA")
root.title("reto 1")
root.bg="#E6E6FA"
frame_1=Frame(root,bg="#E6E6FA",width=750, height=600)
frame_1.grid(row=0, column=0)
titulo_app=Label(frame_1, text="Registro", font=("Times New Roman", 40), bg="#E6E6FA").place(x=200,y=0)


cedad=0 
usp=Entry(frame_1, width=10) 
usp.place(x=350, y=210)
csp=Entry(frame_1, width=10) 
csp.place(x=350, y=310)
et_edad=Label(frame_1, text="Ingrese su edad:", font=("Arial", 20), bg="#E6E6FA").place(x=150, y=100) 
edad=Entry(frame_1, width=10) 
edad.place(x=350, y=110)
et_us=Label(frame_1, text="Usuario:", font=("Arial", 20), bg="#E6E6FA").place(x=150, y=200) 
et_cs=Label(frame_1, text="Contraseña:", font=("Arial", 20),bg="#E6E6FA" ).place(x=150, y=300) 


def valid_edad(): 
    cedad=int(edad.get())
    if cedad>=18: 
        btn_usu_contra=Button(frame_1, text="INGRESAR",font=("Arial", 14),command=valid_usuario_y_contraseña).place(x=180, y=400)
        Label(root, text="",bg="#E6E6FA").place(x=180, y=200)
    else: 
        Label(root, text="Eres menor de edad y no puedes ingresar.(+18)", font=("Dashing Unicorn", 16)).place(x=10, y=60)
        edad.delete(0, END)


def valid_usuario_y_contraseña(): 
    cusuario=usp.get()
    ccontraseña=csp.get()
    if cusuario=="usuario" and ccontraseña=="2022":
        Label(root, text="Acceso Concedido",font=("Times New Roman", 14),bg="#E6E6FA").place(x=180, y=70)
    elif cusuario=="usuario" and ccontraseña!="2022":
        Label(root, text="Contraseña Incorrecta", font=("Times New Roman", 14), bg="").place(x=180, y=70)
    elif cusuario!="usuario" and ccontraseña=="2021":
        Label(root, text="Usuario Incorrecto", font=("Times New Roman", 14), bg="#E6E6FA").place(x=180, y=70)
    else: 
        Label(root, text="Ningún Dato Ingresado es Correcto", font=("Times New Roman", 14), bg="#E6E6FA").place(x=180, y=70)


btn_edad=Button(frame_1, text="Validar Edad", font=("Times New Roman", 14), command=valid_edad).place(x=180, y=148)
root.mainloop()