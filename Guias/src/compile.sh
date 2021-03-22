if [ $# != 0 ]; then
	echo "Compilando $1"
	pandoc "$1" --from markdown+latex_macros -o "../practica${1%.*} - solucion.pdf"
else
	for f in *.md; do
		echo "Compilando $f"
		pandoc "$f" --from markdown+latex_macros -o "../practica${f%.*} - solucion.pdf"
	done
fi
