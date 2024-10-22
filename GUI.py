import tkinter as tk
from tkinter import ttk
from ejemplos import ganado
import functools
from datos import manejo_datos
"""
Ultimos cambios:
- Reorganizacion de panel de datos en forma
  de notebook.
- Ingreso de animales
Continuar con:
- Tab Machos
- Tab Hembras
- Boton Exportar
"""

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.state("zoomed")
        self.title("Ganado")
        self.config(background="#46665F",)
        self.styles()
        # Se establece los datos que se van a trabajar
        self.datos= manejo_datos(ganado)
        # Se establece el frame donde estara el menu y las demas opcines de la app
        self.menu_frame = ttk.Frame(self,style="menu.TFrame")
        self.menu_frame.pack(fill="y",side="left",ipadx=10)
        # Se establece el frame principal que cambiara dependiendo de la funcion a mostrar
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill="both",side="right",expand=True)
        self.menu()
        self.actualW = None
        self.Principal()
        
    def styles(self):
        # Definir los colores de la paleta
        color_primary = "#43BAA0"
        color_secondary = "#4C9182"
        color_accent = "#2CE6BD"
        color_background = "#46665F"
        color_dark = "#323B39"
        color_darker = "#283331"
        
        # Definir las fuentes de los textos
        font_default = ("Helvetica", 10)
        font_bold = ("Helvetica", 10, "bold")
        font_large = ("Helvetica", 12)
        font_title = ("Helvetica", 14, "bold")
        # Especial fonts
        home = ("Helvetica", 16)
        home_bold = ("Helvetica", 16, "bold")

        # Crear un estilo ttk
        style = ttk.Style()

        # Establecer el tema para el estilo
        style.theme_use("clam")
        
        # Casos Especiales
        style.configure("menu.TFrame",background=color_primary)
        
        # General Frame
        style.configure("TFrame", background=color_background)
        
        # Configura el estilo para el Notebook
        style.configure("TNotebook", background=color_background, borderwidth=2)
        style.configure("TNotebook.Tab", 
                        background=color_background,
                        foreground=color_dark, 
                        padding=[10, 5], 
                        font=("Arial", 10, "bold"),
                        focuscolor=color_primary)
        
        # Configura el estilo cuando una pestaña está seleccionada
        style.map("TNotebook.Tab", 
                background=[("selected", color_primary)], 
                foreground=[("selected", color_darker)])

        # Ajusta el padding de las pestañas y el borde de las pestañas seleccionadas
        style.configure("TNotebook.Tab", padding=[10, 5])

        # Treeview
        style.configure("Treeview",
                        background=color_darker,
                        foreground="white",
                        fieldbackground=color_dark,
                        bordercolor=color_secondary,
                        relief="flat",
                        font=font_default)

        style.map("Treeview", background=[('selected', color_primary)])

        # Treeview Heading
        style.configure("Treeview.Heading",
                        background=color_primary,
                        foreground=color_dark,
                        relief="flat",
                        font=font_bold,)

        # Treeview Separator
        style.configure("Treeview.Separator", background=color_secondary)
        
        # Treeview Home Window
        style.configure("Home.Treeview",
                        rowheight=30,
                        font=home)
        style.configure("Home.Treeview.Heading",
                        font=home_bold)

        # Botón principal
        style.configure("TButton",
                        background=color_primary,
                        foreground=color_darker,
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor=color_primary,
                        font=font_bold)

        style.map("TButton", background=[('active', color_secondary)])
        style.map("TButton", focuscolor=[('active', color_secondary)])
        style.map("TButton", foreground=[('disabled', color_dark)])
        
        # Botones CRUD
        style.configure("listado.TButton",
                        background=color_primary,
                        foreground=color_dark,
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor=color_primary,
                        font=font_bold)

        style.map("listado.TButton", background=[('active', color_secondary),("disabled",color_darker)])
        style.map("listado.TButton", focuscolor=[('active', color_secondary),("disabled",color_darker)])
        style.map("listado.TButton", foreground=[('disabled', color_dark)])

        # Entry (campo de texto)
        style.configure("TEntry",
                        fieldbackground=color_dark,
                        foreground="white",
                        borderwidth=1,
                        relief="flat",
                        font=font_default)
        style.map("TEntry",fieldbackground=[("disabled","#222B2A")])
        
        # LabelFrame
        style.configure("TLabelFrame",
                background=color_background,
                foreground=color_primary,
                relief="groove",
                font=font_large)

        style.configure("TLabelFrame.Label",
                background=color_background,
                foreground=color_accent,
                font=font_title)
        # Label
        style.configure("TLabel",
                        background=color_background,
                        foreground="white",
                        padding=5,
                        font=font_bold)
        style.configure("Principal.TLabel",
                        background=color_primary,
                        foreground="white",
                        padding=5,
                        font=font_bold)

        # OptionMenu
        style.configure("TMenubutton",
                        background=color_secondary,
                        foreground="white",
                        borderwidth=0,
                        font=font_default)

        style.map("TMenubutton", background=[('active', color_primary)])

        # Combobox
        style.configure("TCombobox",
                        fieldbackground=color_darker,
                        background=color_secondary,
                        foreground="white",
                        arrowcolor=color_primary)

        # Radiobutton
        style.configure("Toolbutton",
                        background=color_background,
                        foreground="white",
                        indicatorcolor=color_primary,
                        )
        style.map('Toolbutton', background=[('selected', color_dark),
                                            ('!selected', color_background)])
                                                
        # Menú
        style.configure("TMenu",
                        background=color_background,
                        foreground="white",
                        relief="flat")
         
    def menu(self):
        # Se establecen los iconos de cada opcion del menu
        self.home_imagen = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\casa.png")
        self.menu_imagen = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\aplicaciones.png")
        self.data_imagen = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\bases-de-datos.png")
        self.analisis_imagen = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\gestion.png")
        self.config_imagen = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\configuraciones.png")
        # Funciones que expanden y retraen el menu recorriendo cada elemento hijo del frame
        def retraer():
            abrir_menu.configure(command=expandir)
            for boton in self.menu_frame.winfo_children():
                boton.configure(compound="none")
        def expandir():
            abrir_menu.configure(command=retraer)
            for boton in self.menu_frame.winfo_children():
                boton.configure(compound="left")
        # Se definen y muestran los botones del menu con sus respectivos eventos
        def crear_boton(imagen, texto):
            boton = ttk.Button(self.menu_frame, image=imagen, text=texto,)
            #boton.config(highlightthickness=0, borderwidth=0, takefocus=False)  # Eliminar el focus ring
            return boton
        abrir_menu = crear_boton(self.menu_imagen,"  Menu")
        abrir_menu.config(command=expandir)
        abrir_menu.pack(side="top",pady=8)
        boton_home = crear_boton(self.home_imagen,"  Home")
        boton_home.config(command=self.Principal)
        boton_home.pack(side="top",pady=8)
        boton_data = crear_boton(self.data_imagen,"  Datos")
        boton_data.config(command=self.Datos)
        boton_data.pack(side="top",pady=8)
        boton_analisis = crear_boton(self.analisis_imagen,"  Analisis")
        #boton_analisis.config(command=self.Datos)
        boton_analisis.pack(side="top",pady=8)
        boton_ajustes= crear_boton(self.config_imagen,"  Configurar")
        #boton_ajustes.config(command=self.Datos)
        boton_ajustes.pack(side="bottom",pady=8)
    
    # Funcion que crea dataframes
    def dataframes(self,root, tam, datos,act,delete):
            # Obtiene las llaves de los diccionarios de datos
            columns = list(datos[0].keys())
            
            # Define frame del treeview y scrollbar
            frame = ttk.Frame(root)
            frame.pack(fill="x")
            # Define el Treeview con las columnas correspondientes
            listado = ttk.Treeview(frame, columns=columns, show="headings", height=tam)

            # Función que ordena el Treeview por columna
            def sort_by_column(column_name, reverse=False):
                try:
                    column_index = listado["columns"].index(column_name)
                    sorted_items = sorted(
                        ((listado.item(item)["values"][column_index], item) for item in listado.get_children()),
                        key=lambda x: (x[0] is None, x[0]),  # Manejar valores None en el ordenamiento
                        reverse=reverse
                    )
                    for index, (_, item) in enumerate(sorted_items):
                        listado.move(item, '', index)

                    listado.heading(column_name, command=functools.partial(sort_by_column, column_name, not reverse))
                except Exception as e:
                    print(f"Error al ordenar columna: {e}")

            # Crear las columnas y los encabezados
            for column in columns:
                listado.column(column, anchor="center", width=len(column) + 100)  # Ajustar el ancho de forma más flexible
                listado.heading(column, text=column, command=lambda col=column: sort_by_column(col))

            # Insertar los datos en el Treeview
            for animal in datos:
                try:
                    # Usa las claves del diccionario de forma dinámica
                    listado.insert("", tk.END, values=[animal[col] for col in columns])
                except KeyError as e:
                    print(f"Error en los datos: columna no encontrada {e}")
                except Exception as e:
                    print(f"Error al insertar datos: {e}")

            # Función para habilitar botones cuando se selecciona un ítem
            def habilitar_botones(btn1,btn2):
                try:
                    if btn1 != None:
                        btn1.config(state="normal")
                    if btn2 != None:
                        btn2.config(state="normal")
                except NameError:
                    print("Botones 'upd_btn' o 'del_btn' no definidos.")
            
            if act != None or delete !=None:        
                listado.bind("<<TreeviewSelect>>", lambda *args :habilitar_botones(act,delete))
            

            # Scrollbar vertical
            verscrlbar = ttk.Scrollbar(frame, orient="vertical", command=listado.yview)
            verscrlbar.pack(side='right', fill='y', padx=(0, 10))
            listado.configure(yscrollcommand=verscrlbar.set)

            listado.pack(expand=True, fill='both')

            return listado
        
    def Entry(self):
        """
        Ventana para ingreso y registro de cada animal
        -Formulario
        -Listado de registros agregados
        """
        
        def crea_entry(frame, row, col, variable, default):
            # Asignamos el valor por defecto a la variable antes de crear el Entry
            menu = ttk.Entry(frame)
            menu.grid(row=row, column=col, padx=2, pady=2, sticky="w")
            
            # Insertamos el valor por defecto en el Entry
            menu.insert(0,default)
            
            return menu

        # Crea un filtro a partir de ciertos parámetros
        def crear_option_menu(frame, row, col, variable, opciones):
            menu = ttk.OptionMenu(frame, variable, opciones[0], *opciones)
            menu.grid(row=row, column=col, padx=2, sticky="w")
            return menu
        
        # Función que deshabilita el OptionMenu y habilita el Entry si la opción es "Otro"
        def verificar_opcion(variable, entry, variable_2):
            if variable.get() == "Otro":
                entry.config(state="normal")  # Habilita el Entry
            else:
                entry.delete(0,tk.END)
                entry.config(state="disabled")
                
        def seleccionar_texto(entry):
            entry.select_range(0, tk.END)  # Selecciona todo el texto en el Entry
            entry.focus_set()  # Asegura que el Entry tiene el foco
            
        # Enlazamos la funcion de llenado default para cada variable 
        def on_focus_in(entry, default):
            if entry.get() == default:
                entry.delete(0, tk.END)  # Limpiar el texto

        def on_focus_out(entry, default):
            if entry.get() == "":  # Si está vacío, restaurar el valor predeterminado
                entry.insert(0, default)
                
        entryw = tk.Toplevel()
        entryw.title("Ingreso")
        entryw.config(background="#46665F")
        registro = tk.LabelFrame(entryw, text="Registro", background="#46665F", foreground="white")
        registro.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")
        ingresos = tk.LabelFrame(entryw, text="Observaciones", background="#46665F", foreground="white")
        ingresos.grid(row=1, column=1, padx=5, pady=5, sticky="NSEW")

        # Variables
        marca = tk.StringVar()
        otra_marca =tk.StringVar(value="")
        sexo = tk.StringVar()
        dia = tk.StringVar()
        mes = tk.StringVar()
        anio = tk.StringVar()
        nacimiento = tk.StringVar(value=f"{dia.get()}/{mes.get()}/{anio.get()}")
        peso = tk.StringVar()
        raza = tk.StringVar()
        otra_raza =tk.StringVar(value="")
        finca = tk.StringVar()
        otra_finca = tk.StringVar()
        salud = tk.StringVar()
        observaciones = tk.StringVar()
        #reg = [marca, peso, nacimiento, raza, sexo, corral, salud]
        
        # Etiquetas
        labels1 = ["Marca", "Nacimiento", "Raza", "Salud"]
        labels2 = ["Sexo", "Peso", "Finca"]

        for index, label in enumerate(labels1):
            ttk.Label(registro, text=f"* {label} : ", anchor="e", justify="right").grid(row=index + 1, column=1,sticky="e")
        
        for index, label in enumerate(labels2):
            ttk.Label(registro, text=f"* {label} : ", anchor="e", justify="right").grid(row=index + 1, column=5,sticky="e")

                
        # Opciones de marca y raza
        opc_marca = ["NA"]
        opc_marca.extend(sorted(list(manejo_datos(ganado).marcas)))
        opc_marca.append("Otro")
        
        opc_raza = ["NA"]
        opc_raza.extend(sorted(list(manejo_datos(ganado).razas)))
        opc_raza.append("Otro")

        opc_salud = ["Saludable","Herido","Enfermo"]
        
        opc_finca=sorted(list(self.datos.corrales))
        opc_finca.append("Otro")
        
        # Marca
        crear_option_menu(registro, 1, 2, marca, opc_marca)
        marca_otro_entry =crea_entry(registro,1,3,otra_marca,"")
        marca_otro_entry.config(state="disabled")
        
        # Nacimiento
        nacimientoEntry = ttk.Frame(registro)
        nacimientoEntry.grid(row=2,column=2,columnspan=2,sticky="w")
        
        dia_entry =crea_entry(nacimientoEntry,0,0,dia,"DD")
        dia_entry.config(width=8)
        
        ttk.Label(nacimientoEntry,text="/").grid(row=0,column=1)
        mes_entry =crea_entry(nacimientoEntry,0,2,mes,"MM")
        mes_entry.config(width=8)
        
        ttk.Label(nacimientoEntry,text="/").grid(row=0,column=3)
        anio_entry =crea_entry(nacimientoEntry,0,4,anio,"AAAA")
        anio_entry.config(width=8)
        
        # Capturar datos en variable
        dia.set(dia_entry.get())
        mes.set(mes_entry.get())
        anio.set(anio_entry.get())
        
        # Enlazar eventos de focus in/out
        dia_entry.bind("<FocusIn>", lambda event: on_focus_in(dia_entry, "DD"))
        dia_entry.bind("<FocusOut>", lambda event: on_focus_out(dia_entry, "DD"))

        mes_entry.bind("<FocusIn>", lambda event: on_focus_in(mes_entry, "MM"))
        mes_entry.bind("<FocusOut>", lambda event: on_focus_out(mes_entry, "MM"))

        anio_entry.bind("<FocusIn>", lambda event: on_focus_in(anio_entry, "AAAA"))
        anio_entry.bind("<FocusOut>", lambda event: on_focus_out(anio_entry, "AAAA"))
        
        # Raza
        crear_option_menu(registro, 3, 2, raza, opc_raza)
        raza_otro_entry =crea_entry(registro,3,3,otra_raza,"")
        raza_otro_entry.config(state="disabled")
        
        # Salud
        crear_option_menu(registro,4,2,salud,opc_salud)
    
        # Separador
        ttk.Separator(registro,orient="vertical").grid(row=1,column=4,rowspan=3,padx=30,sticky="NES")
        
        # sexo
        opc_sexo=["Macho","Hembra"]
        crear_option_menu(registro,1,6,sexo,opc_sexo)
        
        # Peso
        peso_default = str(self.datos.peso_promedio)
        peso_entry = crea_entry(registro,2,6,peso,peso_default)
        peso_entry.config(width=8,justify="center")
        peso_entry.bind("<FocusIn>", lambda event: seleccionar_texto(peso_entry))
        
        # Finca
        crear_option_menu(registro,3,6,finca,opc_finca)
        finca_otro_entry = crea_entry(registro,3,7,otra_finca,"")
        finca_otro_entry.config(state="disabled")
        
        # Observaciones
        color_dark = "#323B39"
        font_default = ("Helvetica", 10)
        obs_frame = tk.LabelFrame(registro, text="Observaciones", background="#46665F", foreground="white")
        obs_frame.grid(row=4,column=3,columnspan=5,rowspan=2, sticky="NSEW")
        obs_entry= tk.Text(obs_frame,background=color_dark,font=font_default,foreground="white",height=3)
        obs_entry.pack(fill="both")
        
        # Enlazamos los cambios de selección a la función verificar_opcion
        marca.trace_add("write", lambda *args: verificar_opcion(marca, marca_otro_entry,otra_marca))
        raza.trace_add("write", lambda *args: verificar_opcion(raza, raza_otro_entry,otra_raza))
        finca.trace_add("write", lambda *args: verificar_opcion(finca, finca_otro_entry,otra_finca))
        
        # Botones de ingresar y exportar
        ttk.Button(registro,text="Ingresar").grid(row=4,column=9,padx= 20)
        ttk.Button(registro,text="Exportar").grid(row=5,column=9,padx= 20)
        act = ttk.Button(registro,text="Actualizar",state="disabled",style="listado.TButton")
        act.grid(row=4,column=10,padx= 20)
        delete= ttk.Button(registro,text="Eliminar",state="disabled",style="listado.TButton")
        delete.grid(row=5,column=10,padx= 20)
        
        # TABLA DE DATOS INGRESADOS
        lista_filtros= ["" ,"-Seleccionar-", "7", "-Seleccionar-", "-Seleccionar-","-Seleccionar-", "-Seleccionar-", "-Seleccionar-","-Seleccionar-"]
        ingresados = self.datos.filtros(lista_filtros)
        tabla = self.dataframes(ingresos,10,ingresados,act,delete)
        tabla.pack(fill="both")
        
    def tab_general(self,notebook):
        # Frame Tab-General
        tabGeneral = ttk.Frame(notebook)
        
        # Definir botones de actualizar y eliminar registros
        btn_frame = ttk.Frame(tabGeneral)
        upd_btn = ttk.Button(btn_frame,text="Actualizar",state="disabled",style="listado.TButton",width=20)
        del_btn = ttk.Button(btn_frame,text="Eliminar",state="disabled",style="listado.TButton",width=20)
        # Se muestra el listado 
        listado = self.dataframes(tabGeneral,35,self.datos.values_filtrados,upd_btn,del_btn)
        listado.pack(fill="both",padx=8,pady=8)
        
        # BOTONES CRUD
        # Frame de los botones
        btn_frame.pack(side="right",fill="y",padx=20)
        # Botones de Agregar,Actualizar y Eliminar
        add_btn = ttk.Button(btn_frame,text="Agregar",style="listado.TButton",width=20,command=self.Entry)
        export_btn = ttk.Button(btn_frame,text="Exportar",style="listado.TButton",width=20)
        add_btn.pack(side="right",anchor="n",padx=2,pady=(2,8))
        upd_btn.pack(side="right",anchor="n",padx=2,pady=(2,8))
        del_btn.pack(side="right",anchor="n",padx=2,pady=(2,8))
        export_btn.pack(side="right",anchor="n",padx=2,pady=(2,8))
        
        # -Variables
        def default_vars():
            self.marca = tk.StringVar()
            self.peso = tk.StringVar()
            self.edad = tk.StringVar()
            self.nacimiento = tk.StringVar()
            self.raza = tk.StringVar()
            self.sexo = tk.StringVar()
            self.salud = tk.StringVar()
            self.condicion_corporal = tk.StringVar()
            self.corral = tk.StringVar()
            self.vars =[self.marca,self.peso,
                        self.edad,self.nacimiento,
                        self.raza,self.sexo,
                        self.salud,self.condicion_corporal,
                        self.corral
                        ]
            self.filtros = [var.get() for var in self.vars]
        default_vars()  
        # FILTROS
        # Construccion
        filtros_frame = tk.LabelFrame(tabGeneral,text="FILTROS",background="#46665F", foreground="white",font=("Helvetica", 10, "bold"))
        filtros_frame.pack(side="right",fill="y",padx=(8,0),pady=8,ipadx=4,ipady=4)
    
        # Crea un filtro a partir de ciertos parametros
        def crear_filtro(frame, row, col, texto, variable, opciones):
            ttk.Label(frame, text=f"{texto} : ", anchor="e", width=20).grid(row=row, column=col, padx=10, pady=2)
            ttk.OptionMenu(frame, variable, opciones[0], *opciones).grid(row=row, column=col+1, padx=2, sticky="w")
        # Funcion: actualizar la lista de filtros
        def act_filtros(*args):
            for item in listado.get_children():
                listado.delete(item)
            self.filtros = [var.get() for var in self.vars]
            # Datos a filtrar
            datos_filtrados = self.datos.filtros(self.filtros)
            if datos_filtrados != []:
                columns = list(datos_filtrados[0].keys())
            else:
                columns = 0
            for animal in datos_filtrados:
                try:
                    # Usa las claves del diccionario de forma dinámica
                    listado.insert("", tk.END, values=[animal[col] for col in columns])
                except KeyError as e:
                    print(f"Error en los datos: columna no encontrada {e}")
                except Exception as e:
                    print(f"Error al insertar datos: {e}")
            
            #marca,peso,edad,año,raza,sexo
        # Añadir funcion de act_filtros a cada variable
        for var in self.vars:
            var.trace("w", act_filtros)
        
        # Marca
        ttk.Label(filtros_frame, text="Marca : ", anchor="e", width=20).grid(row=1, column=1, padx=10, pady=2)
        marca_entry = ttk.Entry(filtros_frame,justify="center",textvariable=self.marca)
        marca_entry.grid(row=1,column=2,padx=2,ipadx=4,sticky="w")
        # Peso
        opciones_peso = ["-Seleccionar-","0-50","50-100","100-150","150-200","200-250","250-300","300-350","350-400","400-450","450-500"]
        crear_filtro(filtros_frame,2,1,"Peso",self.peso,opciones_peso)
        # Edad
        opciones_edad = ["-Seleccionar-"]
        opciones_edad.extend(sorted(list(manejo_datos(ganado).edades)))
        crear_filtro(filtros_frame,3,1,"Edad",self.edad,opciones_edad)
        # Año
        ttk.Label(filtros_frame, text="Año : ", anchor="e", width=20).grid(row=4, column=1, padx=10, pady=2)
        ttk.Entry(filtros_frame,width=14,justify="center",textvariable=self.nacimiento).grid(row=4,column=2,sticky="w")
        # Raza 
        opciones_raza = ["-Seleccionar-"]
        opciones_raza.extend(list(manejo_datos(ganado).razas.keys()))
        crear_filtro(filtros_frame,5,1,"Raza",self.raza,opciones_raza)
        # Separador
        ttk.Separator(filtros_frame,orient="vertical").grid(row=1,column=6,rowspan=5,padx=30,sticky="NES")
        # Sexo
        opciones_sexo = ["-Seleccionar-"]
        opciones_sexo.extend(sorted(list(manejo_datos(ganado).sexos)))
        crear_filtro(filtros_frame,1,7,"Sexo",self.sexo,opciones_sexo)
        # Estado de Salud
        opciones_salud = ["-Seleccionar-"]
        opciones_salud.extend(sorted(list(manejo_datos(ganado).salud)))
        crear_filtro(filtros_frame,2,7,"Estado de Salud",self.salud,opciones_salud)
        # Condicion Corporal
        opciones_corporal = ["-Seleccionar-"]
        opciones_corporal.extend(sorted(list(manejo_datos(ganado).condicion)))
        crear_filtro(filtros_frame,3,7,"Estado Corporal",self.condicion_corporal,opciones_corporal)
        # Gestacion
        
        # Corral
        opciones_corral = ["-Seleccionar-"]
        opciones_corral.extend(sorted(list(manejo_datos(ganado).corrales)))
        crear_filtro(filtros_frame,4,7,"Corral",self.corral,opciones_corral)
        # Boton Clean filters
        def cleanf():
            for var in self.vars:
                if var == self.marca or var == self.nacimiento:
                    var.set("")
                else:
                    var.set("-Seleccionar-")

        self.clean_filters = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\brocha.png")
        ttk.Button(filtros_frame, image=self.clean_filters,width=30,command=cleanf).grid(row=5,column=9,padx=2,sticky="w")
        act_filtros()
        # INGRESO-SELECCION
        # Frame Observaciones
        
        return tabGeneral
               
    def tab_machos(self,notebook):
        # Frame Tab-Machos
        tabMachos = ttk.Frame(notebook)
        
        # Frame Dataframe
        frame_data = ttk.Frame(tabMachos)
        frame_data.pack(side="top",fill="x",padx=4,pady=4)
        
        # Filtrar por machos
        filtros = ["" ,"-Seleccionar-", "-Seleccionar-", "-Seleccionar-", "-Seleccionar-","Macho", "-Seleccionar-", "-Seleccionar-","-Seleccionar-"]
        datos = self.datos.filtros(filtros)
        data = self.dataframes(frame_data,20,datos,None,None)
        
        # Mostrar solo ciertas columnas
        data["displaycolumns"]=("id","Marca","Edad","Nacimiento","Peso","Raza","Estado_Salud","Condicion_Corporal","Corral")
        
        # Imagen Toro
        # -- al seleccionar un animal debera mostrar la foto de dicho animal, en caso de no tener mostrara una default--
        foto_frame = tk.LabelFrame(tabMachos, background="#283331") # Frame 
        foto_frame.pack(side="left",fill="y",padx=4,pady=(4,8))
        
        self.img = tk.PhotoImage(file=r"Proyecto_ganado\imagenes\toro.png")
        label = tk.Label(foto_frame,image=self.img,background="#283331")
        label.pack()
        
        
        return tabMachos
    
    def tab_hembras(self,notebook):
        tabHembras = ttk.Frame(notebook)
        return tabHembras
        
    def Datos(self,*args):
        if self.actualW =="Datos":
            return
        # Preparando el frame principal
        self.frame_principal.destroy()
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill="both",side="right",expand=True,padx=(0,10))
        self.actualW="Datos"
        
        # Creamos el notebook
        notebook = ttk.Notebook(self.frame_principal)
        
        #  TAB - GENERAL
        tabGeneral = self.tab_general(notebook)
        tabMachos = self.tab_machos(notebook)
        tabHembras = self.tab_hembras(notebook)
        
        # Añadimos los tabs al notebook
        notebook.add(tabGeneral,text="General")
        notebook.add(tabMachos,text="Machos")
        notebook.add(tabHembras,text="Hembras")
        notebook.pack(expand=True, fill="both")
    
    def Principal(self):
        if self.actualW =="Principal":
            return
        # Preparando el frame principal
        self.frame_principal.destroy()
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill="both",side="right",expand=True)
        self.actualW = "Principal"
        # Al usar .grid() se debe configurar las columnas y filas
        self.frame_principal.rowconfigure(0, weight=4)
        self.frame_principal.rowconfigure(1, weight=2)
        self.frame_principal.rowconfigure(2, weight=4)
        self.frame_principal.columnconfigure(0,weight=12)
        self.frame_principal.columnconfigure(1,weight=8)
        # Se plantean y muestran los diferentes botones principales
        analiticas = ttk.Button(self.frame_principal, text='Analisis')
        analiticas.grid(row=0, column=0, sticky='NSWE',rowspan=3,padx=(15,8),pady=15)
        #notificaciones = ttk.Button(self.frame_principal, text='Promedios',)
        #notificaciones.grid(row=2, column=0, sticky='NSWE',padx=8,pady=8)
        notificaciones = ttk.Button(self.frame_principal, text='Notificaciones')
        notificaciones.grid(row=0, column=1, sticky='NSWE',padx=(8,15),pady=(15,8))
        # Datos
        # Crear botón de datos con Treeview
        datos_btn = ttk.Button(self.frame_principal, command=self.Datos)
        datos_btn.grid(row=1, column=1, sticky='NSWE', padx=(8, 15), pady=(8, 15), rowspan=2)

        # Crear un frame dentro del botón para organizar los datos
        tree_frame = ttk.Frame(datos_btn)
        tree_frame.pack(expand=True)

        # Crear el Treeview dentro del frame
        tree = ttk.Treeview(tree_frame, columns=("Dato", "Cantidad"), show="headings", height=9,style="Home.Treeview")
        tree.heading("Dato", text="Dato",command=self.Datos) 
        tree.heading("Cantidad", text="Cantidad",command=self.Datos)
        tree.column("Dato", anchor="center")
        tree.column("Cantidad", anchor="center")
        tree.pack()

        # Obtener los datos y añadirlos al Treeview
        datos, cantidades = self.datos.muestra()
        for i in range(len(datos)):
            tree.insert("", "end", values=(datos[i], cantidades[i]))
            
        tree.bind("<<TreeviewSelect>>", self.Datos)


if __name__ == "__main__":
    app = App()
    app.mainloop()
