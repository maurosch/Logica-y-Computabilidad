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

# Ejercicio 3

Queremos ver que $SQB$ correcto con respecto a $\m{M}$, es decir:
$$SQB \vdash \varphi \entonces \m{M} \models \varphi$$
para toda $\m{L}$-sentencia $\varphi$.  
Notemos que:
$$\m{M} \models SQB$$
Entonces, sea $\varphi$ tal que:
$$SQB \vdash \varphi$$
Entonces también por correctitud:
$$SQB \models \varphi$$
Entonces:
$$SQB \models \varphi\ y\ \m{M} \models SQB \entonces \m{M} \models \varphi$$

\
Ahora veamos que no es completo con respecto a $\m{M}$, es decir:
$$\m{M} \models \varphi \entonces SQB \not\vdash \varphi$$
para alguna $\m{L}$-sentencia.  
Definimos:
$$\varphi: \forall xy(E(x,y) \implica \exist z(E(y,z)))$$
Que quiere decir: "si te llega algún arco, entonces tenés que tener un arco saliente".  
Notamos que $\m{M} \models \varphi$.

Veamos por el absurdo que $SQB \not\vdash \varphi$:
Suponemos que si. Entonces $SQB \models \varphi$ (por correctitud). Entonces cualquier estructura que satisface $SQB$ también satisface $\varphi$.  
Definimos el modelo $\m{B}$ como:  

- $B = \llaves{a,b}$  
  
- $G_{\m{B}} = \llaves{a}$  
  
- $B_{\m{B}} = \llaves{b}$  
  
- $E = \llaves{(a,b)}$

![Modelo $\m{B}$](parcial_graph.png){ width=50% }

Notamos que este modelo $\m{B} \models SQB$ pero $\m{B} \not\models \varphi$. Absurdo, de suponer que $SQB \vdash \varphi$.  
Entonces $SQB \not\vdash \varphi$. Entonces $SQB$ no es completo con respecto a $\m{M}$.