import numpy as np
from matplotlib import pyplot as plt
import cv2
img1 = cv2.imread('imagen1.jpg')
img1=cv2.resize(img1,(600,400))
img2 = cv2.imread('imagen2.jpg')
img2=cv2.resize(img2,(600,400))




#suma met1
suma =img1+img2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('suma',suma)
cv2.waitKey(0)
cv2.destroyAllWindows()
#suma met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
suma=cv2.add(img1,img2)
cv2.imshow('suma',suma)
cv2.waitKey(0)
cv2.destroyAllWindows()
#suma met3
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
suma=cv2.bitwise_or(img1,img2)
cv2.imshow('suma',suma)
cv2.waitKey(0)
cv2.destroyAllWindows()




#resta met1
resta =img2-img1
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('resta',resta)
cv2.waitKey(0)
cv2.destroyAllWindows()
#resta met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
resta=cv2.subtract(img1,img2)
cv2.imshow('resta',resta)
cv2.waitKey(0)
cv2.destroyAllWindows()
#resta met3



#multiplicacion met1
multi =img1*img2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
cv2.imshow('multiplicacion',multi)
cv2.waitKey(0)
cv2.destroyAllWindows()

#multiplicacion met2
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
multi=cv2.multiply(img1,img2)
cv2.imshow('multiplicacion',multi)
cv2.waitKey(0)
cv2.destroyAllWindows()

#multiplicacion met3
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
multi=cv2.bitwise_and(img1,img2)
cv2.imshow('multiplicacion',multi)
cv2.waitKey(0)
cv2.destroyAllWindows()





#division met 1 
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
div=cv2.divide(img1,img2)
cv2.imshow('division',div)
cv2.waitKey(0)
cv2.destroyAllWindows()


#division met 2 
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
div=img2/img1
cv2.imshow('division',div)
cv2.waitKey(0)
cv2.destroyAllWindows()


#potencia
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
pot=cv2.pow(img1,2)
cv2.imshow('potencia1',pot)
pot=cv2.pow(img2,2)
cv2.imshow('potencia2',pot)
cv2.waitKey(0)
cv2.destroyAllWindows()




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
cv2.waitKey(0)
cv2.destroyAllWindows()






















