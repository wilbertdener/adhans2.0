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
    


def salva_no_bd():
    
    allarq = get_nome()
    for arq in allarq:
        bd = list(arq.split(" "))
        histamina(bd[0][0],bd[0], bd[1])
        
        
        pixel_dentro = moda(arq,"dentro")
        dados(pixel_dentro[0], pixel_dentro[1], pixel_dentro[2], bd[0], bd[1], "dentro",pixel_dentro[3])
        
        
        pixel_fora = moda(arq,"fora")
        dados(pixel_fora[0], pixel_fora[1], pixel_fora[2], bd[0], bd[1], "fora",pixel_fora[3])
            
   
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
    
    



# dados -> 216 ->72
# histamina -> 36 ->36
#salva_no_bd()

#teste_histamina('H1-1')

df= todos_dados()
df_fora = df[df['lesao'] == "fora"]
df_dentro =df[df['lesao'] == "dentro"]

df_dentro_antes = df_dentro[df_dentro['tempo'] == "0s"]
df_dentro_pos = df_dentro[df_dentro['tempo'] == "30s"]
#print(df_dentro_antes.sort_values(by=['foto']).head())
#print(df_dentro_pos.sort_values(by=['foto']).head())

#print(df_dentro_pos[df_dentro_pos['foto'].str.startswith('H1')].sort_values(by=['foto']).head())

df_ordenado = df.sort_values(by=['foto','lesao','tempo'])
df_ordenado = df_ordenado.drop(['h1', 'h2','total_pixels','id'], axis=1)
filtro = df_ordenado[df_ordenado['foto'].str.startswith('H3')]
print(filtro)
df_ordenado.to_excel("resultados.xlsx")