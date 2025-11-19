def factorial(n:int):
    if n == 0: 
        return 1
    
    i = n - 1
    while i >= 0:
        if i == 0:
            n = n * 1
        else:
            n = n * i
        
        i -= 1
    
    return n

def coeficiente_binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def distribucion_hipergeometrica(N, n, k, x):
    # N: tamaño de la poblacion
    # n: tamaño de la muestra
    # k: numero de "individuos" o elementos favorables en la poblacion
    # x: variable aleatoria, es el numero de elementos favorables obtenidos. 
    # nota: P(A) = p y P(A) = q ; p + q = 1
    # P(X = x) = (k x) * ( (N - k) (n - x) ) / (N n)
    # P(X = x) = CB1 * ( CB2 ) / CB3

    CB1 = coeficiente_binomial(k, x)
    CB2 = coeficiente_binomial((N - k), (n - x))
    CB3 = coeficiente_binomial(N, n) 

    return (CB1 * CB2) / CB3


def probabilidad_aumulada(N, n, k, x):
    total = 0
    for i in range(0, x+1):
        total += distribucion_hipergeometrica(N, n,k ,i)              
 
    return total

print(factorial(10)) 

print(coeficiente_binomial(4, 2)) 

print(round(distribucion_hipergeometrica(49, 16, 8, 3) * 100, 2))

print(round(probabilidad_aumulada(49, 16, 8, 3) * 100, 2))
