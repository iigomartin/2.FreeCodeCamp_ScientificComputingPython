class Category:

    #Mucho cuidado con las listas por default en Python, porque al crear nuevos objetos heredan las listas anteriores.
    #Hay que hacer el artificio del ledger = None y el if.
    def __init__(self,category,ledger=None):
        if ledger is None:
            ledger = []
        self.category = category
        self.ledger=ledger
    def deposit(self,amount,description=""):
        dict = {"amount":amount,"description":description}
        self.ledger.append(dict)

    def withdraw(self, amount, description=""):
        dinerohastaahora=0
        for a in self.ledger:
            dinerohastaahora=dinerohastaahora+a.get("amount")
        if(dinerohastaahora>=amount):
            dict = {"amount": -amount, "description": description}
            self.ledger.append(dict)
            return True
        else:
            return False
    def get_balance(self):
        dinerohastaahora = 0
        for a in self.ledger:
            dinerohastaahora = dinerohastaahora + a.get("amount")
        return dinerohastaahora
    def transfer(self,amount,othercategory):
        dinerohastaahora = 0
        for a in self.ledger:
            dinerohastaahora = dinerohastaahora + a.get("amount")
        if (dinerohastaahora >= amount):
            dict1 = {"amount": -amount, "description": "Transfer to "+othercategory.category}
            othercategory.deposit(amount,"Transfer from "+self.category)
            self.ledger.append(dict1)
            return True
        else:
            return False
    def check_funds(self,amount):
        cantidadquetengo=self.get_balance()
        if (cantidadquetengo>=amount):
            return True
        else:
            return False
    def __str__(self):
        category=self.category
        titulo=category
        if(len(category)%2==0):
            contador=0
            for i in range (0,(30-len(category))):
                if(contador%2):
                    titulo="*"+titulo
                else:
                    titulo=titulo+"*"
                contador+=1
        else:
            category="*"+self.category
            titulo=category
            contador = 0
            for i in range(0, (30 - len(category))):
                if (contador % 2):
                    titulo = "*" + titulo
                else:
                    titulo = titulo + "*"
                contador += 1
        cuerpo="\n"
        for a in self.ledger:
            primeramitad=""
            if(len(a.get("description"))>=23):
                primeramitad=""+a.get("description")[0:23]
            else:
                primeramitad=""+a.get("description")+" "*(23-len(a.get("description")))
            segundamitad=" "*(7-len("{:.2f}".format(float(a.get("amount")))))+"{:.2f}".format(float(a.get("amount")))
            cuerpo=cuerpo+primeramitad+segundamitad+"\n"
        balance=str(self.get_balance())
        total="Total: "+balance
        completo=titulo+cuerpo+total
        return completo



def create_spend_chart(categories):
    total=0
    list=[]
    for a in categories:
        totalparcial = 0
        for b in a.ledger:
            if b.get("amount")<0:
                totalparcial=totalparcial+b.get("amount")
        list.append({"category": a.category,"amount": totalparcial})
        total=total+totalparcial
    print(total)
    print(list)
    for a in list:
        valor=a.get("amount")
        valorporciento=valor/total
        a["amount"]=int((10*valorporciento))

    print(list)

    titulo="Percentage spent by category\n"
    cuerpo=""
    for i in range(0, 11):
        numero=10-i
        if (i==0):
            primeraparte=str(numero)+"0|"
        elif(i==10):
            primeraparte="  "+str(numero)+"|"
        else:
            primeraparte=" "+str(numero)+("0|")
        cuerpo=cuerpo+primeraparte+" "
        for a in list:
            if(a.get("amount")>=10-i):
                cuerpo=cuerpo+"o  "
            else:
                cuerpo=cuerpo+"   "
        cuerpo=cuerpo+"\n"
    lineas="    -"+"---"*len(list)+"\n"

    caracteres_mas_largo = 0
    for a in categories:
        if(caracteres_mas_largo<len(a.category)):
            caracteres_mas_largo=len(a.category)
    listanombresespaciosbien=[]

    for a in categories:
        if(len(a.category)<caracteres_mas_largo):
            titulo2=a.category+" "*(caracteres_mas_largo-len(a.category))
        else:
            titulo2=a.category
        listanombresespaciosbien.append(titulo2)

    finales=""
    for b in range(0, caracteres_mas_largo):
        parcial="     "
        for a in listanombresespaciosbien:
            parcial=parcial+a[b]+"  "
        if(b==caracteres_mas_largo-1):
            extra=""
        else:
            extra="\n"
        finales=finales+parcial+extra

    return titulo+cuerpo+lineas+finales