#Método gráfico
from tkinter import *
from matplotlib import pyplot as plt
import numpy as np


numeroRestricciones = 0
class MG(Tk):   #Clase principal
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.cambiarVentana(VentanaInicio)

    def cambiarVentana(self, frame_class): #Elimina pantalla base y crea la siguiente
        new_frame = frame_class(self) 
        if self._frame is not None: 
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class VentanaInicio(Frame): #Clase de pantalla de inicio
    def __init__(self, master):
        Frame.__init__(self, master)

        def cambiarVentanaResolver():
                global numeroRestricciones
                if numRes.get:
                    numeroRestricciones = int(numRes.get())
                master.cambiarVentana(VentanaResolver)
    #Etiquetas
        eRes = Label(self, text = "Número de restricciones")
        # Entradas
        numRes = Entry(self)
    #Botones        
        botonSig =  Button(self, text = "Siguiente", command = cambiarVentanaResolver) #Botón siguiente

    #Orden de widgets en pantalla
        eRes.grid(row = 0, column = 0)
        numRes.grid(row = 1, column = 0)
        botonSig.grid(row = 2, column = 0)
        


class VentanaResolver(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        listaHileras = [] #Orden de sus listas [0] = x1; [1] = x2; [2] = signo; [3] = a
        varMaxMin = IntVar()

        def generarEntradas(): #Función para generar tabla dinámicamente 
            global numeroRestricciones
            for i in range (numeroRestricciones): #hileras
                listaTupla = []
                listaHileras.append(listaTupla)
                for j in range(4): #columnas
                    listaTupla.append( StringVar())
                    entradaTemp = Entry(self, textvariable = listaTupla[j])
                    entradaTemp.grid(row = i+7, column = j)
        
        def perp( a ) :
            b = np.empty_like(a)
            b[0] = -a[1]
            b[1] = a[0]
            return b
        
        def seg_intersect(a1,a2, b1,b2) :
            da = a2-a1
            db = b2-b1
            dp = a1-b1
            dap = perp(da)
            denom = np.dot( dap, db)
            num = np.dot( dap, dp )
            return (num / denom.astype(float))*db + b1

        def resolver():
            coeficientesX = [] #Lista para valores X
            coeficientesY = [] #Lista para valores Y
            valorA = []
            puntosA = [] #Coordenadas 'a' de la recta
            puntosB = [] #Coordenadas 'b' de la recta
            for lista in listaHileras:  #For para conseguir los valores de los campos generados dinámicamente
                coeficientesX.append(int(lista[0].get()))
                coeficientesY.append(int(lista[1].get()))
                valorA.append(int(lista[3].get()))
            
            for i in range(len(coeficientesX)): #For para hacer mapeo de coordenadas
                if (coeficientesY[i] and coeficientesX[i]): #Comprobar que los valores no sean 0s
                    tempX = coeficientesX[i]/valorA[i]
                    tempY = valorA[i]/coeficientesY[i]
                    puntosA.append([0,tempY])
                    puntosB.append([tempX,0])
                else:#Woop, no funciona ahora
                    if(coeficientesY[i]):
                        plt.axhline(y=(valorA[i]/coeficientesY[i]))
                    else:
                        plt.axvline(x=(valorA[i]/coeficientesX[i]))
            
            plt.show()
    #Etiquetas
        eX1 = Label(self, text = "X1")
        eX2 = Label(self, text = "X2")
        eX1Z = Label(self, text = "X1")
        eX2Z = Label(self, text = "X2")
        eSigno = Label(self, text = "=/>=/<=")
        eA = Label(self, text = "a")
        eZ = Label(self, text = "Z = ")
        eRest = Label(self, text = "Restricciones")
    #Entradas
        entradaX1Z = Entry(self)
        entradaX2Z = Entry(self)
    #Botones
        rbMax = Radiobutton(self, text = "Maximizar", variable = varMaxMin, value = 1)
        rbMin = Radiobutton(self, text = "Minimizar", variable = varMaxMin, value = 2)
        bResolver = Button(self, text = "Resolver", command = resolver)
    #Orden de widgets en pantalla
        rbMax.grid(row = 0, column = 0)
        rbMin.grid(row = 1, column = 0)
        #Campo de Z
        eZ.grid(row = 0, column = 1)
        eX1Z.grid(row =0, column = 3)
        eX2Z.grid(row = 1, column = 3)
        entradaX1Z.grid(row = 0, column = 2)
        entradaX2Z.grid(row = 1, column = 2)

        eRest.grid(row = 5, column = 0)
        eX1.grid(row = 6, column = 0)
        eX2.grid(row = 6, column = 1)
        eSigno.grid(row = 6, column = 2)
        eA.grid(row = 6, column = 3)
        generarEntradas()

        bResolver.grid(row = 20, column = 1)


if __name__ == "__main__":
    app = MG()
    app.mainloop()


