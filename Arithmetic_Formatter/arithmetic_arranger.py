def arithmetic_arranger(problems,status=False):

    if len(problems)>5:
        return "Error: Too many problems."
    primerafila=[]
    segundafila=[]
    cuartafila=[]
    guardaoperaciones=[]
    for operacion in problems:
        numeros = operacion.split(" ")
        if (len(numeros[0])>4) or (len(numeros[2])>4):
            return "Error: Numbers cannot be more than four digits."
        try:
            numero1 = int(numeros[0])
        except:
            return("Error: Numbers must only contain digits.")
        try:
            numero2 = int(numeros[2])
        except:
            return("Error: Numbers must only contain digits.")
        if numeros[1] == "+":
            resultado = numero1 +numero2
        elif numeros[1] == "-":
            resultado = numero1 - numero2
        else:
            return "Error: Operator must be '+' or '-'."
        primerafila.append(numero1)
        segundafila.append(numero2)
        cuartafila.append(resultado)
        guardaoperaciones.append(numeros[1])
    i = 0
    primerafilastring=""
    segundafilastring=""
    tercerafilastring=""
    cuartafilastring=""
    for numero in primerafila:
        if i>0:
            primerafilastring=primerafilastring+"    "
            segundafilastring=segundafilastring + "    "
            tercerafilastring=tercerafilastring + "    "
            cuartafilastring=cuartafilastring + "    "
            #Eso anade los 4 espacios del medio, excepto en la primera iteracion
        if len(str(numero))>=len(str(segundafila[i])):
            primerafilastring=primerafilastring+"  "+str(numero)
            espacios = ""
            for j in range(0,(1+len(str(numero))-len(str(segundafila[i])))):
                espacios=espacios + " "
            segundafilastring=segundafilastring+guardaoperaciones[i]+espacios+str(segundafila[i])
            for j in range(0, len(espacios)+1+len(str(segundafila[i]))):
                tercerafilastring=tercerafilastring+"-"
            for j in range (0, len(espacios)+1 + len(str(segundafila[i]))-len(str(cuartafila[i]))):
                cuartafilastring=cuartafilastring+" "
            cuartafilastring=cuartafilastring+str(cuartafila[i])
        else:
            segundafilastring=segundafilastring+guardaoperaciones[i]+" "+str(segundafila[i])
            espacios = " "
            for j in range(0,(1+len(str(segundafila[i]))-len(str(numero)))):
                espacios=espacios + " "
            primerafilastring=primerafilastring+espacios+str(numero)
            for j in range(0,len(espacios)+len(str(numero))):
                tercerafilastring=tercerafilastring+"-"
            for j in range (0, len(espacios)+ len(str(numero))-len(str(cuartafila[i]))):
                cuartafilastring=cuartafilastring+" "
            cuartafilastring=cuartafilastring+str(cuartafila[i])
        i+=1
        if status is True:
            arranged_problems = primerafilastring + "\n" + segundafilastring + "\n" + tercerafilastring+"\n"+cuartafilastring
        else:
            arranged_problems = primerafilastring+"\n"+segundafilastring+"\n"+tercerafilastring
    return arranged_problems