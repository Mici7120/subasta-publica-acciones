import itertools
gananciaTotal = 0
acciones_vendidas = []
# Abrir archivo de entrada
with open("entrada.txt", "r") as f:
    # Leer las tres primeras líneas
    A = int(f.readline().strip())       # Cantidad de acciones totales en venta
    B = float(f.readline().strip())     # Precio minimo de venta de las acciones
    n = int(f.readline().strip())       # Cantidad de ofertas

    # Leer las ofertas de los compradores y la oferta del gobierno
    ofertas = []
    for i in range(n+1):
        p, c, r = map(float, f.readline().strip().split(","))
        oferta = (p, int(c), int(r))
        ofertas.append(oferta)
        
# Usando ordenamiento por comparacion ordenamos la matriz de las ofertas, en base al mayor beneficio
# Complejidad n^2, se puede mejorar.

for i in range(0, len(ofertas)-1):
   
    for j in range(i+1, len(ofertas)-1):
          if(ofertas[i][0]*ofertas[i][1]) < (ofertas[j][0]*ofertas[j][1]):
            temporal = ofertas[i]
            ofertas[i] = ofertas[j]
            ofertas[j] = temporal

# Recorre la matriz comparando si el valor de la oferta en mayor o igual al precio de venta
for i in range (0, len(ofertas)):
  
    if ofertas[i][0] >= B:

        # Si la cantidad de acciones es mayor o igual a la cantidad minima de acciones entra al if
        if  A >= ofertas[i][2]:
                # Si la cantidad de acciones es mayor o igual a la cantidad maxima de acciones, se vende el maximo
                if(A >= ofertas[i][1]):
                    A = A - ofertas[i][1];
                    temporal = ofertas[i][1]
                    acciones_vendidas.append(temporal)
                # En caso de que la cantidad de acciones sea menor, se venderan la cantidad de acciones disponibles    
                else:
                    A = A - A;
                    temporal = A
                    acciones_vendidas.append(temporal)
        # En caso de que el valor ofertado sea menor al minimo, no se venderan acciones a dicha empresa            
        else:
            acciones_vendidas.append(0)


#print ("Acciones vendidas", acciones_vendidas)

    # Escribir el resultado en el archivo de salida
with open("salida.txt", "w") as f:
   f.write(f"n^2\n") 
   for x in range(0,len(acciones_vendidas)):
        f.write(f"{acciones_vendidas[x]}\n")
