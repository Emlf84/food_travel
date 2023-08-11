import customtkinter
import json
import tkintermapview
import tkinter as tk
from funciones import *

usuario_principal= None



class Ventana1(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=("#607D8B"))
        

        self.prin= Principio(master=self,fg_color="#80A096")
        self.prin.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.prin.grid_rowconfigure(8, weight=1) 
        self.prin.grid_columnconfigure(0, weight=1)

        self.reg = Registro(master=self,fg_color="#80A096")
        self.reg.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.reg.grid_remove()
        self.reg.grid_rowconfigure(8, weight=1) 
        self.reg.grid_columnconfigure(0, weight=1)

        self.inicio = Login(master=self,fg_color="#80A096")
        self.inicio.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.inicio.grid_remove()
        self.reg.grid_rowconfigure(8, weight=1) 
        self.reg.grid_columnconfigure(0, weight=1)

            

    def mostrar_registro(self):
        self.prin.grid_remove()
        self.inicio.grid_remove()
        self.reg.grid()
    
    def mostrar_login(self):
        self.prin.grid_remove()
        self.reg.grid_remove()
        self.inicio.grid()
    
    def mostrar_principio(self):
        self.reg.grid_remove()
        self.inicio.grid_remove()
        self.prin.grid()
        

    def iniciar_nuevo_menu(self):
        self.destroy()
        menu= Ventana2()
        menu.mainloop()
        
    
        

class Registro(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        '''
        Registro
        '''
        self.nombre_label = customtkinter.CTkLabel(self, text= "Nombre: ",text_color="#1E1E23",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
        self.nombre_label.grid(row=5, column=0, padx=1,pady= (10, 0))
        self.nombre_label.place(relx=0.4, rely=0.23,anchor=customtkinter.CENTER)

        self.nombre_entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese su nombre", width= 200, height=35,text_color="#000000",fg_color="#607D8B",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.nombre_entry.place(relx=0.6, rely=0.23,anchor=customtkinter.CENTER)


        self.apellido_label = customtkinter.CTkLabel(self, text= "Apellido: ",text_color="#1E1E23",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
        self.apellido_label.grid(row=6, column=0, padx=1 ,pady=(10, 0))
        self.apellido_label.place(relx=0.4, rely=0.35,anchor=customtkinter.CENTER)

        self.apellido_entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese su apellido", width= 200, height=35,text_color="#000000",fg_color="#607D8B",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.apellido_entry.place(relx=0.6, rely=0.35,anchor=customtkinter.CENTER)


        self.password_label = customtkinter.CTkLabel(self,text="Contraseña: ",text_color="#1E1E23",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
        self.password_label.grid(row=7, column=0, padx=1, pady= (10, 0))
        self.password_label.place(relx=0.38, rely=0.47,anchor=customtkinter.CENTER)

        self.password_entry = customtkinter.CTkEntry(self,show="*", placeholder_text="Ingrese su contraseña", width= 200, height=35,text_color="#000000",fg_color="#607D8B",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.password_entry.place(relx=0.6, rely=0.47,anchor=customtkinter.CENTER)
       
        self.bt_reg= customtkinter.CTkButton(self, text="Guardar datos", command= self.guardar_datos,width= 300,height=50,
                                               text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#B45F04")
        self.bt_reg.place(relx=0.49, rely=0.63, anchor=customtkinter.CENTER)

        self.bt_atras= customtkinter.CTkButton(self,text="Atras", command= self.master.mostrar_principio,width= 300,height=50,
                                               text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#B45F04")
        self.bt_atras.place(relx=0.49, rely=0.8, anchor=customtkinter.CENTER)
        '''
        Fin registro
        '''
    def guardar_datos(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        password = self.password_entry.get()
        if len(nombre) > 2 or len(apellido) > 2 or len(password) > 3:
            registro('usuarios_registrados.json', nombre, apellido, password)
            self.master.mostrar_principio()         
        else:
            print("ingrese datos validos")


class Login(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        

        self.nombre_label = customtkinter.CTkLabel(self, text= "Nombre: ",text_color="#1E1E23",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
        self.nombre_label.grid(row=2, column=0, padx=1,pady= (10, 0))
        self.nombre_label.place(relx=0.4, rely=0.2,anchor=customtkinter.CENTER)
    

        self.nombre_entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese su nombre",text_color="#1E1E23",fg_color="#607D8B", width= 200, height=35,font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.nombre_entry.grid(row=2, column=0, padx=1,pady= (10, 0))
        self.nombre_entry.place(relx=0.6, rely=0.2,anchor=customtkinter.CENTER)


        self.password_label = customtkinter.CTkLabel(self, text= "Contraseña: ",text_color="#1E1E23",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
        self.password_label.grid(row=7, column=0, padx=1, pady= (10, 0))
        self.password_label.place(relx=0.37, rely=0.36,anchor=customtkinter.CENTER)

        self.password_entry = customtkinter.CTkEntry(self,show="*", placeholder_text="Ingrese su contraseña", width= 200, height=35,text_color="#1E1E23",fg_color="#607D8B",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.password_entry.place(relx=0.6, rely=0.36,anchor=customtkinter.CENTER)

        self.bt_inicio= customtkinter.CTkButton(self, text="Iniciar sesion",command=self.comprobacion, width= 300,height=50,
                                                text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#B45F04")
        self.bt_inicio.place(relx=0.49, rely=0.53,anchor=customtkinter.CENTER)

        self.bt_atras= customtkinter.CTkButton(self, text="Atras", command= self.master.mostrar_principio, width= 300,height=50,
                                               text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#B45F04")
        self.bt_atras.place(relx=0.49, rely=0.7, anchor=customtkinter.CENTER)
    
    def comprobacion(self):
        global usuario_principal
        nombre = self.nombre_entry.get()
        password = self.password_entry.get()
        usuario_encontrado= iniciar_sesion(nombre,password)
        if usuario_encontrado == None:
            print("usuario o contrseña incorrectos")
            
        else:
            usuario_principal= usuario_encontrado
            self.master.iniciar_nuevo_menu()
            print(usuario_principal)
            

class Principio(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bienv_label = customtkinter.CTkLabel(self, text= "Bienvenido",text_color="#000000", font=customtkinter.CTkFont("Roboto Condensed",size=35, weight="bold"))
        self.bienv_label.grid(row=0, column=0, padx=1, pady= 50)
        

        self.button= customtkinter.CTkButton(self, text="Iniciar sesion",
                                             text_color="#F6F1EE", 
                                             font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),
                                             command=self.master.mostrar_login, width= 300,height=50,fg_color="#B45F04")
        self.button.grid(row=1, column=0, padx=1, pady= 30)

        self.button2= customtkinter.CTkButton(self, text="Registrarse",text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"), command=self.master.mostrar_registro, width= 300,height=50,fg_color="#B45F04")
        self.button2.grid(row=2, column=0, padx=1, pady= 20)





















class Ventana2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.configure(fg_color=("#1E1E23"))

        self.lista_lugares = Destinoculinario.cargar_destinos(usuario_principal)


        self.mi_ruta=[]
        self.cargar_ruta()

        
        self.frame = customtkinter.CTkFrame(master=self,fg_color="#80A096")
        self.frame.pack(expand=True, fill="both", padx=13, pady=13)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        self.ventana_mapa = Mapa(self.frame,fg_color="#607D8B")
        self.ventana_mapa.grid(row=2, column=0, columnspan=3, padx=10, pady=(0,10), sticky="nsew")
        self.ventana_mapa.mostrar_lista()
        
        
        self.ventana_busqueda = Busqueda(self.frame,fg_color="#607D8B")
        self.ventana_busqueda.grid(row=2, column=0, columnspan=3, padx=10, pady=(0,10), sticky="nsew")
        self.ventana_busqueda.grid_remove()
        
        self.ventana_mi_lista = Miruta(self.frame,fg_color="#607D8B")
        self.ventana_mi_lista.grid(row=2, column=0, columnspan=3, padx=10, pady=(0,10), sticky="nsew")
        self.ventana_mi_lista.grid_remove()
        
        self.titulo = customtkinter.CTkLabel(master=self.frame, text="Food Travel",text_color="#000000", font=customtkinter.CTkFont("Roboto Condensed",size=35, weight="bold"))
        self.titulo.grid(row=0, column=0, padx=400, pady=10)

        self.menu = customtkinter.CTkSegmentedButton(self.frame, values=["Mapa", "Busqueda", "Mi ruta"], 
                                                     command=self.elegir_ventana,border_width=6,width= 140, height= 58,
                                                     fg_color="#B45F04",unselected_color="#B45F04",selected_hover_color="#38610B",selected_color=("#EB9736","#38610B"),text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
        self.menu.set("Mapa")
        self.menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    def guardar_ruta(self, usuario_principal):
        with open('usuarios_registrados.json', 'r') as f:
            lista_registrados = json.load(f)

        id_usuario = usuario_principal["id"]
        for datos in lista_registrados:
            if datos["id"] == id_usuario:
                datos["historial_ruta"] = usuario_principal["historial_ruta"]

        with open('usuarios_registrados.json', 'w') as f:
            json.dump(lista_registrados, f, indent=4)


    def elegir_ventana(self, opcion):
        opcion = self.menu.get()
        
        if opcion == "Mapa":
            self.ventana_mapa.grid()
            self.ventana_busqueda.grid_remove()
            self.ventana_mi_lista.grid_remove()

            

            self.ventana_mapa.mostrar_lista()
            
        elif opcion == "Busqueda":
            self.ventana_mapa.grid_remove()
            self.ventana_mi_lista.grid_remove()
            self.ventana_busqueda.grid()
            self.ventana_busqueda.buscar_lugar()

        elif opcion == "Mi ruta":
            self.ventana_mapa.grid_remove()
            self.ventana_busqueda.grid_remove()
            self.ventana_mi_lista.grid()

            self.cargar_ruta()
            self.ventana_mi_lista.mostrar_mi_ruta()
            

    def cargar_ruta(self):                                #DESCARTAR||||||||||||||||
        lugares= Destinoculinario.cargar_destinos(usuario_principal)
        for lugar in lugares:
            if lugar.id_destino in usuario_principal["historial_ruta"] and lugar not in self.mi_ruta:
                self.mi_ruta.append(lugar)

    def agregar_ruta(self,lugar):
        if lugar.id_destino in usuario_principal["historial_ruta"]:             #arreglado
            print("repetido")
        else:
            self.mi_ruta.append(lugar)
            usuario_principal["historial_ruta"].append(lugar.id_destino)
            with open('usuarios_registrados.json', 'r') as f:
                lista_registrados = json.load(f)

            id_usuario = usuario_principal["id"]
            for datos in lista_registrados:
                if datos["id"] == id_usuario:
                    datos["historial_ruta"] = usuario_principal["historial_ruta"]

            with open('usuarios_registrados.json', 'w') as f:
                json.dump(lista_registrados, f, indent=4)
            
    def eliminar_ruta(self,lugar):
        self.mi_ruta.remove(lugar)
        usuario_principal["historial_ruta"].remove(lugar.id_destino)
        self.guardar_ruta(usuario_principal)
        print()
        for label, button, button_2, button_3 in self.ventana_mi_lista.label_button_p:
            if label.cget("text") == lugar.nombre:
                label.destroy()
                button.destroy()
                button_2.destroy()
                button_3.destroy()
                                              #ARREGLAR|||||||||||||
        print(self.mi_ruta)

    

    def abrir_ventana(self, lugar):
        coord = lugar.ubicacion["coordenadas"]
        coord_x, coord_y = coord.split(", ")
        coord_x = float(coord_x)
        coord_y = float(coord_y)
        self.ventana_mapa.map_widget.set_position(coord_x, coord_y, text=lugar.nombre)
            
        inf = customtkinter.CTkToplevel(self)
        inf.title(lugar.nombre)
        inf.transient(self)  
        inf.geometry("700x500")
        inf.resizable(False, False)
        inf.rowconfigure(0, weight=1)
        inf.columnconfigure(1, weight=1)

        t_rv = customtkinter.CTkLabel(inf, text= "Reseñas",font=customtkinter.CTkFont(size=15, weight="bold"))
        t_rv.place(relx= 0.65, rely= 0.05)
        
        detalle_f = customtkinter.CTkFrame(master=inf)
        detalle_f.grid(row=0, column=0,sticky="nsew",padx=10, pady=(10,10),ipadx=50)
        detalle_f.rowconfigure(11, weight=1)
        detalle_f.columnconfigure(0, weight=1)
        if lugar.id_usuario == None:
            titulo = customtkinter.CTkLabel(detalle_f, text= "DETALLES DEL LUGAR",font=customtkinter.CTkFont(size=15, weight="bold"))
            titulo.grid(row=3, column=0, padx=1, pady= (20, 10))

            nombre = customtkinter.CTkLabel(detalle_f, text= f"{lugar.nombre}",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
            nombre.grid(row=4, column=0, padx=0, pady= (20, 10))

            t_cc = customtkinter.CTkLabel(detalle_f, text= "TIPO DE COCINA",font=customtkinter.CTkFont(size=15, weight="bold"))
            t_cc.grid(row=5, column=0, padx=0, pady= (10, 10))

            t_c = customtkinter.CTkLabel(detalle_f, text= f"{lugar.tipo_cocina}",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
            t_c.grid(row=6, column=0, padx=0, pady= (5, 5))

            t_in = customtkinter.CTkLabel(detalle_f, text= "INGREDIENTES",font=customtkinter.CTkFont(size=15, weight="bold"))
            t_in.grid(row=7, column=0, padx=0, pady= (10, 10))

            ing = customtkinter.CTkLabel(detalle_f, text= f"{lugar.ingredientes[0]}, {lugar.ingredientes[1]}, {lugar.ingredientes[2]}",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
            ing.grid(row=8, column=0, padx=0, pady= (10, 10))

            p_m = customtkinter.CTkLabel(detalle_f, text= "PRECIO MINIMO      PRECIO MAXIMO",font=customtkinter.CTkFont(size=15, weight="bold"))
            p_m.grid(row=9, column=0, padx=0, pady= (10, 10))

            pm = customtkinter.CTkLabel(detalle_f, text= f"{lugar.precio_minimo}$             {lugar.precio_maximo}$",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
            pm.grid(row=10, column=0, padx=0, pady= (10, 10))

            dir = customtkinter.CTkLabel(detalle_f, text= f"Direccion: {lugar.ubicacion['direccion']}",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
            dir.grid(row=11, column=0, padx=0, pady= (10, 10))
            
        else:
            nombre = customtkinter.CTkLabel(detalle_f, text= f"Lugar agregado por Usuario",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
            nombre.grid(row=3, column=0, padx=1, pady= (20, 10))

        rv_f = customtkinter.CTkScrollableFrame(master=inf)
        rv_f.grid(row=0, column=1,sticky="nsew",padx=10, pady=(70,10))
        rv_f.columnconfigure(0, weight=1)

        with open('reviews_creadas.json', 'r') as f:
            lista_reviews = json.load(f)
        l_rev =[]
        for rev in lista_reviews:
            if rev["id destino"] == lugar.id_destino:
                l_rev.append(rev)
                label = customtkinter.CTkLabel(rv_f, text=rev["comentario"], image=None, compound="center", padx=30, anchor="e", height=60, width=10,font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"))
                label.grid(row=len(l_rev), column=0, pady=(0, 10), sticky="w")
        if len(l_rev)==0:
            label = customtkinter.CTkLabel(rv_f, text="Este destino aun no tiene reseñas", image=None, compound="center", padx=30, anchor="e", height=60, width=10)
            label.grid(row=0, column=0, pady=(0, 10), sticky="w")


class Mapa(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        

        self.titulo = customtkinter.CTkLabel(self, text="Lista de lugares",text_color="#000000", font=customtkinter.CTkFont("Roboto Condensed",size=20, weight="bold")) 
        self.titulo.place(relx= 0.20, rely= 0.02)
        self.titulo = customtkinter.CTkLabel(self, text="Click derecho en el mapa para guardar una ubicacion",text_color="#000000", font=customtkinter.CTkFont("Roboto Condensed",size=20, weight="bold")) 
        self.titulo.place(relx= 0.02, rely= 0.9)

        self.map_widget= tkintermapview.TkinterMapView(self, corner_radius=0, width= 500)
        self.map_widget.grid(row=0, column=1,sticky="nsew",padx=10, pady=(10,10),ipadx= 500)
        self.map_widget.set_position(-24.727834140395917, -65.40757096102425)  
        self.map_widget.set_zoom(15)
        # comando al mapa||||||||||||||||
        self.map_widget.add_right_click_menu_command(label="Agregar esta ubicacion",
                                                     command=self.agregar_ubicacion,
                                                     pass_coords=True)

        self.lista_frame = customtkinter.CTkScrollableFrame(self, width=445,fg_color="#80A096")
        self.lista_frame.grid(row=0, column=0,sticky="nsew",padx=10, pady=(60,90),ipadx=28)
        self.lista_frame.rowconfigure(0, weight=1)
        self.lista_frame.columnconfigure(3, weight=1)

    
    def agregar_ubicacion(self, coords):
        self.cuadro = customtkinter.CTkToplevel() 
        self.cuadro.title("Agregar una ubicacion")
        self.cuadro.geometry("400x300")
        self.cuadro.transient(self)
        self.cuadro.resizable(False, False)
        self.cuadro.columnconfigure(0, weight=1)
        self.cuadro.rowconfigure(3, weight=1)
        

        self.coord_str = f"{coords[0]}, {coords[1]}"
#TERMINAR|||||||||||||||||||||
        if usuario_principal["nombre"] == "admin":
            self.cuadro.geometry("400x800")
            self.cuadro.rowconfigure(7, weight=3)
            

            self.nombre_lugar = customtkinter.CTkEntry(self.cuadro, placeholder_text="Nombre de ubicacion",width=300, height=50)
            self.nombre_lugar.grid(row=0,pady=20)

            self.tipo_c = customtkinter.CTkEntry(self.cuadro, placeholder_text="tipo de cocina",width=300, height=50)
            self.tipo_c.grid(row=1,pady=20)

            self.ingred = customtkinter.CTkEntry(self.cuadro, placeholder_text="ingredientes separados por coma sin espacios",width=300, height=50)
            self.ingred.grid(row=2,pady=20)

            self.precio_min = customtkinter.CTkEntry(self.cuadro, placeholder_text="precio minimo",width=300, height=50)
            self.precio_min.grid(row=3,pady=20)

            self.precio_max = customtkinter.CTkEntry(self.cuadro, placeholder_text="precio maximo",width=300, height=50)
            self.precio_max.grid(row=4,pady=20)

            self.img = customtkinter.CTkEntry(self.cuadro, placeholder_text="imagen url",width=300, height=50)
            self.img.grid(row=5,pady=20)

            self.dir = customtkinter.CTkEntry(self.cuadro, placeholder_text="direccion",width=300, height=50)
            self.dir.grid(row=6,pady=20)
        
            boton= customtkinter.CTkButton(self.cuadro, text="Guardar datos", command=self.guardar_datos_admin, width=250, height=40)
            boton.grid(row=7,pady=10)
            
        else:

            self.nombre_lugar = customtkinter.CTkEntry(self.cuadro, placeholder_text="Ingrese nombre de ubicacion",width=300, height=50)
            self.nombre_lugar.grid(row=0,pady=20)
        
            boton_d = customtkinter.CTkButton(self.cuadro, text="Guardar datos", command=self.guardar_datos, width=300, height=40)
            boton_d.grid(row=1,pady=10)

    def guardar_datos_admin(self):
        agregar_destino(nombre=self.nombre_lugar.get(), 
                        tipo_cocina= self.tipo_c.get(),
                        ingredientes=self.ingred.get(),
                        precio_minimo=int(self.precio_min.get()),
                        precio_maximo=int(self.precio_max.get()),
                        direccion=self.dir.get(),
                        coord=self.coord_str,
                        imagen=self.img.get())
        self.cuadro.destroy()
        self.mostrar_lista()

        

    def guardar_datos(self):
        nombre_lugar = self.nombre_lugar.get()
        if len(nombre_lugar) > 2:
            agregar_destino_usuario(nombre_lugar, self.coord_str,usuario_principal["id"])
        self.cuadro.destroy()
        self.mostrar_lista()


    def mostrar_lista(self):
        self.lista_lugares = Destinoculinario.cargar_destinos(usuario_principal)
        self.label_button_par = []
        self.marcadores= []

        for lugar in self.lista_lugares:
            item = lugar.nombre
            label = customtkinter.CTkLabel(self.lista_frame, text=item, image=None, compound="center", padx=30, anchor="e", height=60, width=10,text_color="#1e1e26",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
            button = customtkinter.CTkButton(self.lista_frame, text="Detalles", width=70, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#38610B")
            button.configure(command=lambda lugar=lugar: self.master.master.abrir_ventana(lugar))
            button_2 = customtkinter.CTkButton(self.lista_frame, text="Agregar a mi lista de ruta", width=50, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#BE7C4C")
            button_2.configure(command=lambda lugar=lugar: self.master.master.agregar_ruta(lugar))

            label.grid(row=len(self.label_button_par), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self.label_button_par), column=1, pady=(0, 10), padx=10)
            button_2.grid(row=len(self.label_button_par), column=2, pady=(0, 10), padx=10)
            self.label_button_par.append((label, button, button_2))

            # agrega marcadores |||||||||||||||||||||
            coord = lugar.ubicacion["coordenadas"]
            coord_x, coord_y = coord.split(", ")
            coord_x = float(coord_x)
            coord_y = float(coord_y)
            self.map_widget.set_marker(coord_x, coord_y, text=lugar.nombre)

        
    




class Busqueda(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Buscar lugar", width=300)
        self.entry.grid(column=5, pady=(10, 10),ipady= 15,row= 0,padx= 15)
    
        self.entry.bind("<KeyRelease>", lambda e: self.buscar_lugar(self.entry.get()))

        
        self.lista_lugares = Destinoculinario.cargar_destinos(usuario_principal)

        self.filtro_frame = customtkinter.CTkScrollableFrame(self,fg_color="#80A096")
        self.filtro_frame.grid(row=1, column=1, columnspan=5, padx=10, pady=(0,10), sticky="nsew")
        self.filtro_frame.grid_rowconfigure(1, weight=3)
        self.filtro_frame.grid_columnconfigure(1, weight=3)
    
    def buscar_lugar(self,entry=None):
        if entry== None or len(entry)<1:
            self.mostrar_lista(self.lista_lugares)
        else:
            self.lista_filtarda=[]
            for widgets in self.filtro_frame.winfo_children():            #Solucion||||||||||||||||||||||||
                print(widgets)
                widgets.destroy()
            for lugar in self.lista_lugares:
                if str(entry.lower()) in lugar.nombre.lower():
                    self.lista_filtarda.append(lugar)
            self.mostrar_lista(self.lista_filtarda)
            
            


    def mostrar_lista(self, lugares):
        self.label_button_m = []
        for lugar in lugares:
            item = lugar.nombre
            label = customtkinter.CTkLabel(self.filtro_frame, text=item, image=None, compound="center", padx=50, anchor="e", height=60, width=10,text_color="#1e1e26",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
            button = customtkinter.CTkButton(self.filtro_frame, text="Detalles", width=70, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#38610B")
            button.configure(command=lambda lugar=lugar: self.master.master.abrir_ventana(lugar))
            button_2 = customtkinter.CTkButton(self.filtro_frame, text="Agregar a mi lista de ruta", width=70, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#BE7C4C")
            button_2.configure(command=lambda lugar=lugar: self.master.master.agregar_ruta(lugar))

            label.grid(row=len(self.label_button_m), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self.label_button_m), column=1, pady=(0, 10), padx=10)
            button_2.grid(row=len(self.label_button_m), column=2, pady=(0, 10), padx=10)
            self.label_button_m.append((label, button, button_2))


        
        
    
class Miruta(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(1, weight=1)

        self.lista_frame = customtkinter.CTkScrollableFrame(self,fg_color="#80A096")
        self.lista_frame.grid(row=1, column=1, columnspan=5, padx=10, pady=(13,13), sticky="nsew")
        self.lista_frame.grid_rowconfigure(1, weight=3)
        self.lista_frame.grid_columnconfigure(0, weight=2)

    def mostrar_mi_ruta(self):
        self.lista_lugares = Destinoculinario.cargar_destinos(usuario_principal)
        self.label_button_p = []

        for lugar in self.master.master.mi_ruta:  
            label = customtkinter.CTkLabel(self.lista_frame, text=lugar.nombre, image=None, compound="center", padx=50, anchor="e", height=60, width=10,text_color="#1e1e26",font=customtkinter.CTkFont("Open Sans",size=20, weight="bold"))
            button = customtkinter.CTkButton(self.lista_frame, text="Detalles", width=90, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#38610B")
            button.configure(command=lambda lugar=lugar: self.master.master.abrir_ventana(lugar))
            button_2= customtkinter.CTkButton(self.lista_frame, text="Reseñar", width=90, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#BE7C4C")
            button_2.configure(command=lambda lugar=lugar: self.ventana_rv(lugar))
            button_3 = customtkinter.CTkButton(self.lista_frame, text="Eliminar", width=90, height=50,text_color="#F6F1EE",font=customtkinter.CTkFont("Open Sans",size=15, weight="bold"),fg_color="#e68b13")
            button_3.configure(command=lambda lugar=lugar : self.master.master.eliminar_ruta(lugar))

            label.grid(row=len(self.label_button_p), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self.label_button_p), column=1, pady=(0, 10), padx=30)
            button_2.grid(row=len(self.label_button_p), column=2, pady=(0, 10), padx=30)
            button_3.grid(row=len(self.label_button_p), column=3, pady=(0, 10), padx=30)
            self.label_button_p.append((label, button, button_2, button_3))
    
    def ventana_rv(self, lugar):
        self.vt_rv=customtkinter.CTkToplevel(self)
        self.vt_rv.title(f"Reseñar {lugar.nombre}")
        self.vt_rv.transient(self)  
        self.vt_rv.geometry("500x700")
        self.vt_rv.resizable(False, False)
        self.vt_rv.rowconfigure(20, weight=1)
        self.vt_rv.columnconfigure(0, weight=1)

        self.titulo_label = customtkinter.CTkLabel(self.vt_rv, text="Escriba una reseña", compound="center", padx=50, anchor="e", height=40, width=80)
        self.titulo_label.grid(row=3, column=0, padx=1, pady= (15, 10))

        self.calif_label = customtkinter.CTkLabel(self.vt_rv, text="Su calificaion", compound="center", padx=50, anchor="e", height=40, width=80)
        self.calif_label.grid(row=4, column=0, padx=1, pady= (15, 3))
        self.calif_entry = customtkinter.CTkEntry(self.vt_rv, placeholder_text="Calificacion del 1 al 5", width=200, height=40)
        self.calif_entry.grid(row=5, column=0, padx=1, pady= (3, 10))

        self.coment_label = customtkinter.CTkLabel(self.vt_rv, text="Escriba un comentario", compound="center", padx=50, anchor="e", height=40, width=80)
        self.coment_label.grid(row=6, column=0, padx=1, pady= (15, 3))
        self.coment_entry = customtkinter.CTkEntry(self.vt_rv, placeholder_text="Su comentario", width=200, height=40)
        self.coment_entry.grid(row=7, column=0, padx=1, pady= (3, 10))

        self.a_label = customtkinter.CTkLabel(self.vt_rv, text="Animo positivo o negativo?", compound="center", padx=50, anchor="e", height=40, width=80)
        self.a_label.grid(row=9, column=0, padx=1, pady= (15, 3))
        self.a_entry = customtkinter.CTkEntry(self.vt_rv, placeholder_text="Positivo o negativo?", width=200, height=40)
        self.a_entry.grid(row=10, column=0, padx=1, pady= (3, 10))

        self.bt_guardar= customtkinter.CTkButton(self.vt_rv, text="Guardar mi review",command=lambda: self.generar_review(lugar), width= 300,)
        self.bt_guardar.grid(row=13, column=0, padx=1, pady= (20, 10))
    
    def generar_review(self,lugar):
        calificacion = self.calif_entry.get()
        comentario = self.coment_entry.get()
        animo = self.a_entry.get()
        destino= lugar
        if len(calificacion)<1 or len(comentario)<4 or len(animo)<4:
            print("ingrese datos validos")
        else:    
            try:
                with open('reviews_creadas.json', 'r') as f:
                    lista_reviews = json.load(f)
            except:
                lista_reviews=[]
                with open('reviews_creadas.json', 'w') as f:
                    json.dump(lista_reviews, f)

            if len(lista_reviews) < 0:
                id_review= 0
            id_review = len(lista_reviews)+1
            id_destino = destino.id_destino
            id_usuario = usuario_principal["id"]
            #calificacion = int(input("Calificaion del 1 al 5: "))
            #comentario= input("Comentario: ")
            #animo= input("positivo o negativo: ")
            review = {
                "id review": id_review,
                "id destino": id_destino,
                "id usuario": id_usuario,
                "calificacion": calificacion,
                "comentario": comentario,
                "animo": animo
            }
            lista_reviews.append(review)

            with open('reviews_creadas.json', 'w') as f:
                json.dump(lista_reviews, f, indent=4)
                print(lista_reviews)
            self.vt_rv.destroy()

if __name__ == "__main__":
    app = Ventana1()
    app.mainloop()