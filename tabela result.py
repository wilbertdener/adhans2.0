from listar import *
from tamanho import *
import statistics
import math
from bd import *
from rois import *


def bd_dados_padronizados():

    allarq = get_nome()
    rgb=[]
    canalrgb =[]
    canalhsv =[]
    canalhls =[]

    valorrgb=[]
    valorhsv=[]
    valorhls=[]

    valortime0=[]
    valorrgbbd=[]
    valorhsvbd=[]
    valorhlsbd=[]
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
        
        canalhsv.append((pixel_dentro[1][0])-(pixel_fora[1][0]))
        canalhsv.append((pixel_dentro[1][1])-(pixel_fora[1][1]))
        canalhsv.append((pixel_dentro[1][2])-(pixel_fora[1][2]))
        
        canalhls.append((pixel_dentro[2][0])-(pixel_fora[2][0]))
        canalhls.append((pixel_dentro[2][1])-(pixel_fora[2][1]))
        canalhls.append((pixel_dentro[2][2])-(pixel_fora[2][2]))
        
        #rgb[1]=int(pixel_dentro[0][1])-int(pixel_fora[0][1])
        #rgb[2]=int(pixel_dentro[0][2])-int(pixel_fora[0][2])
        #print(canal)
        dados_padra(canalrgb, canalhsv, canalhls, bd[0], bd[1] )
        if(bd[1]=='0s'):
            valortime0.append(canalrgb)
            valortime0.append(canalhsv)
            valortime0.append(canalhls)
        else:
            
            
            valorrgbbd.append(abs(abs(valortime0[0][0])-abs(canalrgb[0])))
            valorrgbbd.append(abs(abs(valortime0[0][1])-abs(canalrgb[1])))
            valorrgbbd.append(abs(abs(valortime0[0][2])-abs(canalrgb[2])))
            
            valorhsvbd.append(abs(abs(valortime0[1][0])-abs(canalhsv[0])))
            valorhsvbd.append(abs(abs(valortime0[1][1])-abs(canalhsv[1])))
            valorhsvbd.append(abs(abs(valortime0[1][2])-abs(canalhsv[2])))
            
            valorhlsbd.append(abs(abs(valortime0[2][0])-abs(canalhls[0])))
            valorhlsbd.append(abs(abs(valortime0[2][1])-abs(canalhls[1])))
            valorhlsbd.append(abs(abs(valortime0[2][2])-abs(canalhls[2])))
            dados_padra_semtime(valorrgbbd, valorhsvbd, valorhlsbd, bd[0] )
            valortime0=[]
            valorrgbbd=[]
            valorhsvbd=[]
            valorhlsbd=[]
        
        canalrgb =[]
        canalhsv =[]
        canalhls =[]
        
    
def bd_probabilidade(num,grupo):
    df = get_dados_pad_les_tim()
    df = df.drop('id', axis=1)
    rgb=[]
    hsv=[]
    hls=[]

    filtro = df[df['grupo'].str.startswith(grupo)]
    
    rgb.append(cria_prob(filtro,'r',num) )
    rgb.append(cria_prob(filtro,'g',num))
    rgb.append(cria_prob(filtro,'b',num))
    
    hsv.append(cria_prob(filtro,'h1',num))
    hsv.append(cria_prob(filtro,'s1',num))
    hsv.append(cria_prob(filtro,'v',num))
    
    hls.append(cria_prob(filtro,'h2',num))
    hls.append(cria_prob(filtro,'l',num))
    hls.append(cria_prob(filtro,'s2',num))
    
    
    
    probabilidade(rgb, hsv, hls, grupo,num )

def cria_prob(df,canal,num):
    menor=0
    
    for x in df[canal]:
        
        if(x<num):
            menor=menor+1
   
    prob="{:.2f}".format(float(menor/len(df)))
    
        
    return float(prob)


#bd_dados_padronizados()

def prob_menor_que(menor):
    bd_probabilidade(menor,"H")
    bd_probabilidade(menor,"V")
    bd_probabilidade(menor,"F")
    

def qtde_aceito(num,canal):
    df = get_dados_pad_les_tim()
    df = df.drop('id', axis=1)
    filtroh = df[df['grupo'].str.startswith("H")]
    filtrof = df[df['grupo'].str.startswith("F")]
    filtrov = df[df['grupo'].str.startswith("V")]
    menorf=0
    menorh=0
    menorv=0
    
    for x in filtrof[canal]:
        
        if(x<num):
            menorf=menorf+1
            
    for x in filtroh[canal]:
        
        if(x<num):
            menorh=menorh+1
            
    for x in filtrov[canal]:
        
        if(x<num):
            menorv=menorv+1
    
    
    print("Total canal "+canal+" : \n ")
    print("F : "+str(menorf)+" \nprob no grupo F: "+str("{:.2f}".format(menorf/len(filtrof)))+" \n ")
    print("H : "+str(menorh)+" \nprob no grupo H: "+str("{:.2f}".format(menorh/len(filtroh)))+" \n ")
    print("V : "+str(menorv)+" \nprob no grupo V: "+str("{:.2f}".format(menorv/len(filtrov)))+" \n ")
    
qtde_aceito(10,'r')
qtde_aceito(10,'g')
qtde_aceito(10,'b')