from listar import *
from tamanho import *
import statistics
import math
from bd import *
from rois import *




allarq = get_nome()
rgb=[]
canalrgb =[]
canalhsv =[]
canalhls =[]
for arq in allarq:
    bd = list(arq.split(" "))
    histamina(bd[0][0],bd[0], bd[1])
    
    
    pixel_dentro = moda(arq,"dentro")
    #dados(pixel_dentro[0], pixel_dentro[1], pixel_dentro[2], bd[0], bd[1], "dentro",pixel_dentro[3])
    
    
    pixel_fora = moda(arq,"fora")
    #dados(pixel_fora[0], pixel_fora[1], pixel_fora[2], bd[0], bd[1], "fora",pixel_fora[3])
    canalrgb.append((pixel_dentro[0][0])-(pixel_fora[0][0]))
    canalrgb.append((pixel_dentro[0][1])-(pixel_fora[0][1]))
    canalrgb.append((pixel_dentro[0][2])-(pixel_fora[0][2]))
    
    canalhsv.append((pixel_dentro[0][0])-(pixel_fora[1][0]))
    canalhsv.append((pixel_dentro[0][1])-(pixel_fora[1][1]))
    canalhsv.append((pixel_dentro[0][2])-(pixel_fora[1][2]))
    
    canalhls.append((pixel_dentro[0][0])-(pixel_fora[2][0]))
    canalhls.append((pixel_dentro[0][1])-(pixel_fora[2][1]))
    canalhls.append((pixel_dentro[0][2])-(pixel_fora[2][2]))
    
    #rgb[1]=int(pixel_dentro[0][1])-int(pixel_fora[0][1])
    #rgb[2]=int(pixel_dentro[0][2])-int(pixel_fora[0][2])
    #print(canal)
    dados_padra(canalrgb, canalhsv, canalhls, bd[0], bd[1] )
    canalrgb =[]
    canalhsv =[]
    canalhls =[]