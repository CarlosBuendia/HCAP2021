import numpy as np

def convolucion(Ioriginal,Kernel):
    fr = len(Ioriginal) - (len(Kernel) - 1)
    cr = len(Ioriginal[0]) - (len(kernel[0])- 1)
    Resultado = np.zeros((fr,cr))
    #for para recorrer filas
    for i in range(len(Resultado)):
        #for para recorrer columnas
        for j in range(len(Resultado[0])):
            #Hace las multiplicaciones y la suma
            suma = 0
            #for para cada elemento del kernel de las filas del kernel
            for m in range(len(Kernel)):
                #for para cada elemento del kernel de las columnas
                for n in range(len(kernel[0])):
                    suma += Kernel[m][n] * Ioriginal[m+i][n+j]
            Resultado[i][j] = suma
    return Resultado
#imagenes
K=[[-1,0,1],[-1,0,1],[-1,0,1]]
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]
#imagenes a numpy arrays
In = np.array(I)
Kn = np.array(K)
#Funcion de convolucion
R  = convolucion(In,Kn)
print(R)
