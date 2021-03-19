\newcommand{\entonces}{\Rightarrow}
\newcommand{\si}{\Rightarrow}
\newcommand{\sii}{\Leftrightarrow}
\newcommand{\contenido}{\alpha}
\newcommand{\implica}{\rightarrow}
\newcommand{\union}{\cup}
\newcommand{\interseccion}{\cap}
\newcommand{\y}{\wedge}

# Ejercicio 1

Sea $\gamma$ una formula proposicional del lenguaje $\{\neg,\implica\}$ tal que ninguna de  sus variables proposicionales aparece mas de una vez.  Demostrar que $\gamma$ es una contingencia.

Decimos que una fórmula $\varphi$ es una contingencia cuando existen $v$, $v'$ tal que:
$$v \models \varphi \ y \ v' \not\models \varphi$$

Veamos por inducción estructural:  
**CASO BASE** ($\varphi=p$ es un símbolo proposicional): Es una contingencia, simplemente tomamos una valuación $v_1(p) = 1$ y luego tomamos otra $v_2(p) = 0$. Entonces $v_1 \models \varphi$ y $v_2 \not\models \varphi$.

**PASO INDUCTIVO**: 

- Forma $\neg\varphi$ (por HI $\varphi$ es una contingencia):  
Como $\varphi$ es una contingencia entonces existen $v$ y $v'$ tal que
$$v \models \varphi\ y \ v' \not\models \varphi$$ 
Entonces:
$$v \not\models \neg\varphi\ y \ v' \models \neg\varphi$$ 
Entonces $\neg\varphi$ es una contingencia.
  
- Forma $\varphi \implica \psi$ (por HI $\varphi$ y $\psi$ son contingencias): 
Como ambas son contingencias, entonces existen $v_1,v'_1,v_2,v'_2$ tal que:
$$v_1 \models \varphi\ y \ v'_1 \not\models \varphi$$ 
$$v_2 \models \psi\ y \ v'_2 \not\models \psi$$ 
Luego:
$$v_2 \models \psi \underset{\text{por def}}{\entonces} v_2 \models (\varphi \implica \psi)$$
Definimos:
$$v_s(p) = \begin{cases}
v_1(p) & si\ p \in VAR(\varphi)\\
v_2'(p) & cc\\
\end{cases}$$
Esto lo podemos hacer porque $VAR(\varphi) \interseccion VAR(\psi) = \empty$ (porque ninguna de sus variables proposicionales aparece más de una vez).
Como:
$$v_s \models \varphi\ y\ v_s \not\models \psi$$
$$\underset{\text{por def}}{\entonces} v_s \not\models (\varphi \implica \psi)$$
Entonces $(\varphi \implica \psi)$ es una contingencia.

Entonces $\gamma$ es una contingencia.