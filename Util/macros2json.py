import re

inputMacros = open("macros.tex", "r")
outputJson = open("macros.json", "w")
print("PASA LOS \\newcommand A JSON PARA EXTENSION MARKDOWN+MATH VSCODE")
finalString = ""
for line in inputMacros:
    print("LEYENDO:" + line)
    if line.startswith("\\newcommand"):
        line = line[len("\\newcommand"):].rstrip('\r\n')
        contBraces = 0
        contLetters = 0
        for c in line:
            if c == '{':
                contBraces+=1 
            if c == '}':
                contBraces-=1 
            if contBraces == 0:
                break
            contLetters+=1

        command1, command2 = line[1:contLetters], line[contLetters+2:-1]
        lineString = '  "'+command1+'":"'+command2+'",\n'
        lineString = lineString.replace("\\","\\\\")
        finalString += lineString

outputJson.write("{\n"+finalString+"}")
print("OK")
