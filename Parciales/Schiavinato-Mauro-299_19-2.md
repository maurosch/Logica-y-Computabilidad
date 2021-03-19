\newcommand{\entonces}{\Rightarrow}
\newcommand{\si}{\Rightarrow}
\newcommand{\sii}{\Leftrightarrow}
\newcommand{\contenido}{\alpha}
\newcommand{\implica}{\rightarrow}
\renewcommand{\a}{\alpha}
\renewcommand{\b}{\beta}
\newcommand{\union}{\cup}
\newcommand{\interseccion}{\cap}
\newcommand{\y}{\wedge}
\renewcommand{\o}{\vee}
\newcommand{\llaves}[1]{\{#1\}}
\newcommand{\m}[1]{\mathcal{#1}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\exist}{\exists}

# Ejercicio 2
El conjunto de los naturales que tienen resto 2 al dividirlos por 3 es el conjunto:
$$\llaves{2,5,8,...} = \llaves{2+3 \cdot x:x\in\N}$$
Veamos como expresarlo con el lenguaje $\m{L}$.  
Definimos:
$$\varphi(x): \exist y(x = 2 + y \y \exist z(z+z+z=y))$$
Cumple que $\varphi(x)$ es verdadero sii $x$ resto 3 es 2.  
Entonces la nueva relación se puede expresar como:

$$R = \llaves{v(x):U \models \varphi[v]}$$