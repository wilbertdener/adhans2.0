from listar import *
from tamanho import *
import statistics
import math
from bd import *

def lista_pixel(arq, local, tipo):
    pixels = []
    
    for i in range(1,4):
        rgb = cv2.imread("roi "+local+"/"+arq+"roi"+str(i)+".jpg")
       
        
        if(tipo=="hsv"):
            img = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
        elif(tipo=="hls"):
            img = cv2.cvtColor(rgb, cv2.COLOR_BGR2HLS)
        else:
            img = rgb.copy()
        
        for a in range(img.shape[0]):
            for b in range(img.shape[1]):
                pixels.append(str(img[a][b]))
            
    return pixels

def juncao(arq, local):#aqui
    vet=[[],[],[]]
    
        
                
    vet[0].append(lista_pixel(arq, local, 'rgb'))
    vet[1].append(lista_pixel(arq, local, 'hsv'))        
    vet[2].append(lista_pixel(arq, local, 'hls'))
    
        
    return vet
    
    
    
            
def moda(arq, local):
    
    pixels = juncao(arq, local)      
    
    
    moda = statistics.mode(pixels[0][0])
    canaisrgb = list(moda[1:len(moda)-1].split(" "))
    canaisrgb = list(filter(None,canaisrgb))

    
    modahsv = statistics.mode(pixels[1][0])
    canaishsv = list(modahsv[2:len(moda)-1].split(" "))
    canaishsv = list(filter(None,canaishsv))

    
    modahls = statistics.mode(pixels[2][0])
    canaishls = list(modahls[2:len(moda)-1].split(" "))
    canaishls = list(filter(None,canaishls))
    #canaishls = canaishls.replace('[', '')
    #canaishls = canaishls.replace(']', '')


    rgb=[]
    hsv=[]
    hls=[]
    rgb.append(int(canaisrgb[2]))
    rgb.append(int(canaisrgb[1]))
    rgb.append(int(canaisrgb[0]))

    hsv.append(int(canaishsv[0]))
    hsv.append(int(canaishsv[1]))
    hsv.append(int(canaishsv[2]))

    hls.append(int(canaishls[0]))
    hls.append(int(canaishls[1]))
    hls.append(int(canaishls[2].replace(']', '')))

    return [rgb,hsv,hls,len(pixels[0][0])]
    


def salva_no_bd(nome1= None ,nome2=None):
    canalrgb =[]
    canalhsv =[]
    canalhls =[]


    valortime0=[]
    valorrgbbd=[]
    valorhsvbd=[]
    valorhlsbd=[]
    
    if(nome1):
        allarq = get_nome(False,nome1,nome2)
        
        
    else:
        allarq = get_nome()
        
    
    #print(allarq)
    count =0
    for arq in allarq:
        bd = list(arq.split(" "))
        #histamina(bd[0][0],bd[0], bd[1])
        nome=nome1[:-1]
        if(count==0):
            
            tempo="0s"
            count=count+1
        else:
            tempo="30s"
            count=0
        
        
        pixel_dentro = moda(bd[0]+" "+tempo,"dentro")
        
        dados(pixel_dentro[0], pixel_dentro[1], pixel_dentro[2], nome, tempo, "dentro",pixel_dentro[3])
        #print(pixel_dentro)
        
        pixel_fora = moda(bd[0]+" "+tempo,"fora")
        #print(pixel_fora)
        #print('\n\n')
        
        dados(pixel_fora[0], pixel_fora[1], pixel_fora[2], nome, tempo, "fora",pixel_fora[3])
        
        canalrgb.append(abs((pixel_dentro[0][0])-(pixel_fora[0][0])))
        canalrgb.append(abs((pixel_dentro[0][1])-(pixel_fora[0][1])))
        canalrgb.append(abs((pixel_dentro[0][2])-(pixel_fora[0][2])))
        
        canalhsv.append(abs((pixel_dentro[1][0])-(pixel_fora[1][0])))
        canalhsv.append(abs((pixel_dentro[1][1])-(pixel_fora[1][1])))
        canalhsv.append(abs((pixel_dentro[1][2])-(pixel_fora[1][2])))
        
        canalhls.append(abs((pixel_dentro[2][0])-(pixel_fora[2][0])))
        canalhls.append(abs((pixel_dentro[2][1])-(pixel_fora[2][1])))
        canalhls.append(abs((pixel_dentro[2][2])-(pixel_fora[2][2])))
        
        #rgb[1]=int(pixel_dentro[0][1])-int(pixel_fora[0][1])
        #rgb[2]=int(pixel_dentro[0][2])-int(pixel_fora[0][2])
        #print(canal)
        dados_padra(canalrgb, canalhsv, canalhls, bd[0][:-1], tempo )
        if(tempo=='0s'):
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
            print(valorrgbbd)
            print(valorhsvbd)
            print(valorhlsbd)
            print(bd[0][:-1])
            dados_padra_semtime(valorrgbbd, valorhsvbd, valorhlsbd, bd[0][:-1] )
            valortime0=[]
            valorrgbbd=[]
            valorhsvbd=[]
            valorhlsbd=[]
        
        canalrgb =[]
        canalhsv =[]
        canalhls =[]
            
   
def get_nome(chave=True,nome1=None,nome2=None):
    if(nome1):
        arq = listardiretorio("roi dentro")
        arquivos=[]
        arq2 = []
        allarq = []
        allarq2 = []
        for x in arq:
            
            if(x.startswith(nome1)):
                arquivos.append(x)
                
            if(x.startswith(nome2)):
                arquivos.append(x)
                
        for sigla in sorted(set(arquivos)):
            allarq.append(sigla)
            
        for nome in allarq:
            allarq2.append(nome.split(" ")[0])
        if(chave):
            return allarq
        else:
            return sorted(set(allarq2))       
        
    else:
        arquivos = listardiretorio("roi dentro")
        arq2 = []
        allarq = []
        allarq2 = []
        for arq in arquivos:
            if(arq[8]=="s"):
                arq2.append(arq[0:9])
            elif(arq[7]=="s"):
                arq2.append(arq[0:8])
            elif(arq[9]=="s"):
                arq2.append(arq[0:10])
            elif(arq[6]=="s"):
                arq2.append(arq[0:7])
            else:
                print(arq)
            
            

        for sigla in sorted(set(arq2)):
            allarq.append(sigla)
            
        for nome in allarq:
            allarq2.append(nome.split(" ")[0])
        if(chave):
            return allarq
        else:
            return sorted(set(allarq2))

