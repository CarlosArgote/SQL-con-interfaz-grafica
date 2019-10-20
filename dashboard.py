"""
Nombre: dashboard.py
Objetivo: Manejar bases de datos desde una interfaz gráfica.
Autor: Andrés Eduardo Mora Alonso / Carlos Andres Rodriguez Argote.
Fecha: 13/10/19
"""
import pymysql
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

nombre=''
sueldo=0
global EClave
global ENombre
global ESueldo
global scrolledtext1

def agregar():
    global EClave
    global ENombre
    global ESueldo
    db = pymysql.connect("localhost","root","","base")
    cursor = db.cursor()
    sqlcad="INSERT INTO empleados (clave,nombre,sueldo) VALUES ("+EClave.get()+',"'+ENombre.get()+'",'+ESueldo.get()+');'
    cursor.execute(sqlcad)
    db.commit()
    db.close()
    EClave.delete(0,END)
    ENombre.delete(0,END)
    ESueldo.delete(0,END)

def borrar():
    global EClave
    db = pymysql.connect("localhost","root","","base")
    cursor = db.cursor()
    sqlcad='DELETE FROM empleados WHERE clave='+EClave.get()
    cursor.execute(sqlcad)
    db.commit()
    db.close()
    EClave.delete(0,END)

def nwin():
    global EClave
    global ENombre
    global ESueldo
    nv=Tk()
    nv.geometry('200x150')
    nv.title('Nuevo registro')
    
    svf=Frame(nv,width=180,height=130)
    svf.place(x=10,y=10)

    ClaveLab=Label(svf,text='Clave ')
    ClaveLab.grid(column=1,row=1)
    NombreLab=Label(svf,text='Nombre')
    NombreLab.grid(column=1,row=2)
    SueldoLab=Label(svf,text='Sueldo')
    SueldoLab.grid(column=1,row=3)

    EClave=Entry(svf,width=20)
    EClave.grid(column=2,row=1)
    ENombre=Entry(svf,width=20)
    ENombre.grid(column=2,row=2)
    ESueldo=Entry(svf,width=20)
    ESueldo.grid(column=2,row=3)

    Gb=Button(nv,text='Guardar',command=agregar).place(x=40,y=100)
    Cb=Button(nv,text='Cerrar',command=nv.destroy).place(x=100,y=100)

    nv.mainloop()

def search():
    global EClave
    global ENombre
    global ESueldo
    searchv=Tk()
    searchv.geometry('200x150')
    searchv.title('Buscar')
    
    searchf=Frame(searchv,width=180,height=130)
    searchf.place(x=10,y=10)

    ClaveLab=Label(searchf,text='Clave ')
    ClaveLab.grid(column=1,row=1)
    NombreLab=Label(searchf,text='Nombre')
    NombreLab.grid(column=1,row=2)
    SueldoLab=Label(searchf,text='Sueldo')
    SueldoLab.grid(column=1,row=3)

    EClave=Entry(searchf,width=20)
    EClave.grid(column=2,row=1)
    ENombre=Entry(searchf,width=20)
    ENombre.grid(column=2,row=2)
    ESueldo=Entry(searchf,width=20)
    ESueldo.grid(column=2,row=3)

    Gb=Button(searchv,text='Buscar',command=fnd).place(x=40,y=100)
    Cb=Button(searchv,text='Cerrar',command=searchv.destroy).place(x=100,y=100)

    searchv.mainloop()

def modificar():
    global EClave
    global ENombre
    global ESueldo
    db = pymysql.connect("localhost","root","","base")
    cursor = db.cursor()
    sqlcad='UPDATE empleados SET nombre="'+ENombre.get()+'", sueldo='+ESueldo.get()+' WHERE clave='+EClave.get()
    cursor.execute(sqlcad)
    db.commit()
    db.close()
    EClave.delete(0,END)
    ENombre.delete(0,END)
    ESueldo.delete(0,END)

def fnd():
    global EClave
    db=pymysql.connect("localhost","root","","base")
    cursor=db.cursor()
    sqlcad='SELECT nombre,sueldo FROM empleados where clave='+EClave.get()
    cursor.execute(sqlcad)
    db.commit()
    resultado=cursor.fetchone()
    nfind=resultado[0]
    sfind=resultado[1]
    ENombre.delete(0, tk.END)
    ESueldo.delete(0, tk.END)
    ENombre.insert(0,nfind)
    ESueldo.insert(0,sfind)
    EClave.delete(0,END)

def sw():
    global scrolledtext1
    db=pymysql.connect("localhost","root","","base")
    cursor=db.cursor()
    sqlcad='SELECT * FROM empleados'
    cursor.execute(sqlcad)
    db.commit()
    resultado=cursor.fetchall()
    scrolledtext1.delete("1.0", tk.END)
    for row in reversed(resultado):
        clave=row[0]
        descripcion=row[1]
        precio=row[2]
        scrolledtext1.insert('1.0','\n')      
        scrolledtext1.insert("1.0", '{0} {1} {2}'.format(clave,descripcion,precio))
    db.close()

def bw():
    global EClave
    db=pymysql.connect("localhost","root","","base")
    cursor=db.cursor()
    sqlcad='SELECT nombre, sueldo FROM empleados WHERE clave='+EClave.get()
    cursor.execute(sqlcad)
    db.commit()
    resultado=cursor.fetchone()
    scrolledtext1.delete("1.0", tk.END)
    for row in resultado:
        Nombre=row[1]
        Sueldo=row[2]

def mwin():
    global EClave
    global ENombre
    global ESueldo
    mv=Tk()
    mv.geometry('200x150')
    mv.title('Modificar')
    
    mvf=Frame(mv,width=180,height=130)
    mvf.place(x=10,y=10)

    ClaveLab=Label(mvf,text='Clave ')
    ClaveLab.grid(column=1,row=1)
    NombreLab=Label(mvf,text='Nombre')
    NombreLab.grid(column=1,row=2)
    SueldoLab=Label(mvf,text='Sueldo')
    SueldoLab.grid(column=1,row=3)

    EClave=Entry(mvf,width=20)
    EClave.grid(column=2,row=1)
    ENombre=Entry(mvf,width=20)
    ENombre.grid(column=2,row=2)
    ESueldo=Entry(mvf,width=20)
    ESueldo.grid(column=2,row=3)

    Gb=Button(mv,text='Guardar',command=modificar).place(x=40,y=100)
    Cb=Button(mv,text='Cerrar',command=mv.destroy).place(x=100,y=100)

    mv.mainloop()

def bwin():
    global EClave
    global ENombre
    global ESueldo
    bv=Tk()
    bv.geometry('200x150')
    bv.title('Borrar')
    
    bvf=Frame(bv,width=180,height=130)
    bvf.place(x=10,y=10)

    ClaveLab=Label(bvf,text='Clave ')
    ClaveLab.grid(column=1,row=1)
    EClave=Entry(bvf,width=20)
    EClave.grid(column=2,row=1)

    Gb=Button(bv,text='Borrar',command=borrar).place(x=40,y=100)
    Cb=Button(bv,text='Cerrar',command=bv.destroy).place(x=100,y=100)

    bv.mainloop()

def about():
    aboutv=Tk()
    aboutv.geometry('200x70')
    aboutv.title('Acerca de...')
    
    aboutf=Frame(aboutv,width=180,height=130)
    aboutf.place(x=10,y=10)

    Lab1=Label(aboutf,text='Andrés Eduardo Mora Alonso')
    Lab1.grid(column=1,row=1)
    Lab2=Label(aboutf,text='Carlos Andrés Rodríguez Argote')
    Lab2.grid(column=1,row=2)
    aboutv.mainloop()

def export():
    w, h = A4
    c = canvas.Canvas("Reporte.pdf", pagesize=A4)
    db=pymysql.connect("localhost","root","","base")
    cursor=db.cursor()
    sqlcad='SELECT * FROM empleados'
    cursor.execute(sqlcad)
    db.commit()
    resultado=cursor.fetchall()
    text = c.beginText(50, h - 50)
    for row in resultado:
        clave=row[0]
        descripcion=row[1]
        precio=row[2]    
        text.textLines("{0} {1} {2}\n".format(clave,descripcion,precio))
    c.drawText(text)
    db.close()
    c.showPage()
    c.save()

def main():
    os.system('cls')
    print('\n')

    global scrolledtext1

    #Ventana principal.
    ventana=Tk()
    ventana.geometry("450x200")
            
    #Crear menú de ventana.
    menubar=Menu(ventana)
    menubar = Menu(ventana)
    ventana.config(menu=menubar)

    scrolledtext1=st.ScrolledText(ventana,width=50,height=10)
    scrolledtext1.grid(column=0,row=0, padx=10, pady=10)

    #Crear de edición.
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Agregar",command=nwin)
    filemenu.add_command(label="Buscar",command=search)
    filemenu.add_command(label="Cambiar",command=mwin)
    filemenu.add_command(label="Borrar",command=bwin)

    #Menú para exportar.
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Pantalla",command=sw)
    editmenu.add_command(label="Exportar a PDF",command=export)

    #Menú de ayuda.
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Quiénes somos...",command=about)
    helpmenu.add_separator()
    helpmenu.add_command(label="Salir",command=ventana.destroy)

    #Mostrar pestañas en la ventana.
    menubar.add_cascade(label="Trabajadores", menu=filemenu)
    menubar.add_cascade(label="Reportes", menu=editmenu)
    menubar.add_cascade(label="Opciones", menu=helpmenu)

    ventana.mainloop()

    print('\n')

if __name__=='__main__':
    main()
