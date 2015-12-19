from opencv import *
from opencv.highgui import *
from opencv.cv import *
from random import randint
from random import random

def checkCheto(diff):
    nx = diff.height/30 #valor salto x
    ny = diff.width/30 #valor salto y
    px,py = 0,0 # posicion actual de x e y
    cont_pixCambiados = 0
    n_muestras = 0 #numero de muestras
    
    while px<diff.height:
        while py<diff.width:
            pixel=diff[px][py]
            cambio=pixel[0] + pixel[1] + pixel[2]
            if cambio>60:
                cont_pixCambiados += 1
            py+=ny
            n_muestras+=1
        px+=nx
    
    return cont_pixCambiados>(n_muestras/8)
    

def waitAndExit(char, fps):
    key = cvWaitKey(fps)
    if key == char:
        exit()      
        
def creaFont():
    return cvInitFont(CV_FONT_HERSHEY_DUPLEX, 1, 1, 1, 4, 8)

def addContador(frame, puntuacion):
    font = creaFont()
    cvPutText(frame, str(puntuacion), (15, frame.height-20), font, CV_RGB(148,203,30))
    cvPutText(frame, str("Mata Droides."), (15, 35), font, CV_RGB(148,203,30))
         

class Bug:
    def __init__(self, frame):
        self.imagen = self.select_image(0)
        self.x = randint(0,frame.height-20)
        self.y = randint(0,frame.width-20)
        self.time = 0
        self.etnia = 0
        self.state = "protegido"
        self.randomDestiny = random()
        self.frame = frame
        self.vel = randint(0,5)

    def actualizar(self):
        randomP = random()
        randomStep = random()
        vel = self.vel
        if self.randomDestiny<0.16:
            if (randomP < 0.7):
                self.x += vel
                self.y += vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel
        if(self.randomDestiny<0.32):
            if(randomP < 0.7):
                self.x += vel
                #self.y += vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel    
        if(self.randomDestiny<0.48):
              if(randomP < 0.7):
                self.x -= vel
                #self.y += vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel  
        if(self.randomDestiny<0.64):
              if(randomP < 0.7):
                self.x += vel
                self.y -= vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel        
        if(self.randomDestiny<0.80):
            if(randomP < 0.7):
                #self.x += vel
                self.y -= vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel
        if(self.randomDestiny<0.96):
              if(randomP < 0.7):
                #self.x += vel
                self.y += vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel        
        if(self.randomDestiny<0.64):
              if(randomP < 0.7):
                self.x += vel
                self.y -= vel
        else:
            if(randomStep<0.2):
                self.y +=vel
            elif(randomStep<0.4):
                self.x +=vel
            elif(randomStep<0.6):
                self.y -=vel
                self.x -=vel
            elif(randomStep<0.8):
                self.x +=vel
                self.y -=vel
            else:
                self.x -=vel
                self.y +=vel            
        if self.x > self.frame.height-20:
            self.x = 0
        if self.y > self.frame.width-20:
            self.y = 0
                                  
                        
    def render(self, diff):
            #Comprobamos si se ha tocado
            diffPx = diff[self.x][self.y]
            
            if self.state == "vivo":
                if (diffPx[0] + diffPx[1] + diffPx[2]) > 50 and not checkCheto(diff):
                    self.time = 0
                    self.state = "muerto"
            elif self.state == "protegido" and self.time > 10:
                self.state = "vivo"
            elif self.state == "muerto":
                if self.time >= 20:
                    self.time = 0
                    self.state = "vivo"
                    self.randomDestiny = random()
                    self.x = randint(0,frame.height-20)
                    self.y = randint(0,frame.width-20)

            
            self.time += 1
            if self.state == "vivo":
                return self.imagen.next()
            elif self.state == "protegido":
                return sprite[2][0]
            else:
                return sprite[1][0]
                       
    
     
            
    def select_image(self, selec): # selec: seleccionada 
        while 1:
            for s in sprite[selec][1:]:
                contador = 0 
                while contador < 1:
                    contador += 1
                    yield s
                yield s
    

def put_image(img, sub_img, start_x,start_y):
    x = 0
    y = 0
    while x < sub_img.height:
        while y < sub_img.width:
            pix = sub_img[x][y]
            if pix[0] != 0.0 and pix[1] != 0.0 and pix[2] != 0.0:
                img[start_x+x][start_y+y] = pix
            y += 1
        y = 0
        x += 1

capture = cvCreateCameraCapture(0)

frame_pre = cvQueryFrame(capture)
diff = cvCloneImage(frame_pre)
fullscreen = cvCreateImage((800,600), diff.depth, diff.nChannels)
sprite = ([], [], []) 

for x in [0,1,2,1,3]:
    sprite[0].append(cvLoadImage("sprites/andro%d.png" % x)) 
    sprite[1].append(cvLoadImage("sprites/hadroid%d.png" % x)) 
    sprite[2].append(cvLoadImage("sprites/ufo%d.png" % x))

listaBug = (Bug(frame_pre), Bug(frame_pre), Bug(frame_pre))
puntuacion = 0

while 1:
    frame = cvQueryFrame(capture)
    cvFlip(frame, None, 1)
    cvAbsDiff(frame_pre, frame, diff)
    frame_pre = cvCloneImage(frame)
    
    for bug in listaBug:
        bug.select_image(1)
        if bug.state != "muerto":
            bug.actualizar()
        else:
            puntuacion += 2**bug.vel
        put_image(frame, bug.render(diff), bug.x,bug.y)
    addContador(frame, puntuacion)
    cvResize(frame, fullscreen)
    cvShowImage("Frame", fullscreen)
    key = cvWaitKey(1)
    if key == " ": 
        break

