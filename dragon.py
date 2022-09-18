import random
import time

def mostrarIntroducción():
    print('************************************************')
    print('Un día un anciano extraño alto y con sombrero de punta llega a tu casa y te encomienda la misión de buscar un tesoro muy valioso que te dará una gran fortuna.') 
    print('El único problema que este tesoro está en una cueva habitada por dragones, algunos de ellos son amigables y permitirán compartirlo pero otros sin embargo son ambiciosos, crueles y si te ven te devorarán fácilmente...')
    print('Luego de pasar meses y meses enfrentandote a obstáculos, diferentes enemigos que no te adviriteron antes para llegar hasta aquel lugar te detienes frente a una')
    print('gran montaña, comienzas a escalarla y te encuentras con otra sorpresa.')
    print('Frente a ti hay dos cuevas, en una de ellas duerme un dragón generoso, amigable que te compartirá su tesoro, no obstante, en la otra cueva habitan dragones')
    print('hambrientos que devorán a cualquiera que entre') 
    print('************************************************')
    print('Haz llegado tan lejos y solo te queda optar para ingresar en una de las dos cuevas')
    print()

def elegirCueva():
        cueva = ''
        while cueva!='1' and cueva!='2':
            print('¿A qué cueva queres ingresar? La cueva 1 o 2?: ')
            cueva=input()            
        return cueva 
    
def explorarCueva(CuevaElegida):
        print('Te aproximas a la cueva...')
        time.sleep(2)
        print('Es oscura y espeluznante...')
        time.sleep(2)
        print('Un gran dragon aparece súbitamente frente a ti! Te observa detenidamente y...')
        print()
        time.sleep(3)
                
        cuevaAmigable=random.randint(1,2)
        
        if CuevaElegida == str(cuevaAmigable):
            print('Te comparte el tesoro')
        else:
            print('Te debora de un bocado!')
            
jugarDeNuevo ='si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
    
    mostrarIntroducción()
    numeroDeCueva=elegirCueva()
    explorarCueva(numeroDeCueva)
    print('Te gustaria volver a jugar? (Si/No): ')
    jugarDeNuevo=input()