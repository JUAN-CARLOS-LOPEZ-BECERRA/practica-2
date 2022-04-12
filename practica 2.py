import numpy as np
from matplotlib import pyplot as plt
import cv2

img1 = cv2.imread('imagen1.jpg')
img1=cv2.resize(img1,(600,400))
img2 = cv2.imread('imagen2.jpg')
img2=cv2.resize(img2,(600,400))


def key():
    k = cv2.waitKey(0)&0xFF

    if k==ord('j'):
       cv2.destroyAllWindows() 

     
#suma met1
suma =img1+img2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('suma',suma)
key()
    

#suma met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
suma=cv2.add(img1,img2)
cv2.imshow('suma',suma)
key()
#suma met3
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
suma=cv2.bitwise_or(img1,img2)
cv2.imshow('suma',suma)
key()





#resta met1
resta =img2-img1
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('resta',resta)
key()

#resta met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
resta=cv2.subtract(img1,img2)
cv2.imshow('resta',resta)
key()

#resta met3



#multiplicacion met1
multi =img1*img2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('multiplicacion',multi)
key()


#multiplicacion met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
multi=cv2.multiply(img1,img2)
cv2.imshow('multiplicacion',multi)
key()

#multiplicacion met3
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
multi=cv2.bitwise_and(img1,img2)
cv2.imshow('multiplicacion',multi)
key()


#division met 1 
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
div=cv2.divide(img1,img2)
cv2.imshow('division',div)
key()

#division met 2 
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
div=img2/img1
cv2.imshow('division',div)
key()

#potencia
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
pot=cv2.pow(img1,2)
cv2.imshow('potencia1',pot)
pot=cv2.pow(img2,2)
cv2.imshow('potencia2',pot)
key()


#OR
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
suma=cv2.bitwise_or(img1,img2)
cv2.imshow('OR',suma)
key()
#AND
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
res=cv2.bitwise_and(img1,img2)
cv2.imshow('AND',res)
key()

#NOT
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
res=cv2.bitwise_not(img1)
cv2.imshow('NOT1',res)
res2=cv2.bitwise_not(img2)
cv2.imshow('NOT2',res2)
key()


#traslacion
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
col = img1.shape[1] #columnas
fil = img1.shape[0] # filas
Img1= cv2.getRotationMatrix2D((col//2,fil//2),156,1)
res=cv2.warpAffine(img1,Img1,(col,fil))
cv2.imshow('traslacion 1',res)

col2 = img2.shape[1] #columnas
fil2 = img2.shape[0] # filas
Img2= cv2.getRotationMatrix2D((col2//2,fil2//2),156,1)
res2=cv2.warpAffine(img2,Img2,(col,fil))
cv2.imshow('traslacion 2',res2)
key()

#interpolcion
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
res= cv2.resize(img1,(400,300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('interpolacion1',res)

res2= cv2.resize(img2,(400,300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('interpolacion2',res2)
key()
'''
#logaritmo natural
#cv2.imshow('imagen1',img1)
#cv2.imshow('imagen2',img2)
#log1=cv2.log(img1,)
#log2=cv2.log(img2,)
#cv2.imshow('logaritmo natural1',log1)
#cv2.imshow('logaritmo natural2',log2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#raiz
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
div=cv2.sqrt(img1)
cv2.imshow('division',div)
key()'''





























