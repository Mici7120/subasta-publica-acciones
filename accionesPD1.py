def auction(N, M, P, buyers): #1. numero de compradores,
  #el número de acciones a vender M,
  # Inicializamos la matriz de valores y de decisiones
  dp = [[[0 for _ in range(P+1)] for _ in range(M+1)] for _ in range(N+1)]
  decisions = [[[-1 for _ in range(P+1)] for _ in range(M+1)] for _ in range(N+1)]

  # Se lena la matriz de valores
  for i in range(1, N+1):
      for j in range(1, M+1):
          for k in range(1, P+1):
              # Caso 1: el comprador i no compra nada
              dp[i][j][k] = dp[i-1][j][k]
              decisions[i][j][k] = decisions[i-1][j][k]

              # Caso 2: el comprador i compra algunas acciones
              for c in range(buyers[i-1][2], buyers[i-1][1]+1):
                if j >= c:
                    value = dp[i-1][j-c][buyers[i-1][0]] + c * k
                    if value > dp[i][j][k]:
                        dp[i][j][k] = value
                        decisions[i][j][k] = c

  # Construimos la lista de ofertas elegidas
  chosen_offers = [0 for _ in range(N)]
  j = M
  k = P
  for i in range(N, 0, -1):
      chosen_offers[i-1] = decisions[i][j][k]
      j -= chosen_offers[i-1]
      k = buyers[i-1][0]

  # Devolvemos el valor máximo posible y la lista de ofertas elegidas
  return dp[N][M][P], chosen_offers

# A = 1000 # Cantidad de acciones totales en venta
# B = 100 # Precio minimo de venta de las acciones
# n = 5 # Cantidad de ofertas
# # Cada oferta esta compuesta de tres datos, p, c y e. Que corresponden
# # al precio ofertado, el maximo y minimo número de acciones que se
# # compraran respectivamente.
# oferta = [(500,600,400), (450,400,100), (400,400,100), (200,200,50), (100,1000,10)]
# print(auction(n,A,B,oferta))

N = 3 # número de compradores
M = 10 # el número de acciones a vender
P = 3 # precio mínimo por acción
buyers = [(2, 3, 2), (2, 4, 1), (1, 5, 1)]
print(auction(N, M, P, buyers))