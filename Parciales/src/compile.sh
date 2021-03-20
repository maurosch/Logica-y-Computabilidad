for f in *.md; do
	echo "Compilando $f"
	pandoc "$f" --from markdown+latex_macros -o "../${f%.*} - solucion.pdf"
done
