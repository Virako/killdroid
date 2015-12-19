from opencv import *
from opencv.highgui import *
from opencv.cv import *
from random import randint
import time
import copy

# Cargamos una imagen
#img = cvLoadImageM("jezu.jpg")
#cvShowImage("Imagen", img)
#cvWaitKey(30) # milisegundos
#cvDestroyWindow("Imagen")

# Cargamos un video
cam = cvCreateCameraCapture(0)

# Hallamos la diferencia entre imagenes
def difference(img1, img2):
    """Devuelve la diferencia entre dos matrices/imagenes dadas, 
       aplicandoles anteriormente el efecto Smooth"""
    aux1 = cvCreateMat(img1.rows, img1.cols, img1.type)
    aux2 = cvCreateMat(img1.rows, img1.cols, img1.type)
    res = cvCreateMat(img1.rows, img1.cols, img1.type)
    cvAbsDiff(img1, img2, res)
    return res

# Bucle que lo prueba todo
fps = 50
contador = 3000
primera = 20  # Para comenzar con un retardo de 1 segundo
tocado = False
# sistema puntuacion
tiempo = 30
t0 = time.time() # segundos
puntos = 0

while 1:
    img = cvQueryFrame(cam) # capturamos un frame de la camara
    cvFlip(img, None, 1) # volteamos la imagen sobre la vertical
    contador += fps
    if tocado or contador >= 3000:                                  
        contador = 0
        tocado = False
        x = randint(0, img.height)     # pos aleatoria
        y = randint(0, img.width)
        r1 = randint(-1,1)
        r2 = randint(-1,1)
        vel = randint(2,10)
    else:
        x += int(vel*r1)
        y += int(vel*r2)
        if x <= 0: 
            x = 0
            contador = 3000
        elif y <= 0: 
            y = 0
            contador = 3000
        elif x >= img.height: 
            x = img.height-1
            contador = 3000
        elif y >= img.width: 
            y = img.width-1
            contador = 3000
        
    if r1 == 0 and r2 == 0:
        cvCircle(img, (y,x), 5, CV_RGB(0,0,255), 2, 8, 0) # pintamos el circulo
    elif vel == 9:
        cvCircle(img, (y,x), 5, CV_RGB(255,255,0), 2, 8, 0) # pintamos el circulo
    else:
        cvCircle(img, (y,x), 5, CV_RGB(255,0,0), 2, 8, 0) # pintamos el circulo

    # Guardamos la imagen anterior en img_ant si es valida TODO
    if not primera:
        diff = difference(img_ant, img)
        total = diff[x,y][0] + diff[x,y][1] + diff[x,y][2]
        if total >= 50 and contador > 10*fps:
            cvCircle(img, (y,x), 5, CV_RGB(0,255,0), 2, 8, 0) # pintamos el circulo
            tocado = True
    else:
        primera -= 1
    img_ant = cvCloneImage(img) 

    # Puntuacion
    if tocado:
        puntos += 2**vel
    t1 = int(time.time() - t0)
    if tiempo < t1:
        lineas = []
        add = 0
        nombre = raw_input("Inserta tu nombre: ")
        nombre = nombre.replace(" ", "_")

        f = open("Ranking.txt", "r")
        linea = f.readline().split()
        while linea:
            if puntos > int(linea[1]) and add == 0:
                lineas.append(nombre + " " + str(puntos) + "\n")
                add = 1
            lineas.append(linea[0] + " " + linea[1] + "\n")
            linea = f.readline().split()
        if add == 0:
            lineas.append(nombre + " " + str(puntos) + "\n")

        f = open("Ranking.txt", "w")
        f.writelines(lineas)
        f.close()
        from os import popen2
        popen2("cat -n Ranking.txt")
        break

    # Mostrar puntuacion
    font = cvInitFont(CV_FONT_HERSHEY_DUPLEX, 1, 1, 0, 1, 8)
    cvPutText(img, str(puntos), (50, img.height-50), font, CV_RGB(255,0,0))
    cvPutText(img, str(tiempo-t1), (img.width-40, img.height-40), font, CV_RGB(255,0,0))
    
    cvShowImage("Video", img) # mostramos la imagen

    key = cvWaitKey(fps) # return (explicar)
    if key == (" " or "\n"):
        print key, "WHATT"
        break
