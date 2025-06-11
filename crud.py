from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox
import mysql.connector

# Crear una instancia de Tkinter
root = Tk()
root.title('DOG BARBER')
root.geometry('+10+10')
#root.geometry("+%d+%d" % ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2, (root.winfo_screenheight() - root.winfo_reqheight()) / 2))


#ESTILOS
#Frame
style = ttk.Style()
style.configure('black.TFrame',background='#000000')
style.configure('blue.TFrame',background='#0062C6')
style.configure('white.TFrame',background='#ffffff')
style.configure('red.TFrame',background='red')
#Label
style.configure('black.TLabel',background='black')
#Botones
style.configure('black.TButton',background='black')
'''
1) Crearemos widgets dentro de un frame
2) Ubicaremos el framde dentro de otro frame para personalizar correctamente el ancho y alto
3) De esta manera evitamos configurar cada widget y solo lo haremos con el frame
'''
#FRAME a
framea = ttk.Frame(root, style='blue.TFrame')
framea.pack(fill=BOTH, side=LEFT)
frame1 = ttk.Frame(framea, style='black.TFrame')
frame1.pack(expand=TRUE, fill=BOTH, ipadx=35)
frame2 = ttk.Frame(framea)
frame2.pack(expand=TRUE)
#FRAME b
frameb = ttk.Frame(root)
frameb.pack(expand=TRUE, fill=BOTH, side=RIGHT)
frame3 = LabelFrame(frameb, text='  BUSCAR HISTORIA CLINICA  ')
frame3.pack(expand=TRUE, fill=BOTH, padx=20, pady=10)
frame3_3 = ttk.Frame(frame3)
frame3_3.pack(expand=TRUE, padx=20, pady=10)
frame4 = ttk.Frame(frameb)#, style='red.TFrame')
frame4.pack(expand=TRUE, padx=20)
#Frame c
framec = ttk.Frame(root)
#framec.pack(expand=TRUE, fill=BOTH, side=RIGHT)

#--------------------------------FUNCIONES ventana principal------------------------------------

def datosEnTabla1():
    
    try:
        #Conexión con mysql    
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursor=conexion.cursor()#----Cursor para realizar consultas
        
        cTabla1 = "SELECT propietario.DNI, propietario.NOMBRE, propietario.APELLIDO, paciente.MASCOTA, propietario.CELULAR, historia_clinica.N_HC, historia_clinica.FECHA"
        cTabla2 = "propietario INNER JOIN paciente ON propietario.ID_PROPIETARIO = paciente.ID_PACIENTE INNER JOIN historia_clinica ON propietario.ID_PROPIETARIO = historia_clinica.ID_HC"
        cursor.execute(cTabla1+" FROM "+cTabla2) #---trae los datos de las filas de las tabla unida
        global filas
        filas = cursor.fetchall()#----Guarda todos los datos en una variable
        print('filas :',len(filas),filas)
        #-----Insertar datos en Treeview
        for i in filas:
            tabla.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))
        cursor.close()
        conexion.close
    
    except mysql.connector.errors.DatabaseError as errormysql: 
        print(errormysql)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{errormysql}\n\nNo estás conectado a la base de datos')
    except Exception as error:
        print(error)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')
  
def filtrar():
    #----- 0 (VARIABLE) LISTA que contiene los datos 
    #----- 1 (CONDICIONAL) VALIDA si el widget no está vacio
        #----- 2 (MÉTODO) ELIMINA todas las filas actuales de la tabla
        #----- 3 (VARIABLE) CREA lista nueva que almacenara datos filtrados
        #----- 4 (BUCLE) RECORRE cada tupla de la anterior lista
            #----- 5 (CONDICIONAL) VALIDA si el texto ingresado se encuentra en el indice[] de la tupla
                #----- 6 (MÉTODO) AGREGA la tupla que contiene el texto ingresado a la lista nueva
                #----- 7 (MÉTODO) AGREGA los datos a la tabla
    #----- 2 PASS Si el widget está vacío
    

    print("-----------------------------------------------------------------")
    try:
        print(f"Filas actuales = {len(filas)} {filas}")#----- 0

        '''
        Todos los textos tienen subconjuntos que inlcuyen el vacio ''
        Eso quiere decir que todos los texto tienen '', despues de a 2 caracter, despues de a 3 catacters, etc 
        '''
        global nueva_fila1, nueva_fila2, nueva_fila3, nueva_fila4#---0
        if entrada1.get() != '':#---Si hay texto entrada1, SIGUES
            tabla.delete(*tabla.get_children())#----- 2
            nueva_fila1=[]#----- 3
            for tupla in filas:#----- 4
                if entrada1.get() in tupla[0]:#------ 5
                    print(f"Tupla: {tupla}")
                    nueva_fila1.append(tupla)#----- 6
                    tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))#----- 7
            print(f"------NUEVA FILA 1: {len(nueva_fila1)} {nueva_fila1}")#----- 0
            
            if entrada2.get() != '':#---Si hay texto entrada2, sigues
                tabla.delete(*tabla.get_children())#----- 2
                nueva_fila2=[]#----- 3
                for tupla in nueva_fila1:#----- 4
                    if entrada2.get() in tupla[1]:#----- 5
                        print(f"Texto ingresado indice[1] : {entrada2.get()}")
                        print(f"Tupla: {tupla}")
                        nueva_fila2.append(tupla)#----- 6
                        tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))#----- 7
                print(f"------NUEVA FILA 2: {len(nueva_fila2)} {nueva_fila2}")
                
                if entrada3.get() != '':#---Si hay texto entrada3, sigues
                    tabla.delete(*tabla.get_children())
                    nueva_fila3=[]
                    for tupla in nueva_fila2:
                        if entrada3.get() in tupla[2]:
                            print(f"Texto ingresado indice[2] : {entrada3.get()}")
                            print(f"Tupla: {tupla}")
                            nueva_fila3.append(tupla)
                            tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                    print(f"------NUEVA FILA 3: {len(nueva_fila3)} {nueva_fila3}")
                    
                    if entrada4.get() != '':#---Si hay texto entrada4, sigues
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila3:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")
                        
                else:#--Si la entrada 3 está vacio, SALTAS entrada4
                    if entrada4.get() != '':
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila2:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")
                
            else:#--Si entrada2 está vacio, SALTAS a entrada3
                if entrada3.get() != '':#Si hay texto entrada3, SIGUES
                    tabla.delete(*tabla.get_children())
                    nueva_fila3=[]
                    for tupla in nueva_fila1:
                        if entrada3.get() in tupla[2]:
                            print(f"Texto ingresado indice[2] : {entrada3.get()}")
                            print(f"Tupla: {tupla}")
                            nueva_fila3.append(tupla)
                            tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                    print(f"------NUEVA FILA 3: {len(nueva_fila3)} {nueva_fila3}") 
                    
                    if entrada4.get() != '':#Si hay texto entrada4, SIGUES
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila3:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")
                    
                else:#--Si entrada3 está vacio, SALTAS a entrada 4
                    if entrada4.get() != '':
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila1:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}") 
                    else: pass#--Si entrada4 está vacio, PASS
        
        else:#---Si entrada1 esta vacío
            if entrada2.get() != '':#---Si hay texto entrada2, sigues
                tabla.delete(*tabla.get_children())#----- 2
                nueva_fila2=[]#----- 3
                for tupla in filas:#----- 4
                    if entrada2.get() in tupla[1]:#----- 5
                        print(f"Texto ingresado indice[1] : {entrada2.get()}")
                        print(f"Tupla: {tupla}")
                        nueva_fila2.append(tupla)#----- 6
                        tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))#----- 7
                print(f"------NUEVA FILA 2: {len(nueva_fila2)} {nueva_fila2}")
                
                if entrada3.get() != '':#---Si hay texto entrada3, sigues
                    tabla.delete(*tabla.get_children())
                    nueva_fila3=[]
                    for tupla in nueva_fila2:
                        if entrada3.get() in tupla[2]:
                            print(f"Texto ingresado indice[2] : {entrada3.get()}")
                            print(f"Tupla: {tupla}")
                            nueva_fila3.append(tupla)
                            tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                    print(f"------NUEVA FILA 3: {len(nueva_fila3)} {nueva_fila3}")
                    
                    if entrada4.get() != '':#---Si hay texto entrada4, sigues
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila3:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")
                        
                else:#--Si la entrada 3 está vacio, SALTAS entrada4
                    if entrada4.get() != '':
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila2:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")           
            
            else:#---Si entrada2 está vacio, SALTAS a entrada3
                if entrada3.get() != '':#---Si hay texto entrada3, SIGUES
                    tabla.delete(*tabla.get_children())
                    nueva_fila3=[]
                    for tupla in filas:
                        if entrada3.get() in tupla[2]:
                            print(f"Texto ingresado indice[2] : {entrada3.get()}")
                            print(f"Tupla: {tupla}")
                            nueva_fila3.append(tupla)
                            tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                    print(f"------NUEVA FILA 3: {len(nueva_fila3)} {nueva_fila3}") 
                    
                    if entrada4.get() != '':#Si hay texto entrada4, SIGUES
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in nueva_fila3:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}")
                    
                else:#---Si entrada3 está vacio, SALTAS a entrada 4
                    if entrada4.get() != '':#---SI hay texto en entrada4, SIGUES
                        tabla.delete(*tabla.get_children())
                        nueva_fila4=[]
                        for tupla in filas:
                            if entrada4.get() in tupla[3]:
                                print(f"Texto ingresado indice[2] : {entrada4.get()}")
                                print(f"Tupla: {tupla}")
                                nueva_fila4.append(tupla)
                                tabla.insert('', 0, text=tupla[0], values=(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6]))
                        print(f"------NUEVA FILA 4: {len(nueva_fila4)} {nueva_fila4}") 
                    else:#---Si entrada4 está vacio
                        tabla.delete(*tabla.get_children())
                        datosEnTabla1()
    except Exception as error:
        print(error)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}\n\nNo estás conectado a la base de datos')
#--------------------------------Framea-------------------------------------------------------
# Widget con pad dentro del FRAME 1
imagen = PhotoImage(file='D:\Proyectos\DOG_BARBER\CRUD\logo_fondonegro.png')
Label(frame1, image=imagen, bg='black').pack(expand=True)


# widget con pad dentro del FRAME 2
boton1 = Button(frame2, text='CLIENTES',font=('Dosis',20,'bold') , fg='#ffffff', bg='#0062C6', borderwidth=1, relief='ridge')
boton1.grid(row=0, column=0, ipady=20, sticky='NSWE')
boton2 = Button(frame2, text='CONTABILIDAD',font=('Dosis',20,'bold') , fg='#ffffff', bg='#0062C6',  borderwidth=1, relief='ridge')
boton2.grid(row=1, column=0, ipadx=20, ipady=20, sticky='NSWE')

#--------------------------------Frameb-------------------------------------------------------
# widget con pad dentro del FRAME 3
#fila 0
Label(frame3_3, text='DNI:').grid(row=0, column=0, pady=10, sticky='e')
entrada1 = Entry(frame3_3, width=40)
entrada1.grid(row=0, column=1, columnspan=3, padx=10, sticky='w')
#fila 1
Label(frame3_3, text='Nombre:').grid(row=1, column=0, pady=10, sticky='e')
entrada2 = Entry(frame3_3, width=30)
entrada2.grid(row=1, column=1, padx=10, sticky='w')
Label(frame3_3, text='Apellido:').grid(row=1, column=2, pady=10, sticky='e')
entrada3 = Entry(frame3_3, width=40)
entrada3.grid(row=1, column=3, padx=10, sticky='w')
#fila 2
Label(frame3_3, text='Nombre de Mascota:').grid(row=2, column=0, pady=10, sticky='e')
entrada4 = Entry(frame3_3, width=50)
entrada4.grid(row=2, column=1, columnspan=3, padx=10, sticky='w')
#Creación de boton
botonBuscar = Button(frame3_3, text='ACTUALIZAR', bg='yellow', command=filtrar).grid(row=3, column=3, ipadx=10, ipady=2, padx=10, pady=10)

#-------------------- VENTANA DE LECTURA -------------------- VENTANA PARA CREAR -----------------------------------
#--- Variables de la Historia clinica ---
vActitud=['letárgico','estuporoso','comatoso','alerta']
vGenero=['hombre','mujer']

def nuevaVentana():
    
    print('---Ventana creada---')
    # Crear nueva ventana
    global root2
    root2 = Toplevel(root)
    root2.title('DOG BARBER - Historia Clínica')
    root2.geometry('1350x650')
    root2.geometry('+1+1')
    global estadoRoot2
    estadoRoot2 = True
    print('2 estadoRoot2 :',estadoRoot2)
    root2.protocol("WM_DELETE_WINDOW", cierreRoot2)
    #--- Método protocol ejecuta la función cuando se apreta boton cerrar de la ventana
    
    '''Si quieres ver el fondo del widget padre,
    debes usar pad en el widget interno'''
    #-------------------- FRAME A ----------------------------------------------------------------------
    frameA = ttk.Frame(root2)#, style='white.TFrame')
    frameA.pack(fill=BOTH, side=LEFT)
    frame_a = ttk.Frame(frameA, style='black.TFrame')
    frame_a.pack(expand=True, fill=BOTH)
    frame_b = ttk.Frame(frameA, style='white.TFrame')
    frame_b.pack(expand=True, fill=BOTH, ipady=40)
    #Labelframe
    frame_imagen = Frame(frame_a)
    frame_imagen.pack(expand=TRUE, padx=20, pady=20)
    frame_mascota = LabelFrame(frame_b)
    frame_mascota.pack(expand=TRUE, padx=20)
    frame_mascota1 = Frame(frame_mascota)
    frame_mascota1.pack(padx=20, pady=10)
    
    global frame_tabla #--- frame_tabla se destruye
    frame_tabla = LabelFrame(frame_b)
    frame_tabla.pack(expand=TRUE, padx=20)
    frame_tabla1 = Frame(frame_tabla)
    frame_tabla1.pack(padx=20, pady=10)
      
    #-------------------- FRAME B ---------------------------------------------------------------------------
    frameB = ttk.Frame(root2)
    frameB.pack(expand=True, fill=BOTH, side=RIGHT)
    frame_c = ttk.Frame(frameB)#,  style='red.TFrame')
    frame_c.pack(expand=True, fill=BOTH)
    global frame_d #--- widgets dentro de frame_d se editan
    frame_d = ttk.Frame(frameB, style='blue.TFrame')
    frame_d.pack(fill=X, side=BOTTOM, ipady=10)
    #CrearCanvas
    canvas = Canvas(frame_c, bg='yellow', width=1000, height=560)
    canvas.pack(expand=True, side=LEFT)
    #CrearScrollbar
    scrollbar = Scrollbar(frame_c)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=canvas.yview)
    #ConfiguracionDelScrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    # Enlazar controlador de eventos del mouse para canvas y scrollbar
    canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    scrollbar.config(command=canvas.yview)
    # Enlazar controlador de eventos del mouse para la ventana principal
    #canvas.bind('<B1-Motion>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    #Agregar mainframe al canvas
    main_frame = ttk.Frame(canvas)#, style='white.TFrame')
    main_frame.pack(expand=True, fill=BOTH, side=TOP)
    canvas.create_window((0, 0), window=main_frame, anchor='nw')
    canvas.update_idletasks()
    #Agregar LabelFrame al mainframe
    frame_fecha = Frame(main_frame)
    frame_fecha.pack(pady=20)
    frame_propi = LabelFrame(main_frame, text='  PROPIETARIO  ')
    frame_propi.pack(pady=20)
    global frame_propi1 #--- widgets dentro de frame_propi1 se editan
    frame_propi1 =Frame(frame_propi)
    frame_propi1.pack(padx=20, pady=20)
    frame_anam = LabelFrame(main_frame, text='  ANAMNESIS  ')
    frame_anam.pack(pady=20)
    frame_anam1 = Frame(frame_anam)
    frame_anam1.pack(padx=20, pady=20)
    frame_despa = LabelFrame(frame_anam, text='  DESPARASITACIÓN  ')
    frame_despa.pack(padx=20)
    frame_despa1 =Frame(frame_despa)
    frame_despa1.pack(padx=20, pady=20)
    frame_vacu = LabelFrame(frame_anam, text='  VACUNACIÓN  ')
    frame_vacu.pack(padx=20, pady=20)
    frame_vacu1 = Frame(frame_vacu)
    frame_vacu1.pack(padx=20, pady=20)
    frame_clinico = LabelFrame(main_frame, text='  EXÁMEN CLÍNICO  ')
    frame_clinico.pack(pady=10)
    frame_clinico1 = Frame(frame_clinico)
    frame_clinico1.pack(padx=20, pady=20)
    frame_oys = LabelFrame(frame_clinico, text='  ÓRGANOS Y SISTEMAS  ')
    frame_oys.pack(padx=20, pady=20)
    frame_oys1 = Frame(frame_oys)
    frame_oys1.pack(padx=20, pady=20)
    frame_diferencial = LabelFrame(main_frame, text='  DIAGNÓSTICO DIFERENCIAL  ')
    frame_diferencial.pack(pady=20)
    frame_problema = LabelFrame(frame_diferencial, text='  PROBLEMAS  ')
    frame_problema.pack(padx=20, pady=20, side=LEFT)
    frame_problema1 = Frame(frame_problema)
    frame_problema1.pack(padx=20, pady=20)
    frame_diagnostico = LabelFrame(frame_diferencial, text='  DIAGNÓSTICO  ')
    frame_diagnostico.pack(padx=20, pady=20, side=RIGHT)
    frame_diagnostico1 = Frame(frame_diagnostico)
    frame_diagnostico1.pack(padx=20, pady=20)
    frame_complementario = LabelFrame(main_frame, text='  EXÁMEN COMPLEMENTARIO  ')
    frame_complementario.pack(pady=20)
    frame_complementario1 = Frame(frame_complementario)
    frame_complementario1.pack(padx=20, pady=20)
    frame_conclusionFinal = LabelFrame(main_frame, text='  CONCLUSIONES  ')
    frame_conclusionFinal.pack(pady=20)
    frame_conclusionFinal1 = Frame(frame_conclusionFinal)
    frame_conclusionFinal1.pack(padx=20, pady=20)
    frame_tratamiento = LabelFrame(main_frame, text='  TRATAMIENTO  ')
    frame_tratamiento.pack(pady=20)
    frame_medico = LabelFrame(frame_tratamiento, text='  MÉDICO VETERINARIO  ')
    frame_medico.pack(padx=20, pady=20)
    frame_medico1 = Frame(frame_medico)
    frame_medico1.pack(padx=20, pady=20)
    frame_detalles = Frame(frame_tratamiento)
    frame_detalles.pack(padx=20, pady=20)
    
    global nHC,fHC
    global nMasco,mEspecie,mRaza,mSexo,mPeso,mNaci
    global dni,nombreProp,apellido,nacimiento,genero,celular,correo,domicilio
    global eAnte,trata,evo,ali,hRepro,uCelo,uParto,mConsul,dProdu,dFecha,vMarca,vLote,vFecha
    global fRespi,lCapi,fCardi,gLinfa,tempe,muco,pulso,acti
    global eGene,eHidra,sTegu,ojos,oidos,nariz,sDiges,sRespi,sNervi,sMuscu,sCardio,sGeni,dHalla
    global proble1,proble2,proble3,proble4,proble5,proble6,proble7,diag1,diag2,diag3,diag4,diag5,diag6,diag7
    global qSangui,rayosx,eco,cHepa,frotis,copro,endos,ecg,eeg,pOri,copros,culti,anti,biopsia,otros
    global dHPD,dFinal
    global mNombre,mApe,mMatri,tTrata,pBase,dBasi,presen,via,frecu,dura
    
    #---------- Widget dentro de FRAME A --------------------------------------------------------------------------------
    #PACIENTE
    Label(frame_imagen, image=imagen, bg='black').pack(expand=True)
    Label(frame_mascota1, text='MASCOTA:').grid(row=0, column=0, pady=10, sticky='e')
    nMasco=Entry(frame_mascota1)
    nMasco.grid(row=0, column=1, pady=10)
    Label(frame_mascota1, text='ESPECIE:').grid(row=1, column=0, pady=10, sticky='e')
    mEspecie=Entry(frame_mascota1)
    mEspecie.grid(row=1, column=1, pady=10)
    Label(frame_mascota1, text='RAZA:').grid(row=2, column=0, pady=10, sticky='e')
    mRaza=Entry(frame_mascota1)
    mRaza.grid(row=2, column=1, pady=10)
    Label(frame_mascota1, text='SEXO:').grid(row=3, column=0, pady=10, sticky='e')
    mSexo=Entry(frame_mascota1)
    mSexo.grid(row=3, column=1, pady=10)
    Label(frame_mascota1, text='PESO (Kg):').grid(row=4, column=0, pady=10, sticky='e')
    mPeso=Entry(frame_mascota1)
    mPeso.grid(row=4, column=1, pady=10)
    Label(frame_mascota1, text='NACIMIENTO:').grid(row=5, column=0, pady=10, sticky='e')
    mNaci=Entry(frame_mascota1)
    mNaci.grid(row=5, column=1, pady=10)
    #Treeview
    global tabla2
    tabla2 = ttk.Treeview(frame_tabla1, height=3, column='fecha')
    tabla2.grid(row=0, column=0, columnspan=2, pady=10)
    tabla2.heading('#0', text='Nº H.C')
    tabla2.heading('fecha', text='FECHA')
    # Ajustar ancho de columnas
    tabla2.column('#0', width=60)
    tabla2.column('fecha', width=130)
    # Agregar filas de ejemplo
    #tabla2.insert('', 'end', text='1', values='23/03/2023')
    #Boton
    global botonAbrir,botonCrear2
    botonAbrir = Button(frame_tabla1, text='ABRIR', bg='#0062C6', fg='white', command=Abrir)
    botonAbrir.grid(row=1, column=0, ipadx=15, ipady=3, padx=10, pady=10)
    botonCrear2 = Button(frame_tabla1, text='NUEVO', bg='green', fg='white', command=Nuevo)
    botonCrear2.grid(row=1, column=1, ipadx=15, ipady=3, padx=10, pady=10)

    
    #---------- Widget dentro de FRAME B -----------------------------------------------------------------------------------------------
    #HISTORIA CLINICA
    Label(frame_fecha, text='Nº HISTORIA CLÍNICA').grid(row=0, column=0, padx=20, pady=10)
    nHC=Label(frame_fecha, text=1)
    nHC.grid(row=1, column=0, padx=20)
    Label(frame_fecha, text='FECHA').grid(row=0, column=1, padx=20, pady=10)
    fHC=Entry(frame_fecha)
    fHC.grid(row=1, column=1, padx=20)
    
    #PROPIETARIO
    Label(frame_propi1, text='DNI:').grid(row=0, column=0, pady=10, sticky='e')
    dni=Entry(frame_propi1)
    dni.grid(row=0, column=1, padx=10, sticky='w')
    Label(frame_propi1, text='NOMBRE:').grid(row=0, column=2, pady=10, sticky='e')
    nombreProp=Entry(frame_propi1, width=30)
    nombreProp.grid(row=0, column=3, padx=10)
    Label(frame_propi1, text='APELLIDO').grid(row=0, column=4, pady=10, sticky='e')
    apellido=Entry(frame_propi1, width=40)
    apellido.grid(row=0, column=5, padx=10)
    Label(frame_propi1, text='NACIMIENTO:').grid(row=1, column=0, pady=10, sticky='e')
    nacimiento=Entry(frame_propi1)
    nacimiento.grid(row=1, column=1, padx=10, sticky='w')
    Label(frame_propi1, text='GÉNERO:').grid(row=1, column=2, pady=10, sticky='e')
    genero=ttk.Combobox(frame_propi1, values=vGenero)
    genero.grid(row=1, column=3, padx=10)
    Label(frame_propi1, text='CELULAR:').grid(row=1, column=4, pady=10, sticky='e')
    celular=Entry(frame_propi1, width=30)
    celular.grid(row=1, column=5, padx=10, sticky='w')
    Label(frame_propi1, text='DOMICILIO:').grid(row=2, column=0, pady=10, sticky='e')
    domicilio=Entry(frame_propi1)
    domicilio.grid(row=2, column=1, columnspan=5, padx=10, sticky='we')
    Label(frame_propi1, text='CORREO:').grid(row=3, column=0, pady=10, sticky='e')
    correo=Entry(frame_propi1)
    correo.grid(row=3, column=1, columnspan=5, padx=10, sticky='we')
    
    #ANAMNESIS
    Label(frame_anam1, text='ENFERMEDADES ANTERIORES:').grid(row=1, column=0, pady=10, sticky='e')
    eAnte = Text(frame_anam1, height=4, width=80)
    eAnte.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    Label(frame_anam1, text='TRATAMIENTOS:').grid(row=2, column=0, pady=10, sticky='e')
    trata = Text(frame_anam1, height=4, width=80)
    trata.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    Label(frame_anam1, text='EVOLUCIÓN:').grid(row=3, column=0, pady=10, sticky='e')
    evo = Text(frame_anam1, height=4, width=80)
    evo.grid(row=3, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    Label(frame_anam1, text='ALIMENTACIÓN:').grid(row=4, column=0, pady=10, sticky='e')
    ali = Text(frame_anam1, height=4, width=80)
    ali.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    Label(frame_anam1, text='HISTORIA REPRODUCTIVA:').grid(row=5, column=0, pady=10, sticky='e')
    hRepro = Text(frame_anam1, height=4, width=80)
    hRepro.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    Label(frame_anam1, text='ÚLTIMO CELO:').grid(row=6, column=0, pady=10, sticky='e')
    uCelo = Entry(frame_anam1, width=30)
    uCelo.grid(row=6, column=1, padx=10, sticky='w')
    Label(frame_anam1, text='ÚLTIMO PARTO:').grid(row=6, column=2, pady=10, sticky='e')
    uParto = Entry(frame_anam1, width=30)
    uParto.grid(row=6, column=3, padx=10, sticky='w')
    Label(frame_anam1, text='MOTIVO DE CONSULTA:').grid(row=7, column=0, pady=10, sticky='e')
    mConsul = Text(frame_anam1, height=4, width=80)
    mConsul.grid(row=7, column=1, columnspan=3, padx=10, pady=10, sticky='w')
    #DESPARASITACIÓN
    Label(frame_despa1, text='PRODUCTO:').grid(row=0, column=0, pady=10, sticky='e')
    dProdu = Entry(frame_despa1, width=40)
    dProdu.grid(row=0, column=1, padx=10, sticky='w')
    Label(frame_despa1, text='FECHA:').grid(row=0, column=2, pady=10, sticky='e')
    dFecha = Entry(frame_despa1, width=30)
    dFecha.grid(row=0, column=3, padx=10, sticky='w')
    #VACUNACIÓN
    Label(frame_vacu1, text='MARCA:').grid(row=0, column=0, pady=10, sticky='e')
    vMarca = Entry(frame_vacu1, width=40)
    vMarca.grid(row=0, column=1, padx=10, sticky='w')
    Label(frame_vacu1, text='LOTE:').grid(row=0, column=2, pady=10, sticky='e')
    vLote = Entry(frame_vacu1, width=30)
    vLote.grid(row=0, column=3, padx=10, sticky='w')
    Label(frame_vacu1, text='FECHA:').grid(row=0, column=4, pady=10, sticky='e')
    vFecha = Entry(frame_vacu1, width=30)
    vFecha.grid(row=0, column=5, padx=10, sticky='w')
    
    #EXAMEN CLINICO
    Label(frame_clinico1, text='FRECUENCIA RESPIRATORIA (rpm):').grid(row=0, column=0, pady=10, sticky='e')
    fRespi=Entry(frame_clinico1)
    fRespi.grid(row=0, column=1, padx=10, sticky='w')
    Label(frame_clinico1, text='LLENADO CAPILAR (tiempo):').grid(row=0, column=2, pady=10, sticky='e')
    lCapi=Entry(frame_clinico1)
    lCapi.grid(row=0, column=3, padx=10, sticky='w')
    Label(frame_clinico1, text='FRECUENCIA CARDIACA (lpm):').grid(row=1, column=0, pady=10, sticky='e')
    fCardi=Entry(frame_clinico1)
    fCardi.grid(row=1, column=1, padx=10, sticky='w')
    Label(frame_clinico1, text='GANGLIOS LINFÁTICOS:').grid(row=1, column=2, pady=10, sticky='e')
    gLinfa=Entry(frame_clinico1)
    gLinfa.grid(row=1, column=3, padx=10, sticky='w')
    Label(frame_clinico1, text='TEMPERATURA (ºC):').grid(row=2, column=0, pady=10, sticky='e')
    tempe=Entry(frame_clinico1)
    tempe.grid(row=2, column=1, padx=10, sticky='w')
    Label(frame_clinico1, text='MUCOSAS:').grid(row=2, column=2, pady=10, sticky='e')
    muco=Entry(frame_clinico1)
    muco.grid(row=2, column=3, padx=10, sticky='w')
    Label(frame_clinico1, text='PULSO:').grid(row=3, column=0, pady=10, sticky='e')
    pulso=Entry(frame_clinico1)
    pulso.grid(row=3, column=1, padx=10, sticky='w')
    Label(frame_clinico1, text='ACTITUD:').grid(row=3, column=2, pady=10, sticky='e')
    acti=ttk.Combobox(frame_clinico1, values=vActitud)
    acti.grid(row=3, column=3, padx=10, sticky='w')
    #ORGANOS Y SISTEMAS
    Label(frame_oys1, text='ESTADO GENERAL:').grid(row=0, column=0, pady=10, sticky='e')
    eGene = Text(frame_oys1, height=3, width=70)
    eGene.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='ESTADO DE HIDRATACIÓN:').grid(row=1, column=0, pady=10, sticky='e')
    eHidra = Text(frame_oys1, height=3, width=70)
    eHidra.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='OJOS:').grid(row=2, column=0, pady=10, sticky='e')
    ojos = Text(frame_oys1, height=3, width=70)
    ojos.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='ODIOS:').grid(row=3, column=0, pady=10, sticky='e')
    oidos = Text(frame_oys1, height=3, width=70)
    oidos.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='NARIZ:').grid(row=4, column=0, pady=10, sticky='e')
    nariz = Text(frame_oys1, height=3, width=70)
    nariz.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    #STM
    Label(frame_oys1, text='SISTEMA TEGUMENTARIO:').grid(row=6, column=0, pady=10, sticky='e')
    sTegu = Text(frame_oys1, height=3, width=70)
    sTegu.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA DIGESTIVO:').grid(row=7, column=0, pady=10, sticky='e')
    sDiges = Text(frame_oys1, height=3, width=70)
    sDiges.grid(row=7, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA RESPIRATORIO:').grid(row=8, column=0, pady=10, sticky='e')
    sRespi = Text(frame_oys1, height=3, width=70)
    sRespi.grid(row=8, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA NERVIOSO:').grid(row=9, column=0, pady=10, sticky='e')
    sNervi = Text(frame_oys1, height=3, width=70)
    sNervi.grid(row=9, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA MUSCULO-ESQUELÉTICO:').grid(row=10, column=0, pady=10, sticky='e')
    sMuscu = Text(frame_oys1, height=3, width=70)
    sMuscu.grid(row=10, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA CARDIOVASCULAR:').grid(row=11, column=0, pady=10, sticky='e')
    sCardio = Text(frame_oys1, height=3, width=70)
    sCardio.grid(row=11, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='SISTEMA GENITOURINARIO:').grid(row=12, column=0, pady=10, sticky='e')
    sGeni = Text(frame_oys1, height=3, width=70)
    sGeni.grid(row=12, column=1, padx=10, pady=10, sticky='w')
    Label(frame_oys1, text='DESCRIPCIÓN DE HALLAZGOS:').grid(row=13, column=0, pady=10, sticky='e')
    dHalla = Text(frame_oys1, height=3, width=70)
    dHalla.grid(row=13, column=1, padx=10, pady=10, sticky='w')
    #DIAGNOSTICO DIFERENCIAL-PROBLEMA
    Label(frame_problema1, text='1º PROBLEMA:').grid(row=0, column=0, pady=10, sticky='e')
    proble1 = Text(frame_problema1, height=3, width=30)
    proble1.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='2º PROBLEMA:').grid(row=1, column=0, pady=10, sticky='e')
    proble2 = Text(frame_problema1, height=3, width=30)
    proble2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='3º PROBLEMA:').grid(row=2, column=0, pady=10, sticky='e')
    proble3 = Text(frame_problema1, height=3, width=30)
    proble3.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='4º PROBLEMA:').grid(row=3, column=0, pady=10, sticky='e')
    proble4 = Text(frame_problema1, height=3, width=30)
    proble4.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='5º PROBLEMA:').grid(row=4, column=0, pady=10, sticky='e')
    proble5 = Text(frame_problema1, height=3, width=30)
    proble5.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='6º PROBLEMA:').grid(row=5, column=0, pady=10, sticky='e')
    proble6 = Text(frame_problema1, height=3, width=30)
    proble6.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    Label(frame_problema1, text='7º PROBLEMA:').grid(row=6, column=0, pady=10, sticky='e')
    proble7 = Text(frame_problema1, height=3, width=30)
    proble7.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    #DIAGNOSTICO DIFERENCIAL-DIAGNÓSTICO
    Label(frame_diagnostico1, text='1º DIAGNÓSTICO:').grid(row=0, column=0, pady=10, sticky='e')
    diag1 = Text(frame_diagnostico1, height=3, width=30)
    diag1.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='2º DIAGNÓSTICO:').grid(row=1, column=0, pady=10, sticky='e')
    diag2 = Text(frame_diagnostico1, height=3, width=30)
    diag2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='3º DIAGNÓSTICO:').grid(row=2, column=0, pady=10, sticky='e')
    diag3 = Text(frame_diagnostico1, height=3, width=30)
    diag3.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='4º DIAGNÓSTICO:').grid(row=3, column=0, pady=10, sticky='e')
    diag4 = Text(frame_diagnostico1, height=3, width=30)
    diag4.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='5º DIAGNÓSTICO:').grid(row=4, column=0, pady=10, sticky='e')
    diag5 = Text(frame_diagnostico1, height=3, width=30)
    diag5.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='6º DIAGNÓSTICO:').grid(row=5, column=0, pady=10, sticky='e')
    diag6 = Text(frame_diagnostico1, height=3, width=30)
    diag6.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    Label(frame_diagnostico1, text='7º DIAGNÓSTICO:').grid(row=6, column=0, pady=10, sticky='e')
    diag7 = Text(frame_diagnostico1, height=3, width=30)
    diag7.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    #EXAMEN COMPLEMENTARIO
    Label(frame_complementario1, text='QUÍMICA SANGUÍNEA:').grid(row=0, column=0, pady=10, sticky='e')
    qSangui = Text(frame_complementario1, height=3, width=70)
    qSangui.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='RAYOS X:').grid(row=1, column=0, pady=10, sticky='e')
    rayosx = Text(frame_complementario1, height=3, width=70)
    rayosx.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='ECOGRAFÍA:').grid(row=2, column=0, pady=10, sticky='e')
    eco = Text(frame_complementario1, height=3, width=70)
    eco.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='CUADRO HEPÁTICO:').grid(row=3, column=0, pady=10, sticky='e')
    cHepa = Text(frame_complementario1, height=3, width=70)
    cHepa.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='FROTIS (raspado de piel):').grid(row=4, column=0, pady=10, sticky='e')
    frotis = Text(frame_complementario1, height=3, width=70)
    frotis.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='COPROLÓGICO:').grid(row=5, column=0, pady=10, sticky='e')
    copro = Text(frame_complementario1, height=3, width=70)
    copro.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='ENDOSCOPIA:').grid(row=6, column=0, pady=10, sticky='e')
    endos = Text(frame_complementario1, height=3, width=70)
    endos.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='ECG:').grid(row=7, column=0, pady=10, sticky='e')
    ecg = Text(frame_complementario1, height=3, width=70)
    ecg.grid(row=7, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='EEG:').grid(row=8, column=0, pady=10, sticky='e')
    eeg = Text(frame_complementario1, height=3, width=70)
    eeg.grid(row=8, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='PARCIAL DE ORINA:').grid(row=9, column=0, pady=10, sticky='e')
    pOri = Text(frame_complementario1, height=3, width=70)
    pOri.grid(row=9, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='COPROSCÓPICO:').grid(row=10, column=0, pady=10, sticky='e')
    copros = Text(frame_complementario1, height=3, width=70)
    copros.grid(row=10, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='CULTIVOS:').grid(row=11, column=0, pady=10, sticky='e')
    culti = Text(frame_complementario1, height=3, width=70)
    culti.grid(row=11, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='ANTIBIOGRAMA:').grid(row=12, column=0, pady=10, sticky='e')
    anti = Text(frame_complementario1, height=3, width=70)
    anti.grid(row=12, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='BIOPSIA:').grid(row=13, column=0, pady=10, sticky='e')
    biopsia = Text(frame_complementario1, height=3, width=70)
    biopsia.grid(row=13, column=1, padx=10, pady=10, sticky='w')
    Label(frame_complementario1, text='OTROS:').grid(row=14, column=0, pady=10, sticky='e')
    otros = Text(frame_complementario1, height=3, width=70)
    otros.grid(row=14, column=1, padx=10, pady=10, sticky='w')
    #CONCLUSIONES
    Label(frame_conclusionFinal1, text='DESCRIPCIÓN DE HALLAZGOS PRUEBAS DIAGNÓSTICO:').grid(row=0, column=0, pady=10, sticky='e')
    dHPD = Text(frame_conclusionFinal1, height=4, width=80)
    dHPD.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_conclusionFinal1, text='DIAGNÓSTICO FINAL O CONFIRMATIVO:').grid(row=1, column=0, pady=10, sticky='e')
    dFinal = Text(frame_conclusionFinal1, height=4, width=80)
    dFinal.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    #TRATAMIENTO-MEDICO
    Label(frame_medico1, text='NOMBRE:').grid(row=0, column=0, pady=10, sticky='e')
    mNombre=Entry(frame_medico1, width=30)
    mNombre.grid(row=0, column=1, padx=10, sticky='w')
    Label(frame_medico1, text='APELLIDO:').grid(row=0, column=2, pady=10, sticky='e')
    mApe=Entry(frame_medico1, width=40)
    mApe.grid(row=0, column=3, padx=10, sticky='w')
    Label(frame_medico1, text='MATRÍCULA\nPROFESIONAL/CÓDIGO:').grid(row=1, column=0, pady=10, sticky='e')
    mMatri=Entry(frame_medico1)
    mMatri.grid(row=1, column=1, columnspan=3, padx=10, sticky='we')
    #TRATAMIENTO-DETALLES
    Label(frame_detalles, text='TIPO DE TRATAMIENTO:').grid(row=0, column=0, pady=10, sticky='e')
    tTrata = Text(frame_detalles, height=2, width=50)
    tTrata.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='PRODUCTO BASE:').grid(row=1, column=0, pady=10, sticky='e')
    pBase=Text(frame_detalles, height=2, width=50)
    pBase.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='DOSIS BÁSICA:').grid(row=2, column=0, pady=10, sticky='e')
    dBasi=Text(frame_detalles, height=2, width=50)
    dBasi.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='PRESENTACIÓN:').grid(row=3, column=0, pady=10, sticky='e')
    presen=Text(frame_detalles, height=2, width=50)
    presen.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='VÍA:').grid(row=4, column=0, pady=10, sticky='e')
    via=Text(frame_detalles, height=2, width=50)
    via.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='FRECUENCIA:').grid(row=5, column=0, pady=10, sticky='e')
    frecu=Text(frame_detalles, height=2, width=50)
    frecu.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    Label(frame_detalles, text='DURACIÓN:').grid(row=6, column=0, pady=10, sticky='e')
    dura=Text(frame_detalles, height=2, width=50)
    dura.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    #global botonActualizar,botonEliminar
    #Boton en frame_d
    #botonActualizar= Button(frame_d, text='ACTUALIZAR', bg='green', fg='white')
    #botonActualizar.pack(side=RIGHT, padx=30, pady=2, ipadx=15, ipady=3)
    #botonEliminar= Button(frame_d, text='ELIMINAR', bg='red',fg='white', command=Eliminar)
    #botonEliminar.pack(side=RIGHT, padx=5, pady=2)

#-------------------------------------------------------------------------------------------------------------------
def Read():
    print('--------------------Read--------------------')
    seleccion = tabla.selection()#--- Fila seleccionada
    if seleccion:
        
        print('1 estadoRoot2 :',estadoRoot2)
        if not estadoRoot2:# not False = True --- Comprueba que ventana este cerrada (False)
            nuevaVentana()
            
            diccionario = tabla.item(seleccion[0])#---Guarda fila en diccionario
            print("---Fila seleccionada:", diccionario)
            global tablaDni
            tablaDni = diccionario['text']#--Extraes DNI
            tablaHc = diccionario['values'][4]#--Extraes H.C
            print('---DNI',type(tablaDni),tablaDni)
            print('---Nº H.C',type(tablaHc),tablaHc)
            
            #--- Abre cursorSQL | extraccionDatosSQL() | cierra cursorSQL | ventanaERROR
            try:
                #--- Conexión con mysql ---
                conexion=mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='dog_barber'
                )
                cursorSQL=conexion.cursor()
                
                #--- Consultar a SQL el indice del propietario con DNI e H.C ---
                consul = '''SELECT propietario.ID_PROPIETARIO FROM dog_barber.propietario
                INNER JOIN historia_clinica ON propietario.ID_PROPIETARIO = historia_clinica.ID_HC
                WHERE propietario.DNI=%s AND historia_clinica.N_HC=%s;'''
                cursorSQL.execute(consul,(tablaDni,tablaHc))
                indicePropi = cursorSQL.fetchall()
                global indice
                indice = indicePropi[0][0]#--- INDICE
                print('---indice mysql obtenido con DNI y H.C :',indice)
            
                cursorSQL.close()
                conexion.close()
                
                extraccionDatosSQL()
                borrarDatos()
                asignarDatos()
                datosEnTabla2()#--- Abre cursor | extrae datosSQL x globalDni | cierra cursor | ventanaERROR
                
            except Exception as error:
                print(error)
                tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')        
            
        else:
            root2.focus()

def Create():
    print('1 estadoRoot2 :',estadoRoot2)
    if not estadoRoot2:
        nuevaVentana()
        deshabilitar()
    else:
        root2.focus()
    
#-------------------- FUNCIONES EXTRAS -------------------- FUNCIONES EXTRAS -----------------------------------

#--- READ ---
        
#--- Extraccion datos SQL
def extraccionDatosSQL():
    
    try:
        print('--------------------Extraccion datos SQL--------------------')
        #--- Conexión con mysql ---
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursorSQL=conexion.cursor()
        
        global historia_clinica, paciente, propietario, anamnesis, desparasitacion, vacuna
        global examen_clinico, oys, stm, diferencial, problema, diagnostico
        global complementario, conclusion, tratamiento, medico
        
        #--- 1 Extraer la fila de tabla historia_clinica con el mismo INDICE ---
        consul1 = '''SELECT historia_clinica.* FROM dog_barber.historia_clinica
        WHERE historia_clinica.ID_HC=%s;'''
        cursorSQL.execute(consul1,(indice,))
        historia_clinica = cursorSQL.fetchall()
        historia_clinica = historia_clinica[0]
        print('historia_clinica',historia_clinica)

        #--- 2 Extraer la fila de tabla paciente con el mismo INDICE ---
        consul2 = '''SELECT paciente.* FROM dog_barber.paciente
        WHERE paciente.ID_PACIENTE=%s;'''
        cursorSQL.execute(consul2,(indice,))
        paciente = cursorSQL.fetchall()
        paciente = paciente[0]
        print('paciente',paciente)
        
        #--- 3 Extraer la fila de tabla propietario con el mismo INDICE ---
        consul3 = '''SELECT propietario.* FROM dog_barber.propietario
        WHERE propietario.ID_PROPIETARIO=%s;'''
        cursorSQL.execute(consul3,(indice,))
        propietario = cursorSQL.fetchall()
        propietario = propietario[0]
        print('propietario',propietario)
        
        #--- 4 Extraer la fila de tabla anamnesis con el mismo INDICE ---
        consul4 = '''SELECT anamnesis.* FROM dog_barber.anamnesis
        WHERE anamnesis.ID_ANAMNESIS=%s;'''
        cursorSQL.execute(consul4,(indice,))
        anamnesis = cursorSQL.fetchall()
        anamnesis = anamnesis[0]
        print('anamnesis',anamnesis)
        
        #--- 5 Extraer la fila de tabla desparasitacion con el mismo INDICE ---
        consul5 = '''SELECT desparasitacion.* FROM dog_barber.desparasitacion
        WHERE desparasitacion.ID_DESPARASITACION=%s;'''
        cursorSQL.execute(consul5,(indice,))
        desparasitacion = cursorSQL.fetchall()
        desparasitacion = desparasitacion[0]
        print('desparasitacion',desparasitacion)
        
        #--- 6 Extraer la fila de tabla vacuna con el mismo INDICE ---
        consul6 = '''SELECT vacuna.* FROM dog_barber.vacuna
        WHERE vacuna.ID_VACUNA=%s;'''
        cursorSQL.execute(consul6,(indice,))
        vacuna = cursorSQL.fetchall()
        vacuna = vacuna[0]
        print('vacuna',vacuna)
        
        #--- 7 Extraer la fila de tabla examen_clinico con el mismo INDICE ---
        consul7 = '''SELECT examen_clinico.* FROM dog_barber.examen_clinico
        WHERE examen_clinico.ID_CLINICO=%s;'''
        cursorSQL.execute(consul7,(indice,))
        examen_clinico = cursorSQL.fetchall()
        examen_clinico = examen_clinico[0]
        print('examen_clinico',examen_clinico)
        
        #--- 8 Extraer la fila de tabla oys con el mismo INDICE ---
        consul8 = '''SELECT oys.* FROM dog_barber.oys
        WHERE oys.ID_OYS=%s;'''
        cursorSQL.execute(consul8,(indice,))
        oys = cursorSQL.fetchall()
        oys = oys[0]
        print('oys',oys)
        
        #--- 9 Extraer la fila de tabla stm con el mismo INDICE ---
        consul9 = '''SELECT stm.* FROM dog_barber.stm
        WHERE stm.ID_STM=%s;'''
        cursorSQL.execute(consul9,(indice,))
        stm = cursorSQL.fetchall()
        stm = stm[0]
        print('stm',stm)
        
        #--- 10 Extraer la fila de tabla diferencial con el mismo INDICE ---
        consul10 = '''SELECT diferencial.* FROM dog_barber.diferencial
        WHERE diferencial.ID_DIFERENCIAL=%s;'''
        cursorSQL.execute(consul10,(indice,))
        diferencial = cursorSQL.fetchall()
        diferencial = diferencial[0]
        print('diferencial',diferencial)
        
        #--- 11 Extraer la fila de tabla problema con el mismo INDICE ---
        consul11 = '''SELECT problema.* FROM dog_barber.problema
        WHERE problema.ID_PROBLEMA=%s;'''
        cursorSQL.execute(consul11,(indice,))
        problema = cursorSQL.fetchall()
        problema = problema[0]
        print('problema',problema)
        
        #--- 12 Extraer la fila de tabla diagnostico con el mismo INDICE ---
        consul12 = '''SELECT diagnostico.* FROM dog_barber.diagnostico
        WHERE diagnostico.ID_DIAGNOSTICO=%s;'''
        cursorSQL.execute(consul12,(indice,))
        diagnostico = cursorSQL.fetchall()
        diagnostico = diagnostico[0]
        print('diagnostico',diagnostico)
        
        #--- 13 Extraer la fila de tabla complementario con el mismo INDICE ---
        consul13 = '''SELECT complementario.* FROM dog_barber.complementario
        WHERE complementario.ID_COMPLEMENTARIO=%s;'''
        cursorSQL.execute(consul13,(indice,))
        complementario = cursorSQL.fetchall()
        complementario = complementario[0]
        print('complementario',complementario)
        
        #--- 14 Extraer la fila de tabla conclusion con el mismo INDICE ---
        consul14 = '''SELECT conclusion.* FROM dog_barber.conclusion
        WHERE conclusion.ID_CONCLUSION=%s;'''
        cursorSQL.execute(consul14,(indice,))
        conclusion = cursorSQL.fetchall()
        conclusion = conclusion[0]
        print('conclusion',conclusion)
        
        #--- 15 Extraer la fila de tabla tratamiento con el mismo INDICE ---
        consul15 = '''SELECT tratamiento.* FROM dog_barber.tratamiento
        WHERE tratamiento.ID_TRATAMIENTO=%s;'''
        cursorSQL.execute(consul15,(indice,))
        tratamiento = cursorSQL.fetchall()
        tratamiento = tratamiento[0]
        print('tratamiento',tratamiento)
        
        #--- 16 Extraer la fila de tabla medico con el mismo INDICE ---
        consul16 = '''SELECT medico.* FROM dog_barber.medico
        WHERE medico.ID_MEDICO=%s;'''
        cursorSQL.execute(consul16,(indice,))
        medico = cursorSQL.fetchall()
        medico = medico[0]
        print('medico',medico)
        
        cursorSQL.close()
        conexion.close()
    
    except Exception as error:
        print(error)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')        
#--- Borrar datos de widgets ---
def borrarDatos():
    
    print('--------------------Borrar datos de widgets--------------------')
    #------ 1 Delete datos historia_clinica ------
    nHC.config(text = '')
    fHC.delete(0, END)
    
    #------ 2 Delete datos a widgets paciente ------
    nMasco.delete(0, END)
    mEspecie.delete(0, END)
    mRaza.delete(0, END)
    mSexo.delete(0, END)
    mPeso.delete(0, END)
    mNaci.delete(0, END)
    
    #------ 3 Delete datos a widgets propietario ------
    dni.destroy()
    nombreProp.delete(0, END)
    apellido.delete(0, END)
    nacimiento.delete(0, END)
    genero.delete(0, END)
    celular.delete(0, END)
    domicilio.delete(0, END)
    correo.delete(0, END)
    
    #------ 4 Delete datos a widgets anamnesis ------
    eAnte.delete("1.0", END)
    trata.delete("1.0", END)
    evo.delete("1.0", END)
    ali.delete("1.0", END)
    hRepro.delete("1.0", END)
    uCelo.delete(0, END)
    uParto.delete(0, END)
    mConsul.delete("1.0", END)
    
    #------ 5 Delete datos a widgets desparasitacion ------
    dProdu.delete(0, END)
    dFecha.delete(0, END)
    
    #------ 6 Delete datos a widgets vacuna ------
    vMarca.delete(0, END)
    vLote.delete(0, END)
    vFecha.delete(0, END)
    
    #------ 7 Delete a widgets examen_clinico ------
    fRespi.delete(0, END)
    lCapi.delete(0, END)
    fCardi.delete(0, END)
    gLinfa.delete(0, END)
    tempe.delete(0, END)
    muco.delete(0, END)
    pulso.delete(0, END)
    acti.delete(0, END)
    
    #------ 8 Delete datos a widgets oys ------
    eGene.delete("1.0", END)
    eHidra.delete("1.0", END)
    ojos.delete("1.0", END)
    oidos.delete("1.0", END)
    nariz.delete("1.0", END)
    dHalla.delete("1.0", END)
    
    #------ 9 Delete datos a widgets stm ------
    sTegu.delete("1.0", END)
    sDiges.delete("1.0", END)
    sRespi.delete("1.0", END)
    sNervi.delete("1.0", END)
    sMuscu.delete("1.0", END)
    sCardio.delete("1.0", END)
    sGeni.delete("1.0", END)
    
    #------ 10 Delete datos a widgets diferencial ------
    
    #------ 11 Delete datos a widgets problema ------
    proble1.delete("1.0", END)
    proble2.delete("1.0", END)
    proble3.delete("1.0", END)
    proble4.delete("1.0", END)
    proble5.delete("1.0", END)
    proble6.delete("1.0", END)
    proble7.delete("1.0", END)
    
    #------ 12 Delete datos a widgets diagnostico ------
    diag1.delete("1.0", END)
    diag2.delete("1.0", END)
    diag3.delete("1.0", END)
    diag4.delete("1.0", END)
    diag5.delete("1.0", END)
    diag6.delete("1.0", END)
    diag7.delete("1.0", END)
    
    #------ 13 Delete datos a widgets complementario ------
    qSangui.delete("1.0", END)
    rayosx.delete("1.0", END)
    eco.delete("1.0", END)
    cHepa.delete("1.0", END)
    frotis.delete("1.0", END)
    copro.delete("1.0", END)
    endos.delete("1.0", END)
    ecg.delete("1.0", END)
    eeg.delete("1.0", END)
    pOri.delete("1.0", END)
    copros.delete("1.0", END)
    culti.delete("1.0", END)
    anti.delete("1.0", END)
    biopsia.delete("1.0", END)
    otros.delete("1.0", END)
    
    #------ 14 Delete datos a widgets conclusion ------
    dHPD.delete("1.0", END)
    dFinal.delete("1.0", END)
    
    #------ 15 Delete datos a widgets tratamiento ------
    tTrata.delete("1.0", END)
    pBase.delete("1.0", END)
    dBasi.delete("1.0", END)
    presen.delete("1.0", END)
    via.delete("1.0", END)
    frecu.delete("1.0", END)
    dura.delete("1.0", END)
    
    #------ 16 Delete datos a widgets medico ------
    mNombre.delete(0, END)
    mApe.delete(0, END)
    mMatri.delete(0, END)
#--- Asignar datos a cada widget ---
def asignarDatos():
    
    print('--------------------Asignar datos a widgets--------------------')
    #------ 1 Insertar datos historia_clinica ------
    nHC.config(text = historia_clinica[1])
    fHC.insert(0, historia_clinica[2])
    
    #------ 2 Insertar datos a widgets paciente ------
    nMasco.insert(0, paciente[1])
    mEspecie.insert(0, paciente[2])
    mRaza.insert(0, paciente[3])
    mSexo.insert(0, paciente[4])
    mPeso.insert(0, paciente[5])
    mNaci.insert(0, paciente[6])
    
    #------ 3 Insertar datos a widgets propietario ------
    global dni
    dni=Label(frame_propi1, text= propietario[1])
    dni.grid(row=0, column=1, padx=10, sticky='w')
    nombreProp.insert(0, propietario[2])
    apellido.insert(0, propietario[3])
    nacimiento.insert(0, propietario[4])
    genero.insert(0, propietario[5])
    celular.insert(0, propietario[6])
    domicilio.insert(0, propietario[7])
    correo.insert(0, propietario[8])
    
    #------ 4 Insertar datos a widgets anamnesis ------
    eAnte.insert(END, anamnesis[1])
    trata.insert(END, anamnesis[2])
    evo.insert(END, anamnesis[3])
    ali.insert(END, anamnesis[4])
    hRepro.insert(END, anamnesis[5])
    uCelo.insert(0, anamnesis[6])
    uParto.insert(0, anamnesis[7])
    mConsul.insert(END, anamnesis[8])
    
    #------ 5 Insertar datos a widgets desparasitacion ------
    dProdu.insert(0, desparasitacion[1])
    dFecha.insert(0, desparasitacion[2])
    
    #------ 6 Insertar datos a widgets vacuna ------
    vMarca.insert(0, vacuna[1])
    vLote.insert(0, vacuna[2])
    vFecha.insert(0, vacuna[3])
    
    #------ 7 Insertar datos a widgets examen_clinico ------
    fRespi.insert(0, examen_clinico[1])
    lCapi.insert(0, examen_clinico[5])
    fCardi.insert(0, examen_clinico[2])
    gLinfa.insert(0, examen_clinico[6])
    tempe.insert(0, examen_clinico[3])
    muco.insert(0, examen_clinico[7])
    pulso.insert(0, examen_clinico[4])
    acti.insert(0, examen_clinico[8])
    
    #------ 8 Insertar datos a widgets oys ------
    eGene.insert(END, oys[1])
    eHidra.insert(END, oys[2])
    ojos.insert(END, oys[3])
    oidos.insert(END, oys[4])
    nariz.insert(END, oys[5])
    dHalla.insert(END, oys[7])
    
    #------ 9 Insertar datos a widgets stm ------
    sTegu.insert(END, stm[1])
    sDiges.insert(END, stm[2])
    sRespi.insert(END, stm[3])
    sNervi.insert(END, stm[4])
    sMuscu.insert(END, stm[5])
    sCardio.insert(END, stm[6])
    sGeni.insert(END, stm[7])
    
    #------ 10 Insertar datos a widgets diferencial ------
    
    #------ 11 Insertar datos a widgets problema ------
    proble1.insert(END, problema[1])
    proble2.insert(END, problema[2])
    proble3.insert(END, problema[3])
    proble4.insert(END, problema[4])
    proble5.insert(END, problema[5])
    proble6.insert(END, problema[6])
    proble7.insert(END, problema[7])
    
    #------ 12 Insertar datos a widgets diagnostico ------
    diag1.insert(END, diagnostico[1])
    diag2.insert(END, diagnostico[2])
    diag3.insert(END, diagnostico[3])
    diag4.insert(END, diagnostico[4])
    diag5.insert(END, diagnostico[5])
    diag6.insert(END, diagnostico[6])
    diag7.insert(END, diagnostico[7])
    
    #------ 13 Insertar datos a widgets complementario ------
    qSangui.insert(END, complementario[1])
    rayosx.insert(END, complementario[2])
    eco.insert(END, complementario[3])
    cHepa.insert(END, complementario[4])
    frotis.insert(END, complementario[5])
    copro.insert(END, complementario[6])
    endos.insert(END, complementario[7])
    ecg.insert(END, complementario[8])
    eeg.insert(END, complementario[9])
    pOri.insert(END, complementario[10])
    copros.insert(END, complementario[11])
    culti.insert(END, complementario[12])
    anti.insert(END, complementario[13])
    biopsia.insert(END, complementario[14])
    otros.insert(END, complementario[15])
    
    #------ 14 Insertar datos a widgets conclusion ------
    dHPD.insert(END, conclusion[1])
    dFinal.insert(END, conclusion[2])
    
    #------ 15 Insertar datos a widgets tratamiento ------
    tTrata.insert(END, tratamiento[2])
    pBase.insert(END, tratamiento[3])
    dBasi.insert(END, tratamiento[4])
    presen.insert(END, tratamiento[5])
    via.insert(END, tratamiento[6])
    frecu.insert(END, tratamiento[7])
    dura.insert(END, tratamiento[8])
    
    #------ 16 Insertar datos a widgets medico ------
    mNombre.insert(0, medico[1])
    mApe.insert(0, medico[2])
    mMatri.insert(0, medico[3])
#--- Traer datos (H.C's y FECHAS) a Treeview2 ---
def datosEnTabla2():
    
    try:
        print('--------------------Asignar datos a Tabla2--------------------')
        #--- Conexión con mysql ---
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursor=conexion.cursor()
        
        #--- Consultar a MySQL todos los H.C según el dni del Treeview ---
        consulB = '''SELECT historia_clinica.ID_HC,N_HC, FECHA, propietario.NOMBRE
        FROM dog_barber.historia_clinica INNER JOIN propietario
        ON historia_clinica.ID_HC = propietario.ID_PROPIETARIO
        WHERE propietario.DNI=%s AND historia_clinica.N_HC>=1;'''
        cursor.execute(consulB,(tablaDni,)) #---trae los datos de las filas de las tabla unida
        global filas2
        filas2 = cursor.fetchall()#----Guarda las filas unidas en variables
        print('Datos en Tabla2 :',filas2)
        
        #--- Lista de Nº de H.C
        global filasnhc
        filasnhc = []
        for i in filas2:
            print('Tupla :',i)
            print('Nº H.C :',i[1])
            filasnhc.append(int(i[1]))
        print('Lista de Nº H.C :',filasnhc)        
        
        #--- Insertar datos en Treeview2 ---
        for i in filas2:
            tabla2.insert('', 0, text=i[1], values=i[2])
        
        cursor.close()
        conexion.close()
        
    except Exception as error:
        print(error)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')


#--- Abir --- 
def Abrir():
    
    print('-------------------------------Abrir-------------------------------------------------')
    seleccion = tabla2.selection()#---Fila seleccionada
    if seleccion:
        diccionario = tabla2.item(seleccion[0])#---Guarda fila en diccionario
        print("---Fila seleccionada :", diccionario)
        tablaHc = diccionario['text']#--Extraes nuevo H.C
        print('---nuevo H.C :',type(tablaHc),tablaHc)
        
        print('1---estadoBoton :',estadoBoton)
        if estadoBoton:
            borrarbotonGuardar()
        
        try:
            #--- Conexión con mysql ---
            conexion=mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='dog_barber'
            )
            cursorSQL=conexion.cursor()
            
            #--- Consultar a SQL el indice del propietario con DNI e H.C ---
            consul = '''SELECT propietario.ID_PROPIETARIO FROM dog_barber.propietario
            INNER JOIN historia_clinica ON propietario.ID_PROPIETARIO = historia_clinica.ID_HC
            WHERE propietario.DNI=%s AND historia_clinica.N_HC=%s;'''
            cursorSQL.execute(consul,(tablaDni,tablaHc))
            indicePropi = cursorSQL.fetchall()
            global indice
            indice = indicePropi[0][0]#--- nuevo INDICE
            print('---indice mysql obtenido con DNI y nuevo H.C :',indice)
            
            cursorSQL.close()
            conexion.close()
            
            extraccionDatosSQL()
            borrarDatos()
            asignarDatos()
        
        except Exception as error:
            print(error)
            tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')

#--- Nuevo ---
def Nuevo():
    
    print('--------------------Nuevo--------------------')
    print('1---estadoBoton',estadoBoton)
    if not estadoBoton:
        print('----------Crear Boton----------')
        crearbotonGuardar()
        borrarDatos()
        
        #--- Obtener nuevo Nº H.C
        maximo = max(filasnhc)
        nuevoHC = maximo + 1
        print('maximoHC :',maximo)
        print('nuevoHC :',nuevoHC)
        
        print('----------Conexion con mysql----------')
        #--- Conexión con mysql ---
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursor=conexion.cursor()
    
        
        #--- Consultar a MySQL útimo historia_clinica , propietario y paciente ---
        consul = '''SELECT *
        FROM dog_barber.historia_clinica 
        INNER JOIN paciente
        ON historia_clinica.ID_HC = paciente.ID_PACIENTE
        INNER JOIN propietario
        ON historia_clinica.ID_HC = propietario.ID_PROPIETARIO
        WHERE propietario.DNI=%s AND historia_clinica.N_HC=%s;'''
        cursor.execute(consul,(tablaDni,maximo)) #---trae los datos de las filas de las tabla unida
        ultimaFila = cursor.fetchall()#----Guarda las filas unidas en variables
        ultimaFila = ultimaFila[0]
        print('ultimaFila :',ultimaFila)
        
        cursor.close()
        conexion.close()

        
        print('----------Insertar nuevos datos----------')
        #------ 1 Insertar datos historia_clinica ------
        nHC.config(text = nuevoHC)
    
        #------ 2 Insertar datos a widgets paciente ------
        nMasco.insert(0, ultimaFila[12])
        mEspecie.insert(0, ultimaFila[13])
        mRaza.insert(0, ultimaFila[14])
        mSexo.insert(0, ultimaFila[15])
        mPeso.insert(0, ultimaFila[16]) 
        mNaci.insert(0, ultimaFila[17])
    
        #------ 3 Insertar datos a widgets propietario ------
        global dni
        dni=Label(frame_propi1, text= ultimaFila[19])
        dni.grid(row=0, column=1, padx=10, sticky='w')
        nombreProp.insert(0, ultimaFila[20])
        apellido.insert(0, ultimaFila[21])
        nacimiento.insert(0, ultimaFila[22])
        genero.insert(0, ultimaFila[23])
        celular.insert(0, ultimaFila[24])
        domicilio.insert(0, ultimaFila[25])
        correo.insert(0, ultimaFila[26])    

estadoBoton = False
def crearbotonGuardar():
    #crear boton Guardar2
    global estadoBoton
    estadoBoton = True
    print('2---estadoBoton :',estadoBoton)
    #--- Añadir Boton ---
    global botonGuardar
    botonGuardar= Button(frame_d, text='GUARDAR', bg='green', fg='white', command=Guardar2)
    botonGuardar.pack(side=RIGHT, padx=30, pady=2, ipadx=15, ipady=3)

def borrarbotonGuardar():
    botonGuardar.destroy()
    print('--- Boton destruido---')
    global estadoBoton
    estadoBoton = False
    print('3---estadoBoton :',estadoBoton)

def guardarDatosLabelEnSQL():
    try:
        #Conexión con mysql    
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursor=conexion.cursor()#----Cursor para realizar consultas
        
        
        #------NUEVO indice de TABLA SQL después del último disponible en columna------------------------------------------------------
        cursor.execute("SELECT ID_HC FROM historia_clinica")#---Consulta para seleccionar la columna de la tabla
        valores = [ID[0] for ID in cursor.fetchall()]#---Recuperar los valores de la columna
        print(valores)
        if valores:
            mayor = max(valores)#---Identificar el número mayor
            nuevoID = mayor+1#---Nuevo ID de tabla
            print(mayor)
        else:
            nuevoID = 1
        print(nuevoID)#---Imprimir el nuevo ID de tabla
        #------------------------------------------------------------------------------------------------------------
        
        #tabla MySQL y widgets que capturan su valor
        tablaHC = 'ID_HC,N_HC,FECHA,ID_PACIENTE,ID_PROPIETARIO,ID_ANAMNESIS,ID_CLINICO,ID_DIFERENCIAL,ID_COMPLEMENTARIO,ID_CONCLUSION,ID_TRATAMIENTO'
        valuesHC = f"'{nuevoID}','{nHC.cget('text')}','{fHC.get()}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}'"
        tablaPaci = 'ID_PACIENTE,MASCOTA,ESPECIE,RAZA,SEXO,PESO,NACIMIENTO'
        valuesPaci = f"'{nuevoID}','{nMasco.get()}','{mEspecie.get()}','{mRaza.get()}','{mSexo.get()}','{mPeso.get()}','{mNaci.get()}'"
        tablaPropi = 'ID_PROPIETARIO,DNI,NOMBRE,APELLIDO,NACIMIENTO,GENERO,CELULAR,DOMICILIO,CORREO'
        valuesPropi = f"'{nuevoID}','{dni.cget('text')}','{nombreProp.get()}','{apellido.get()}','{nacimiento.get()}','{genero.get()}','{celular.get()}','{domicilio.get()}','{correo.get()}'"
        tablaAnam = 'ID_ANAMNESIS,ENFERMEDADES_ANTERIORES,TRATAMIENTOS,EVOLUCION,ALIMENTACION,HISTORIA_REPRODUCTIVA,ULTIMO_CELO,ULTIMO_PARTO,MOTIVO_CONSULTA,ID_DESPARASITACION,ID_VACUNA'
        valuesAnam = f"'{nuevoID}','{eAnte.get('1.0',END)}','{trata.get('1.0',END)}','{evo.get('1.0',END)}','{ali.get('1.0',END)}','{hRepro.get('1.0',END)}','{uCelo.get()}','{uParto.get()}','{mConsul.get('1.0',END)}','{nuevoID}','{nuevoID}'"
        tablaDespa = 'ID_DESPARASITACION,PRODUCTO,FECHA'
        valuesDespa = f"'{nuevoID}','{dProdu.get()}','{dFecha.get()}'"
        tablaVacu = 'ID_VACUNA,MARCA,LOTE,FECHA'
        valuesVacu = f"'{nuevoID}','{vMarca.get()}','{vLote.get()}','{vFecha.get()}'"
        tablaClini = 'ID_CLINICO,FRECUENCIA_RESPIRATORIA,FRECUENCIA_CARDIACA,TEMPERATURA,PULSO,LLENADO_CAPILAR,GANGLIOS_LINFATICOS,MUCOSAS,ACTITUD,ID_OYS'
        valuesClini = f"'{nuevoID}','{fRespi.get()}','{fCardi.get()}','{tempe.get()}','{pulso.get()}','{lCapi.get()}','{gLinfa.get()}','{muco.get()}','{acti.get()}','{nuevoID}'"
        tablaOys = 'ID_OYS,ESTADO_GENERAL,ESTADO_HIDRATACION,OJOS,OIDOS,NARIZ,ID_STM,DESCRIPCION_HALLAZGOS'
        valuesOys = f"'{nuevoID}','{eGene.get('1.0',END)}','{eHidra.get('1.0',END)}','{ojos.get('1.0',END)}','{oidos.get('1.0',END)}','{nariz.get('1.0',END)}','{nuevoID}','{dHalla.get('1.0',END)}'"
        tablaStm = 'ID_STM,STM_TEGUMENTARIO,STM_DIGESTIVO,STM_RESPIRATORIO,STM_NERVIOSO,STM_MUSCULO_ESQUELETICO,STM_CARDIOVASCULAR,STM_GENITOURINARIO'
        valuesStm = f"'{nuevoID}','{sTegu.get('1.0',END)}','{sDiges.get('1.0',END)}','{sRespi.get('1.0',END)}','{sNervi.get('1.0',END)}','{sMuscu.get('1.0',END)}','{sCardio.get('1.0',END)}','{sGeni.get('1.0',END)}'"
        tablaDife = 'ID_DIFERENCIAL,ID_PROBLEMA,ID_DIAGNOSTICO'
        valuesDife = f"'{nuevoID}','{nuevoID}','{nuevoID}'"
        tablaProble = 'ID_PROBLEMA,PROBLEMA1,PROBLEMA2,PROBLEMA3,PROBLEMA4,PROBLEMA5,PROBLEMA6,PROBLEMA7'
        valuesProble = f"'{nuevoID}','{proble1.get('1.0',END)}','{proble2.get('1.0',END)}','{proble3.get('1.0',END)}','{proble4.get('1.0',END)}','{proble5.get('1.0',END)}','{proble6.get('1.0',END)}','{proble7.get('1.0',END)}'"
        tablaDiag = 'ID_DIAGNOSTICO,DIAGNOSTICO1,DIAGNOSTICO2,DIAGNOSTICO3,DIAGNOSTICO4,DIAGNOSTICO5,DIAGNOSTICO6,DIAGNOSTICO7'
        valuesDiag = f"'{nuevoID}','{diag1.get('1.0',END)}','{diag2.get('1.0',END)}','{diag3.get('1.0',END)}','{diag4.get('1.0',END)}','{diag5.get('1.0',END)}','{diag6.get('1.0',END)}','{diag7.get('1.0',END)}'"
        tablaComple = 'ID_COMPLEMENTARIO,QUIMICA_SANGUINEA,RAYOS_X,ECOGRAFIA,CUADRO_HEPATICO,FROTIS,COPROLOGICO,ENDOSCOPIA,ECG,EEG,PARCIAL_ORINA,COPROSCOPICO,CULTIVOS,ANTIBIOGRAMA,BIOPSIA,OTROS'
        valuesComple = f"'{nuevoID}','{qSangui.get('1.0',END)}','{rayosx.get('1.0',END)}','{eco.get('1.0',END)}','{cHepa.get('1.0',END)}','{frotis.get('1.0',END)}','{copro.get('1.0',END)}','{endos.get('1.0',END)}','{ecg.get('1.0',END)}','{eeg.get('1.0',END)}','{pOri.get('1.0',END)}','{copros.get('1.0',END)}','{culti.get('1.0',END)}','{anti.get('1.0',END)}','{biopsia.get('1.0',END)}','{otros.get('1.0',END)}'"
        tablaConclu = 'ID_CONCLUSION,DESCRIPCION_HALLAZGOS_PRUEBAS_DIAGNOSTICO,DIAGNOSTICO_FINAL'
        valuesConclu = f"'{nuevoID}','{dHPD.get('1.0',END)}','{dFinal.get('1.0',END)}'"
        tablaTrata = 'ID_TRATAMIENTO,ID_MEDICO,TIPO_TRATAMIENTO,PRODUCTO_BASE,DOSIS_BASICA,PRESENTACION,VIA,FRECUENCIA,DURACION'
        valuesTrata = f"'{nuevoID}','{nuevoID}','{tTrata.get('1.0',END)}','{pBase.get('1.0',END)}','{dBasi.get('1.0',END)}','{presen.get('1.0',END)}','{via.get('1.0',END)}','{frecu.get('1.0',END)}','{dura.get('1.0',END)}'"
        tablaMedi = 'ID_MEDICO,NOMBRE,APELLIDO,MATRICULA_PROFESIONAL_CODIGO'
        valuesMedi = f"'{nuevoID}','{mNombre.get()}','{mApe.get()}','{mMatri.get()}'"
        
        #insert into dog_barber.propietario({}) values({})
        sqlHC = f"insert into dog_barber.historia_clinica({tablaHC}) values({valuesHC})"
        sqlPaci = f"insert into dog_barber.paciente({tablaPaci}) values({valuesPaci})"
        sqlPropi = f"insert into dog_barber.propietario({tablaPropi}) values({valuesPropi})"
        sqlAnam = f"insert into dog_barber.anamnesis({tablaAnam}) values({valuesAnam})"
        sqlDespa = f"insert into dog_barber.desparasitacion({tablaDespa}) values({valuesDespa})"
        sqlVacu = f"insert into dog_barber.vacuna({tablaVacu}) values({valuesVacu})"
        sqlClini = f"insert into dog_barber.examen_clinico({tablaClini}) values({valuesClini})"
        sqlOys = f"insert into dog_barber.oys({tablaOys}) values({valuesOys})"
        sqlStm = f"insert into dog_barber.stm({tablaStm}) values({valuesStm})"
        sqlDife = f"insert into dog_barber.diferencial({tablaDife}) values({valuesDife})"
        sqlProble = f"insert into dog_barber.problema({tablaProble}) values({valuesProble})"
        sqlDiag = f"insert into dog_barber.diagnostico({tablaDiag}) values({valuesDiag})"
        sqlComple = f"insert into dog_barber.complementario({tablaComple}) values({valuesComple})"
        sqlConclu = f"insert into dog_barber.conclusion({tablaConclu}) values({valuesConclu})"
        sqlTrata = f"insert into dog_barber.tratamiento({tablaTrata}) values({valuesTrata})"
        sqlMedi = f"insert into dog_barber.medico({tablaMedi}) values({valuesMedi})"
        
        cursor.execute(sqlHC)#----Ejecuta Consulta para insertar datos
        cursor.execute(sqlPaci)
        cursor.execute(sqlPropi)
        cursor.execute(sqlAnam)
        cursor.execute(sqlDespa)
        cursor.execute(sqlVacu)
        cursor.execute(sqlClini)
        cursor.execute(sqlOys)
        cursor.execute(sqlStm)
        cursor.execute(sqlDife)
        cursor.execute(sqlProble)
        cursor.execute(sqlDiag)
        cursor.execute(sqlComple)
        cursor.execute(sqlConclu)
        cursor.execute(sqlTrata)
        cursor.execute(sqlMedi)
        
        conexion.commit()#---Confirma
        cursor.close()
        conexion.close()
        tkinter.messagebox.showinfo('AVISO!','Se guardó con éxito')
        cierreRoot2()
    
    except mysql.connector.errors.DatabaseError as errormysql: 
        print(errormysql)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{errormysql}\n\nNo estás conectado a la base de datos')
    #except Exception as error:
    #    print(error)
    #    tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')

def Guardar2():
    if fHC.get()!='' and nombreProp.get()!='' and apellido.get()!='' and celular.get()!='' and nMasco.get()!='':
        guardarDatosLabelEnSQL()        
    else:
        tkinter.messagebox.showinfo('AVISO!','Es obligatorio que llenes la FECHA, los datos del PACIENTE y del PROPIETARIO')
        root2.focus()


#--- CREATE ---
def deshabilitar():
    #crear boton Guardar1
    botonGuardar= Button(frame_d, text='GUARDAR', bg='green', fg='white', command=Guardar1)
    botonGuardar.pack(side=RIGHT, padx=30, pady=2, ipadx=15, ipady=3)
    frame_tabla.destroy()

def Guardar1(): 
    if fHC.get()!='' and dni.get()!='' and nombreProp.get()!='' and apellido.get()!='' and celular.get()!='' and nMasco.get()!='':
        guardarDatosEnSQL()        
    else:
        tkinter.messagebox.showinfo('AVISO!','Es obligatorio que llenes la FECHA, los datos del PACIENTE y del PROPIETARIO')
        root2.focus()

def guardarDatosEnSQL():
    try:
        #Conexión con mysql    
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dog_barber'
        )
        cursor=conexion.cursor()#----Cursor para realizar consultas
        
        
        #------NUEVO indice de TABLA SQL después del último disponible en columna------------------------------------------------------
        cursor.execute("SELECT ID_HC FROM historia_clinica")#---Consulta para seleccionar la columna de la tabla
        valores = [ID[0] for ID in cursor.fetchall()]#---Recuperar los valores de la columna
        print(valores)
        if valores:
            mayor = max(valores)#---Identificar el número mayor
            nuevoID = mayor+1#---Nuevo ID de tabla
            print(mayor)
        else:
            nuevoID = 1
        print(nuevoID)#---Imprimir el nuevo ID de tabla
        #------------------------------------------------------------------------------------------------------------
        
        #tabla MySQL y widgets que capturan su valor
        tablaHC = 'ID_HC,N_HC,FECHA,ID_PACIENTE,ID_PROPIETARIO,ID_ANAMNESIS,ID_CLINICO,ID_DIFERENCIAL,ID_COMPLEMENTARIO,ID_CONCLUSION,ID_TRATAMIENTO'
        valuesHC = f"'{nuevoID}','{nHC.cget('text')}','{fHC.get()}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}','{nuevoID}'"
        tablaPaci = 'ID_PACIENTE,MASCOTA,ESPECIE,RAZA,SEXO,PESO,NACIMIENTO'
        valuesPaci = f"'{nuevoID}','{nMasco.get()}','{mEspecie.get()}','{mRaza.get()}','{mSexo.get()}','{mPeso.get()}','{mNaci.get()}'"
        tablaPropi = 'ID_PROPIETARIO,DNI,NOMBRE,APELLIDO,NACIMIENTO,GENERO,CELULAR,DOMICILIO,CORREO'
        valuesPropi = f"'{nuevoID}','{dni.get()}','{nombreProp.get()}','{apellido.get()}','{nacimiento.get()}','{genero.get()}','{celular.get()}','{domicilio.get()}','{correo.get()}'"
        tablaAnam = 'ID_ANAMNESIS,ENFERMEDADES_ANTERIORES,TRATAMIENTOS,EVOLUCION,ALIMENTACION,HISTORIA_REPRODUCTIVA,ULTIMO_CELO,ULTIMO_PARTO,MOTIVO_CONSULTA,ID_DESPARASITACION,ID_VACUNA'
        valuesAnam = f"'{nuevoID}','{eAnte.get('1.0',END)}','{trata.get('1.0',END)}','{evo.get('1.0',END)}','{ali.get('1.0',END)}','{hRepro.get('1.0',END)}','{uCelo.get()}','{uParto.get()}','{mConsul.get('1.0',END)}','{nuevoID}','{nuevoID}'"
        tablaDespa = 'ID_DESPARASITACION,PRODUCTO,FECHA'
        valuesDespa = f"'{nuevoID}','{dProdu.get()}','{dFecha.get()}'"
        tablaVacu = 'ID_VACUNA,MARCA,LOTE,FECHA'
        valuesVacu = f"'{nuevoID}','{vMarca.get()}','{vLote.get()}','{vFecha.get()}'"
        tablaClini = 'ID_CLINICO,FRECUENCIA_RESPIRATORIA,FRECUENCIA_CARDIACA,TEMPERATURA,PULSO,LLENADO_CAPILAR,GANGLIOS_LINFATICOS,MUCOSAS,ACTITUD,ID_OYS'
        valuesClini = f"'{nuevoID}','{fRespi.get()}','{fCardi.get()}','{tempe.get()}','{pulso.get()}','{lCapi.get()}','{gLinfa.get()}','{muco.get()}','{acti.get()}','{nuevoID}'"
        tablaOys = 'ID_OYS,ESTADO_GENERAL,ESTADO_HIDRATACION,OJOS,OIDOS,NARIZ,ID_STM,DESCRIPCION_HALLAZGOS'
        valuesOys = f"'{nuevoID}','{eGene.get('1.0',END)}','{eHidra.get('1.0',END)}','{ojos.get('1.0',END)}','{oidos.get('1.0',END)}','{nariz.get('1.0',END)}','{nuevoID}','{dHalla.get('1.0',END)}'"
        tablaStm = 'ID_STM,STM_TEGUMENTARIO,STM_DIGESTIVO,STM_RESPIRATORIO,STM_NERVIOSO,STM_MUSCULO_ESQUELETICO,STM_CARDIOVASCULAR,STM_GENITOURINARIO'
        valuesStm = f"'{nuevoID}','{sTegu.get('1.0',END)}','{sDiges.get('1.0',END)}','{sRespi.get('1.0',END)}','{sNervi.get('1.0',END)}','{sMuscu.get('1.0',END)}','{sCardio.get('1.0',END)}','{sGeni.get('1.0',END)}'"
        tablaDife = 'ID_DIFERENCIAL,ID_PROBLEMA,ID_DIAGNOSTICO'
        valuesDife = f"'{nuevoID}','{nuevoID}','{nuevoID}'"
        tablaProble = 'ID_PROBLEMA,PROBLEMA1,PROBLEMA2,PROBLEMA3,PROBLEMA4,PROBLEMA5,PROBLEMA6,PROBLEMA7'
        valuesProble = f"'{nuevoID}','{proble1.get('1.0',END)}','{proble2.get('1.0',END)}','{proble3.get('1.0',END)}','{proble4.get('1.0',END)}','{proble5.get('1.0',END)}','{proble6.get('1.0',END)}','{proble7.get('1.0',END)}'"
        tablaDiag = 'ID_DIAGNOSTICO,DIAGNOSTICO1,DIAGNOSTICO2,DIAGNOSTICO3,DIAGNOSTICO4,DIAGNOSTICO5,DIAGNOSTICO6,DIAGNOSTICO7'
        valuesDiag = f"'{nuevoID}','{diag1.get('1.0',END)}','{diag2.get('1.0',END)}','{diag3.get('1.0',END)}','{diag4.get('1.0',END)}','{diag5.get('1.0',END)}','{diag6.get('1.0',END)}','{diag7.get('1.0',END)}'"
        tablaComple = 'ID_COMPLEMENTARIO,QUIMICA_SANGUINEA,RAYOS_X,ECOGRAFIA,CUADRO_HEPATICO,FROTIS,COPROLOGICO,ENDOSCOPIA,ECG,EEG,PARCIAL_ORINA,COPROSCOPICO,CULTIVOS,ANTIBIOGRAMA,BIOPSIA,OTROS'
        valuesComple = f"'{nuevoID}','{qSangui.get('1.0',END)}','{rayosx.get('1.0',END)}','{eco.get('1.0',END)}','{cHepa.get('1.0',END)}','{frotis.get('1.0',END)}','{copro.get('1.0',END)}','{endos.get('1.0',END)}','{ecg.get('1.0',END)}','{eeg.get('1.0',END)}','{pOri.get('1.0',END)}','{copros.get('1.0',END)}','{culti.get('1.0',END)}','{anti.get('1.0',END)}','{biopsia.get('1.0',END)}','{otros.get('1.0',END)}'"
        tablaConclu = 'ID_CONCLUSION,DESCRIPCION_HALLAZGOS_PRUEBAS_DIAGNOSTICO,DIAGNOSTICO_FINAL'
        valuesConclu = f"'{nuevoID}','{dHPD.get('1.0',END)}','{dFinal.get('1.0',END)}'"
        tablaTrata = 'ID_TRATAMIENTO,ID_MEDICO,TIPO_TRATAMIENTO,PRODUCTO_BASE,DOSIS_BASICA,PRESENTACION,VIA,FRECUENCIA,DURACION'
        valuesTrata = f"'{nuevoID}','{nuevoID}','{tTrata.get('1.0',END)}','{pBase.get('1.0',END)}','{dBasi.get('1.0',END)}','{presen.get('1.0',END)}','{via.get('1.0',END)}','{frecu.get('1.0',END)}','{dura.get('1.0',END)}'"
        tablaMedi = 'ID_MEDICO,NOMBRE,APELLIDO,MATRICULA_PROFESIONAL_CODIGO'
        valuesMedi = f"'{nuevoID}','{mNombre.get()}','{mApe.get()}','{mMatri.get()}'"
        
        #insert into dog_barber.propietario({}) values({})
        sqlHC = f"insert into dog_barber.historia_clinica({tablaHC}) values({valuesHC})"
        sqlPaci = f"insert into dog_barber.paciente({tablaPaci}) values({valuesPaci})"
        sqlPropi = f"insert into dog_barber.propietario({tablaPropi}) values({valuesPropi})"
        sqlAnam = f"insert into dog_barber.anamnesis({tablaAnam}) values({valuesAnam})"
        sqlDespa = f"insert into dog_barber.desparasitacion({tablaDespa}) values({valuesDespa})"
        sqlVacu = f"insert into dog_barber.vacuna({tablaVacu}) values({valuesVacu})"
        sqlClini = f"insert into dog_barber.examen_clinico({tablaClini}) values({valuesClini})"
        sqlOys = f"insert into dog_barber.oys({tablaOys}) values({valuesOys})"
        sqlStm = f"insert into dog_barber.stm({tablaStm}) values({valuesStm})"
        sqlDife = f"insert into dog_barber.diferencial({tablaDife}) values({valuesDife})"
        sqlProble = f"insert into dog_barber.problema({tablaProble}) values({valuesProble})"
        sqlDiag = f"insert into dog_barber.diagnostico({tablaDiag}) values({valuesDiag})"
        sqlComple = f"insert into dog_barber.complementario({tablaComple}) values({valuesComple})"
        sqlConclu = f"insert into dog_barber.conclusion({tablaConclu}) values({valuesConclu})"
        sqlTrata = f"insert into dog_barber.tratamiento({tablaTrata}) values({valuesTrata})"
        sqlMedi = f"insert into dog_barber.medico({tablaMedi}) values({valuesMedi})"
        
        cursor.execute(sqlHC)#----Ejecuta Consulta para insertar datos
        cursor.execute(sqlPaci)
        cursor.execute(sqlPropi)
        cursor.execute(sqlAnam)
        cursor.execute(sqlDespa)
        cursor.execute(sqlVacu)
        cursor.execute(sqlClini)
        cursor.execute(sqlOys)
        cursor.execute(sqlStm)
        cursor.execute(sqlDife)
        cursor.execute(sqlProble)
        cursor.execute(sqlDiag)
        cursor.execute(sqlComple)
        cursor.execute(sqlConclu)
        cursor.execute(sqlTrata)
        cursor.execute(sqlMedi)
        
        conexion.commit()#---Confirma
        cursor.close()
        conexion.close()
        tkinter.messagebox.showinfo('AVISO!','Se guardó con éxito')
        cierreRoot2()
    
    except mysql.connector.errors.DatabaseError as errormysql: 
        print(errormysql)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{errormysql}\n\nNo estás conectado a la base de datos')
    except Exception as error:
        print(error)
        tkinter.messagebox.showerror('ERROR', f'Ocurrió un error!\n\n{error}')


estadoRoot2 = False
def cierreRoot2():
    global estadoRoot2
    estadoRoot2 = False
    root2.destroy()
    print('3 estadoRoot2 :',estadoRoot2)
    
    
#FRAME 4
# Crear tabla con 5 columnas y establecer encabezados
tabla = ttk.Treeview(frame4, height=12, columns=('nombre', 'apellido', 'mascota', 'celular', 'nhc', 'fecha'))
tabla.grid(row=0, column=0, columnspan=2)
tabla.heading('#0', text='DNI')#entrada1
tabla.heading('nombre', text='NOMBRE')#entrada2
tabla.heading('apellido', text='APELLIDO')#entrada3
tabla.heading('mascota', text='MASCOTA')#entrada4
tabla.heading('celular', text='CELULAR')
tabla.heading('nhc', text='Nº H.C')
tabla.heading('fecha', text='ÚLTIMA VISITA')
# Ajustar ancho de columnas
tabla.column('#0', width=100)
tabla.column('nombre', width=150)
tabla.column('apellido', width=200)
tabla.column('mascota', width=100)
tabla.column('celular', width=100)
tabla.column('nhc', width=50)
tabla.column('fecha', width=100)
# Agregar filas de ejemplo
datosEnTabla1()

#botonEliminar= Button(frame4, text='ELIMINAR', bg='red',fg='white', command=Eliminar).grid(row=1, column=0, padx=10, pady=10)
botonVer= Button(frame4, text='VER HISTORIA CLÍNICA', bg='#0062C6', fg='white', command=Read)
botonVer.grid(row=1, column=0, ipadx=15, ipady=3, padx=10, pady=10)
botonCrear= Button(frame4, text='AÑADIR NUEVO PACIENTE', bg='green', fg='white', command=Create)
botonCrear.grid(row=1, column=1, ipadx=15, ipady=3, padx=10, pady=10)

#root.geometry('400x200')
root.mainloop()
