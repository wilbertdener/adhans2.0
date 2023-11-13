from listar import *
from tamanho import *
import statistics
import math
from bd import *

def lista_pixel(img):
    pixels = []
    for a in range(img.shape[0]):
        for b in range(img.shape[1]):
            pixels.append(str(img[a][b]))
            
    return pixels

def moda(img):
    #img = cv2.imread(diretorio)
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hlsimg = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    pixels = lista_pixel(img)
    pixelshsv = lista_pixel(hsvimg)        
    pixelshls = lista_pixel(hlsimg)       

                
    moda = statistics.mode(pixels)
    canaisrgb = list(moda[1:len(moda)-1].split(" "))
    canaisrgb = list(filter(None,canaisrgb))
    
    modahsv = statistics.mode(pixelshsv)
    canaishsv = list(modahsv[2:len(moda)-1].split(" "))
    canaishsv = list(filter(None,canaishsv))
    
    modahls = statistics.mode(pixelshls)
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
    
    return [rgb,hsv,hls]
    



#modas = moda("roi dentro/H4-1 (3)roi1.jpg")


#dados(modas[0], modas[1], modas[2], "H4", "dento")
def salva_no_bd():
    
    allarq = get_nome()
    for arq in allarq:
        bd = list(arq.split(" "))
        histamina(bd[0][0],bd[0], bd[1])
        
        for i in range(1,4):
            droi1 = cv2.imread("roi dentro/"+arq+"roi"+str(i)+".jpg")
            #print("roi dentro/"+arq+"roi"+str(i)+".jpg")
            pixel_dentro = moda(droi1)
            dados(pixel_dentro[0], pixel_dentro[1], pixel_dentro[2], arq, "dentro")
            
            froi1 = cv2.imread("roi fora/"+arq+"roi"+str(i)+".jpg")
            #print("roi fora/"+arq+"roi"+str(i)+".jpg")
            pixel_fora = moda(froi1)
            dados(pixel_fora[0], pixel_fora[1], pixel_fora[2], arq, "fora")
            
   
def get_nome(chave=True):
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

#print(get_nome(False))


#salva_no_bd()
"""df = get_dados('H1-1 0s')
print(df)
for x in df:
  print(x)"""
  
'''df = dados_pd('H1-1 0s')
df_fora = df[df ['lesao'] == "fora"]
df_dentro =df[df ['lesao'] == "dentro"]

print("dentro")
print(df_dentro.head())
print("fora")
print(df_fora.head())'''

def teste_histamina(diretorio):
    df_inicial = dados_pd(diretorio+' 0s')
    df_final = dados_pd(diretorio+' 30s')
    df = pd.concat([df_inicial, df_final])
    
    
    df_fora = df[df['lesao'] == "fora"]
    df_dentro =df[df['lesao'] == "dentro"]
    
    print("dentro")
    print(df_dentro.head(12))
    print("fora")
    print(df_fora.head(12))
    
    
teste_histamina('H1-1')