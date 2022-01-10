import copy
import random
# Consider using the modules imported above.

#Este problema es complejo, porque a priori no se los argumentos que me van a entrar.
#Por ello, usamos **kwargs. El **kwargs significa que vamos a meter muchos argumentos en forma diccionario: clave = valor
#Despues, iteramos el **kwargs para ir guardando la clave como variable y el valor.
class Hat:
    def __init__(self, **kwargs):
        contents=[]
        for color, numero in kwargs.items():
            for i in range (0,numero):
                contents.append(color)
        self.contents=contents
    def draw(self,numero):
        if(numero>=len(self.contents)):
            devuelto=self.contents.copy()
            self.contents.clear()
            return devuelto
        else:
            devuelto=[]
            for i in range (0,numero):
                aleatorio = random.randint(0,len(self.contents)-1)
                color_sacado=self.contents[aleatorio]
                del self.contents[aleatorio]
                devuelto.append(color_sacado)
            return devuelto
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experimentos_acertados=0
    for i in range(0, num_experiments):
        copia=copy.deepcopy(hat)
        bolas_sacadas=copia.draw(num_balls_drawn)
        convertidoadiccionario= {k:bolas_sacadas.count(k) for k in bolas_sacadas}

        controlador=0
        for a,b in expected_balls.items():
            sacadodiccionario=convertidoadiccionario.get(a)
            if sacadodiccionario is None:
                controlador = controlador+1
            elif (sacadodiccionario>=b):
                controlador=controlador+0
            else:
                controlador = controlador + 1
        if controlador == 0:
            experimentos_acertados+=1
    probabilidad=experimentos_acertados/num_experiments
    return probabilidad



