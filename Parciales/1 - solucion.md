---
title: "Solución 1º Parcial Lógica y Computabilidad - Verano 2021"
#author: Schiavinato Mauro
#date: March 22, 2021
geometry: margin=2.5cm
output: pdf_document
---

Solución hecha por un alumno. 

# Ejercicio 1

Definamos $f(x)$ como la función:

$$f(x) = <sumaIns1(x), sumaIns2(x), sumaIns3(x)>$$

Si $sumaIns1(x), sumaIns2(x), sumaIns3(x)$ son pr, entonces $f(x)$ es pr, porque la codificación de tripleta está dada como:

$$<\cdot,\cdot,\cdot> = <\cdot,<\cdot,\cdot>>$$

Que es una composición de codificación de pares con codificación de pares. Y la codificación de pares es pr (demostrado en teórica).

Sabemos que:

- $V \leftarrow V+1$ tiene número de instrucción 1.
- $V \leftarrow V\dot-1$ tiene número de instrucción 2.
- $IF V \neq 0\ GOTO\ L$ tiene número de instrucción $\#(L)+2$ la cual es siempre mayor a 2 (porque las etiquetas se enumeran desde el 1).

Definimos una función auxiliar que nos va a dar el número de instrucción de una línea del programa:

$$numIns(x,i) = l(r((x+1)[i]))$$

Que es pr por ser composición de:

- $l(x)$ y $r(x)$ que son pr (visto en teórica).
- $x+1$ que es pr (la suma es pr, visto en teórica).
- $x[i]$ es pr (visto en teórica).

Luego definimos las funciones:

$$sumaIns1(x) = \sum_{i=1}^{|x+1|} (numIns(x,i) = 1)$$

$$sumaIns2(x) = \sum_{i=1}^{|x+1|} (numIns(x,i) = 2)$$

$$sumaIns3(x) = \sum_{i=1}^{|x+1|} (numIns(x,i) > 2)$$

Que las tres son pr por ser composición de las siguientes funciones:

- $\sum_{t=1}^{y} f(x,t)$ que es pr (visto en teórica).
- $|\cdot|$ es pr (visto en teórica).
- $x+1$ que es pr (la suma es pr, visto en teórica).
- $numIns(x,i)$ que es pr (demostrado más arriba).
- $=, >$ que son predicados pr (ejercicio 5 guía 1).

Entonces $f(x)$ es primitiva recursiva.

# Ejercicio 2

$$g(x,y) = \begin{cases}
1 & si\ \{0,1,...,y\} \subseteq Dom(\Phi_x^{(1)}) \\
0 & cc
\end{cases}$$

Suponemos que es computable. Entonces también es computable la función:

$$g'(x) = g(x,0) = \begin{cases}
1 & si\ 0 \in Dom(\Phi_x^{(1)}) \equiv \Phi_x^{(1)}(0)\downarrow \\
0 & cc
\end{cases}$$

$g'(x)$ es computable porque es una composición de $g(x,y)$ con la función $f(x)=0$ en el segundo parámetro. La función nula es primitiva recursiva (función inicial), entonces es computable.

La función $g'(x)$  es la función característica del conjunto:

$$G' = \{x:\Phi_x^{(1)}(0)\downarrow\}$$

Sea $C$ definido como la siguiente clase de funciones:

$$C = \{g(x):g(0)\downarrow\}$$

Entonces $G'$ es un conjunto de índices porque lo podemos escribir como:

$$G' = \{x:\Phi_x^{(1)} \in C\}$$

Sea $P_1$ el programa:

```jsx
[A] GOTO A
```

Notar que $GOTO\ A$ es una macro (definida en teórica).

Y sea $P_2$ el programa:

```jsx
Y <- 0
```

Entonces $P_1 \notin G'$ y $P_2 \in G'$. 

Entonces no es un conjunto trivial $(\mathbb{N}$ o $\emptyset)$. Entonces por teorema de Rice, es un conjunto no computable. 

Entonces $g'(x)$ no es computable. Absurdo porque compusimos una función computable con funciones pr (computables).

Entonces $g(x,y)$ no es computable.

# Ejercicio 3

$R$ es un conjunto c.e., entonces podemos escribir $R$ como:

$$R = \{x:g(x)\downarrow\} = dom\ g$$

Siendo $g(x)$ alguna función parcial computable.

Entonces para ver que

$$W = \bigcup_{x \in R} Dom(\Phi_x)$$

Es un conjunto c.e., podemos buscar un programa donde se defina únicamente en los elementos de $W$. Si llegase a ocurrir eso, entonces podríamos tener:

$$W = \{x:g'(x)\downarrow\} = dom\ g'$$

Lo cual es la definición de ce. Veamos como construir tal $g'(x)$.

Para que un elemento pertenezca a $W$, tiene que pertenecer al $Dom$ de los programas generados por los elementos de $R$.

Sea $w$ el número de un programa que computa la función $g(x)$ (la del dominio de $R$, existe porque $R$ es ce), entonces podemos definir $g'(x)$ como: 

$$g'(y) = (\exists <x,t_1,t_2>) (STP^{(1)}(x, w, t_1) = 1 \wedge\ STP^{(1)}(y, x, t_2) = 1)$$

Esta es parcial computable, porque es una composición de las siguientes funciones:

- El $(\exists x)p(x)$ es parcial computable si el predicado $p(x)$ es computable (visto en la teórica).
- $STP^{(1)}(x,y,z)$ es pr (entonces computable)(visto en teórica). Es un predicado que devuelve 1 sii el programa $y$ termina en $z$ o menos pasos con entrada $x$.
- = es pr (ej4 guía 1).
- $\wedge$ es pr (ej4 guía 1).

Veamos que se define donde queramos (en los elementos que pertenecen al conjunto) y se indefine en el resto (los que no pertenecen).

Sea $p \in Dom(\Phi_x)$ tal que $x \in R$. Entonces va a existir $x, t_1, t_2$ tal que:

- $STP^{(1)}(x, w, t_1) = 1$ porque $x \in R$, entonces $g(x)\downarrow$.
- $STP^{(1)}(p, x, t_2) = 1$ porque $p \in Dom(\Phi_x)$, entonces $\Phi_x(p)\downarrow$.

Notemos que estos dos puntos son **si solo si**, entonces si no suceden ambas cosas la función se va a indefinir.