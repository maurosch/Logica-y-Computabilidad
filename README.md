### Agregar soluciones
Si tenés alguna solución faltante me la podes enviar por foto a maurolschiavinato@gmail.com y yo la transcribo a latex. Aunque si sabes latex me harías un gran favor pasandola vos y luego haciendo un pull request para agregarla.

### Errores
No soy ningún profesor ni nada cerca de la materia. Si encuentran errores haganmelo saber y lo arreglo.

### Compilación
Utilizo pandoc para compilar los markdown. Si están en linux pueden correr el ejecutable **compile.sh** para compilar los fuentes.

### Consideraciones
En nuestra notación incluimos el 0 en el conjunto de naturales.

### Qué use para hacer los ejercicios en latex
**Overleaf** mucho no me gusta para trabajar solo en latex por el tiempo de compilación y porque no se puede trabajar offline. Al principio use **notion** que soporta latex y compila en tiempo real con javascript (osea no hay espera para ver el resultado :D). Pero la principal desventaja es que no se puede usar offline y que no podemos usar macros que se compartan entre celdas. Finalmente utilicé **vscode** con la extensión **Markdown+Math** la cual escribimos mediante markdown y podemos agregar latex matemático con el signo pesos en tiempo real y nos deja usar macros. Luego para obtener el pdf simplemente se puede compilar con pandoc. La desventaja de usar esta extensión es que no podemos incluir librerías, algo que no creo que sea posible de hacer sin compilar.

Una opción a probar que no use es **Jupyter**.
