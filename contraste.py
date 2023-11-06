import cv2 
from listar import *
from tamanho import *
  
def BrightnessContrast(brightness=0): 
   
    brightness = cv2.getTrackbarPos('Brightness', 
                                    'GEEK') 
      
    contrast = cv2.getTrackbarPos('Contrast', 
                                  'GEEK') 
  
    effect = controller(img, brightness,  contrast) 
  
    
    
    cv2.imshow('Effect', effect) 
  
def controller(img, brightness=255, 
               contrast=127): 
    
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255)) 
  
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127)) 
  
    if brightness != 0: 
        if brightness > 0: 
            shadow = brightness 
            max = 255
        else: 
            shadow = 0
            max = 255 + brightness 
            al_pha = (max - shadow) / 255
            ga_mma = shadow 
            cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma) 
  
    else: 
        cal = img 
  
    if contrast != 0: 
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast)) 
        Gamma = 127 * (1 - Alpha) 
        cal = cv2.addWeighted(cal, Alpha,  cal, 0, Gamma) 
  
    
    cv2.putText(cal, 'B:{},C:{}'.format(brightness, 
                                        contrast), (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
  
    return cal 
  
#if __name__ == '__main__': 
    
def todas_imagens():
    original = cv2.imread("img.jpg") 


    #img = original.copy() 



    arquivos = listardiretorio("imagens")


    for arq in arquivos:
        

        img = tamanho("imagens/"+arq)
        

        cv2.imshow('GEEK', img) 
        
            
            
            
        cv2.createTrackbar('Brightness', 'GEEK', 172, 2 * 255, BrightnessContrast)  
            
            
        cv2.createTrackbar('Contrast', 'GEEK', 190, 2 * 127, BrightnessContrast)   
        
            
        BrightnessContrast(0) 
        
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        
"""img = tamanho("img.jpg")
teste = controller(img, 172, 190)
cv2.imshow('GEEK', img) 
cv2.imshow('GEK', teste) 


cv2.waitKey(0)
cv2.destroyAllWindows() """