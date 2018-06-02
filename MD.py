#Modelo de descuento por cantidad

from tkinter import * #GUI de python
from tkinter import messagebox
from math import sqrt, floor
numeroRangos = 0

class MC(Tk):   #Clase principal
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
        global numeroRangos
    
        def cambiarVentanaTabla():
            global numeroRangos
            if numRang.get:
                numeroRangos = int(numRang.get())
            master.cambiarVentana(VentanaTabla)

    #Etiquetas
        eRang = Label(self, text = "Número de rangos")

    # Entradas
        numRang = Entry(self)

    #Botones        
        botonSig =  Button(self, text = "Siguiente", command = cambiarVentanaTabla ) #Botón siguiente

    #Orden de widgets en pantalla
        eRang.grid(row = 0, column = 0)
        numRang.grid(row = 0, column = 10)
        botonSig.grid(row = 0, column = 20)

class VentanaTabla(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        listaHileras = []

    #Funciones
        def generarTabla(): #Función para generar tabla dinámicamente 
            global numeroRangos
            for i in range (numeroRangos): #hileras
                listaTupla = []
                listaHileras.append(listaTupla)
                for j in range(2): #columnas
                    listaTupla.append( StringVar())
                    entradaTemp = Entry(self, textvariable = listaTupla[j])
                    entradaTemp.grid(row = i+7, column = j)

        def resolver():
            global numeroRangos
            numDemanda = float(demanda.get())
            numCostoP = float(costoPedido.get())
            numCostoA = float(costoAlm.get())
            
            numCostoA = numCostoA/100
            diccionarioSoluciones = {} #Diccionario para almacenar cantidades y precios
            for lista in listaHileras: #Se empieza iterar los valores obtenidos para generar costo por rango
                valorUnidad = float(lista[1].get())
                Q = sqrt((2 * numDemanda * numCostoP) / ((numCostoA) * valorUnidad))    
                
                #Obtener rango del formato 'x-y'
                temp = lista[0].get()
                tempGuion = temp.find('-')
                limiteMenor = int(temp[:tempGuion])    

                costoTotal = round((numDemanda * valorUnidad + (numDemanda * numCostoP)/(Q) + (Q*numCostoA*valorUnidad)/2 ),4) #Se redondea a 4 decimales
                diccionarioSoluciones["C("+(str(floor(Q)) if Q > limiteMenor else str(limiteMenor))+")"] = costoTotal 

                stringSolucion = ""
                for llave,valor in diccionarioSoluciones.items():
                    stringSolucion = stringSolucion + llave+"="+str(valor)+"\n"

            llaveMin = min(diccionarioSoluciones, key = diccionarioSoluciones.get)
            messagebox.showinfo("Solución",stringSolucion+"\nSolución Óptima: "+str(llaveMin))

    #Etiquetas
        eDemanda = Label(self, text = "Demanda") 
        eCPedido = Label(self, text = "Costo por pedido")
        eCAlm = Label(self, text = "Costo almacenamiento (%)")
        eCantidad = Label(self, text = "Unidades (x-y)") 
        eCostoU = Label(self, text = "Costo unitario") 


    #Entradas
        demanda = Entry(self)
        costoPedido = Entry(self)
        costoAlm = Entry(self)
 
    #Botones
        bResolver = Button(self, text = "Resolver", command = resolver)

    #Orden de widgets en pantalla
        eDemanda.grid(row = 0, column = 0)
        demanda.grid(row = 0, column = 1)

        eCPedido.grid(row = 2, column = 0)
        costoPedido.grid(row = 2, column = 1)

        eCAlm.grid(row = 4, column = 0)
        costoAlm.grid(row = 4, column = 1)

        eCantidad.grid(row = 6, column = 0)
        eCostoU.grid(row = 6, column = 1)
        
        bResolver.grid(row = 20, column = 1)
        
        generarTabla()
        
if __name__ == "__main__":
    app = MC()
    app.mainloop()