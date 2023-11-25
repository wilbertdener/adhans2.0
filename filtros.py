
from listar import *
from tamanho import *
import statistics
import math
from bd import *
from rois import *
from statistics import median, mean
from math import isnan
from itertools import filterfalse

def qtde_aceito(num,canal):
    df = get_dados_pad_les_tim()
    df = df.drop('id', axis=1)
    filtroh = df[df['foto'].str.startswith("H")]
    filtrof = df[df['foto'].str.startswith("F")]
    filtrov = df[df['foto'].str.startswith("V")]
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
    


def filtro_viti(df):
    df0s = df[df['tempo']=='0s']
    filtroh = df0s[df0s['foto'].str.startswith("H")]
    filtrof = df0s[df0s['foto'].str.startswith("F")]
    filtrov = df0s[df0s['foto'].str.startswith("V")]
    
    filtroh2 = filtroh[abs(filtroh['s1'])<=40]
    filtrof2 = filtrof[abs(filtrof['s1'])<=40]
    filtrov2 = filtrov[abs(filtrov['s1'])<=40]
    
    '''print("Media han: "+str(mean(abs(filtroh['b']))))
    print("max han: "+str(max(abs(filtroh['b']))))
    #print(median(filtrof['r']))
    print("Media vit: "+str(mean(abs(filtrov['b']))))
    print("min vit: "+str(min(abs(filtrov['b']))))'''
        #b, - 31-55=24
        # s2, - 11-34=23
    # l - 29-44=15

        
        # b, - 31-55=24 han max=67; min,media vit=24,55
            # s2, - 11-34=23 han max=37; min,media vit=5,35
        # h1-5-11 han max=72; min,media vit=2,11
                        # s1 D=29 han max=41; min,media vit=21,46
    '''print("F :"+str(len(filtrof)))
    print("Filtro F :"+str(len(filtrof2))+"\n")                    
    print("H :"+str(len(filtroh)))
    print("Filtro H :"+str(len(filtroh2))+"\n")
    print("V :"+str(len(filtrov)))
    print("Filtro V :"+str(len(filtrov2))+"\n")'''
    
    
    result = pd.concat([filtroh2, filtrov2,filtrof2])
    
    return(result['foto'].values.tolist())
 
 
def filtro_han(nomes, num, canal):
    
    df = get_dados_pad_les_tim()
    df = df.drop('id', axis=1)
    dffiltro = df[df['foto']==nomes[0]].copy()
    for x in nomes[1:len(nomes)]:
        dffiltro = pd.concat([dffiltro,df[df['foto']==x]])
        
    
    #df =df[df['foto']==('H8-1'or 'H7-1')]
    filtrot = dffiltro[dffiltro[canal]>=num]
    filtroh = dffiltro[dffiltro['foto'].str.startswith("H")]
    filtrof = dffiltro[dffiltro['foto'].str.startswith("F")]
    filtrov = dffiltro[dffiltro['foto'].str.startswith("V")]
    menorh = filtroh[filtroh[canal]>=num]
    menorf = filtrof[filtrof[canal]>=num]
    menorv = filtrov[filtrov[canal]>=num]
    
    
    
    '''print("Total canal "+canal+" : \n ")
    print("F : "+str(len(menorf))+" \nprob no grupo F: "+str("{:.2f}".format(len(menorf)/44))+" \n ")
    print("H : "+str(len(menorh))+" \nprob no grupo H: "+str("{:.2f}".format(len(menorh)/18))+" \n ")
    print("V : "+str(len(menorv))+" \nprob no grupo V: "+str("{:.2f}".format(len(menorv)/11))+" \n ") 
    print("Total : "+str(len(filtrot))+" \nprob no grupo Total: "+str("{:.2f}".format(len(filtrot)/(44+18+11)))+" \n ") ''' 
    
    return(filtrot['foto'].values.tolist())


def acerto(df,nomes):
    qtdh = len(df[df['foto'].str.startswith("H")])
    qtdf = len(df[df['foto'].str.startswith("F")])
    qtdv = len(df[df['foto'].str.startswith("V")])
    qtd = len(df)
    
    df1 = df[df['foto']==nomes[0]].copy()
    for x in nomes[1:len(nomes)]:
        df1 = pd.concat([df1,df[df['foto']==x]])
    
    
    qtdhsel = len(df1[df1['foto'].str.startswith("H")])
    qtdfsel = len(df1[df1['foto'].str.startswith("F")])
    qtdvsel = len(df1[df1['foto'].str.startswith("V")])
    qtdsel = len(df1)
    
    acerto =  (qtdhsel+(qtdf-qtdfsel)+(qtdv-qtdvsel))/qtd
    erro =  ((qtdh-qtdhsel)+qtdvsel+qtdfsel)/qtd
    
    print("Porcentagem do software dizer que possui e ser verdade : {:.2f} %".format((qtdhsel/qtd)*100))
    print("Porcentagem do software dizer que possui e ser mentira : {:.2f} %".format((  (qtdvsel+qtdfsel)/qtd   )*100))
    print("Porcentagem do software dizer que não possui e ser verdade : {:.2f} %".format((((qtdf-qtdfsel)+(qtdv-qtdvsel))/qtd)*100))
    print("Porcentagem do software dizer que não possui e ser mentira : {:.2f} %".format(((qtdh-qtdhsel)/qtd)*100))
    print("\n\n")

    print("Porcentagem de acerto : {:.2f} %".format(acerto*100))
    print("Porcentagem de erro : {:.2f} %".format(erro*100))


def probabilidade_geral():
    df = get_dados_pad()

    print('Total amostra de F: '+str(len(df[df['grupo']=='F'])/2))
    print('Total amostra de H: '+str(len(df[df['grupo']=='H'])/2))
    print('Total amostra de V: '+str(len(df[df['grupo']=='V'])/2))
    print('Total amostra :'+str(len(df)/2)+"\n")
    vitifiltro = filtro_viti(df)
    filtrohan = filtro_han(vitifiltro,10,'r')
    print("sem passar pelo primeiro filtro")
    filtrohan2 = filtro_han(df['foto'],10,'r')

    acerto(df,filtrohan)
    
def probabilidade_foto(nome):
    df = todos_dados()
    df=df[df['foto']==nome]
    print(df)
    dados_padronizados(df,nome)
    
def dados_padronizados(df,nome):
    
    dentro = df[df['tempo']=='0s']
    fora = df[df['tempo']=='30s']
    
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
    #dados_padra(rgb, hsv, hls, nome, tempo )
    print(fora)
    print(dentro)



def filtro_individual(df_padr,df_full):
    
    
    df_padr1 = df_padr[df_padr['tempo']=='0s']
    
    if(int(df_padr1['s1'])>=40):
        print("calcular se é vitiligo")
    else:
        
    
        if(int(df_full['r'])>=10):
            print("calcular se é hanseniase")
        else:
            print("calcular se é normal")