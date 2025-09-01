# Actividad-1.2

# Problema de la Mochila (Knapsack Problem)

## Objetivo
Este proyecto tiene como finalidad analizar y diseñar algoritmos para resolver el **Problema de la Mochila**, aplicando **programación dinámica** para la variante 0/1.

## Descripción del Problema
El **Problema de la Mochila 0/1** consiste en determinar qué objetos deben incluirse en una mochila que tiene una **capacidad máxima de peso** para maximizar el **valor total** sin exceder dicha capacidad.

- Se tienen `n` objetos.  
- Cada objeto `i` tiene un **peso** `w_i` y un **valor** `v_i`.  
- La mochila tiene una capacidad máxima `W`.  
- El objetivo es **maximizar la suma de los valores** de los objetos seleccionados, sin superar `W`.

## Análisis del Problema

### Mochila 0/1
- Cada objeto se puede tomar o no tomar (no fraccionado).  
- Se resuelve mejor con programación dinámica.  
- Tiempo de ejecución: `O(n * W)`.

### Mochila Fraccionaria
- Los objetos se pueden tomar porciones (ejemplo: la mitad de un objeto).  
- Se resuelve con un algoritmo codicioso (greedy), tomando primero los objetos con mayor relación `valor/peso`.  
- Tiempo de ejecución: `O(n log n)` (por la ordenación).  

En este proyecto se eligió **programación dinámica** porque el problema es **Mochila 0/1**, donde la técnica codiciosa no siempre da la solución óptima.

## Implementación
El algoritmo usa una **tabla 2D (`tabla`)** de tamaño `(n+1) x (W+1)` donde:

- `tabla[i][w]` = valor máximo con los primeros `i` objetos y capacidad `w`.  
- Se llena la tabla con programación dinámica.  

## Ejemplos

### Ejemplo 1
Objetos:  
- (Peso=2, Valor=3), (Peso=3, Valor=4), (Peso=4, Valor=5), (Peso=5, Valor=6)  
Capacidad = 5  

Resultado: Valor máximo = 7  
Objetos elegidos = Objeto 1 y Objeto 2  

### Ejemplo 2
Objetos:  
- (Peso=1, Valor=1), (Peso=2, Valor=6), (Peso=3, Valor=10), (Peso=4, Valor=12)  
Capacidad = 5  

Resultado: Valor máximo = 7  
Objetos elegidos = Objeto 2 y Objeto 1  

### Ejemplo 3
Objetos:  
- (Peso=4, Valor=5), (Peso=3, Valor=4), (Peso=2, Valor=3), (Peso=1, Valor=1)  
Capacidad = 6  

Resultado: Valor máximo = 6  
Objetos elegidos = Objeto 1 y Objeto 4  

## Conclusión
La programación dinámica resulta ser la técnica más adecuada para resolver el Problema de la Mochila 0/1, ya que garantiza encontrar siempre la solución óptima considerando todas las combinaciones posibles. A diferencia del enfoque codicioso, que solo funciona correctamente en la versión fraccionaria del problema, este método permite un análisis exhaustivo aunque con un costo computacional dependiente de la capacidad máxima de la mochila, lo que puede ser una limitación en instancias muy grandes.
