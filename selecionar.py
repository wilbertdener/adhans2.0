from listar import *
import os
import cv2
from tamanho import *
from excel import *
import os.path
from openpyxl import *
from contraste import *


#arquivos = listardiretorio()
count = 0
vet = []

def rois(texto, local,pasta):
    
    foto1 = tamanho(pasta+"/"+local)

    def draw_lines(event, x, y, flags, param):
        ix, iy, sx, sy = -1, -1, -1, -1
        global vet
        global count
        if (count == 0):
            cor = (121, 39, 165)
        elif (count == 1):
            cor = (139, 0, 139)
        elif (count == 2):
            cor = (161, 64, 158)
        else:
            cor = (0, 0, 0)

        # if the left mouse button was clicked, record the starting
        if event == cv2.EVENT_LBUTTONDOWN:

            # draw circle of 2px
            # cv2.circle(img, (x, y), 3, (0, 0, 127), -1)
            # coordenada centrais(x,y) e raio(3)

            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), cor, 1)
            # canto superior esquerdo e do canto inferior direito

            if (count < 3):
                vet.append((x, y));
            count = count + 1



        elif event == cv2.EVENT_LBUTTONDBLCLK:
            ix, iy = -1, -1  # reset ix and iy
            if flags == 33:  # if alt key is pressed, create line between start and end points to create polygon
                cv2.line(img, (x, y), (sx, sy), (0, 0, 127), 2, cv2.LINE_AA)

    

    img = foto1.copy()

    cv2.namedWindow(texto +" - "+ local )
    cv2.setMouseCallback(texto +" - "+ local, draw_lines)

    
    while (1):
        cv2.imshow(texto +" - "+ local, img)
        teste = controller(img, 172, 190)
        cv2.imshow("contraste "+texto +" - "+ local, teste)
        if cv2.waitKey(20) & 0xFF == 27:
            break
        if count == 4:
            break

    cv2.destroyAllWindows()




def desenho_todos_quadrados(vet, nome,pasta,time):

    antes =[]
    depois = []
    razao = diferenca(pasta+"/"+nome)
    #print("desenho : ",razao)
    for v in vet[0]:
        antes.append(convertponto(pasta+"/"+nome,v))
    for v in vet[1]:
        depois.append(convertponto(pasta+"/" + nome, v))

    imgdesenho = cv2.imread(pasta+"/" + nome)
    imgcut = imgdesenho.copy()
    #dentro a area
    imgdesenho = cv2.rectangle(imgdesenho, (antes[0][0] - (5*razao), antes[0][1] - (5*razao)),
                               (antes[0][0] + (5*razao), antes[0][1] + (5*razao)),
                               (255, 255, 255), 10)
    
    roidentro1 = imgcut[ (antes[0][1] - (5*razao)):(antes[0][1] + (5*razao)),(antes[0][0] - (5*razao)):(antes[0][0] + (5*razao))] 
    cv2.imwrite("roi dentro/"+nome[:len(nome)-4]+" "+time+"roi1.jpg", roidentro1)
    
    imgdesenho = cv2.rectangle(imgdesenho, (antes[1][0] - (5*razao), antes[1][1] - (5*razao)),
                               (antes[1][0] + (5*razao), antes[1][1] + (5*razao)),
                               (255, 255, 255), 10)
    
    roidentro2 = imgcut[ (antes[1][1] - (5*razao)):(antes[1][1] + (5*razao)),(antes[1][0] - (5*razao)):(antes[1][0] + (5*razao))] 
    cv2.imwrite("roi dentro/"+nome[:len(nome)-4]+" "+time+"roi2.jpg", roidentro2)
    
    imgdesenho = cv2.rectangle(imgdesenho, (antes[2][0] - (5*razao), antes[2][1] - (5*razao)),
                               (antes[2][0] + (5*razao), antes[2][1] + (5*razao)),
                               (255, 255, 255), 10)
    
    roidentro3 = imgcut[ (antes[2][1] - (5*razao)):(antes[2][1] + (5*razao)) , (antes[2][0] - (5*razao)):(antes[2][0] + (5*razao))] 
    cv2.imwrite("roi dentro/"+nome[:len(nome)-4]+" "+time+"roi3.jpg", roidentro3)
    
    # distante a area
    imgdesenho = cv2.rectangle(imgdesenho, (depois[0][0] - (5*razao), depois[0][1] - (5*razao)),
                               (depois[0][0] + (5*razao), depois[0][1] + (5*razao)),
                               (121, 39, 165), 10)
    
    roifora1 = imgcut[ (depois[0][1] - (5*razao)):(depois[0][1] + (5*razao)) , (depois[0][0] - (5*razao)):(depois[0][0] + (5*razao))] 
    cv2.imwrite("roi fora/"+nome[:len(nome)-4]+" "+time+"roi1.jpg", roifora1)
    
    imgdesenho = cv2.rectangle(imgdesenho, (depois[1][0] - (5*razao), depois[1][1] - (5*razao)),
                               (depois[1][0] + (5*razao), depois[1][1] + (5*razao)),
                               (121, 39, 165), 10)
    
    roifora2 = imgcut[ (depois[1][1] - (5*razao)):(depois[1][1] + (5*razao)) , (depois[1][0] - (5*razao)):(depois[1][0] + (5*razao))] 
    cv2.imwrite("roi fora/"+nome[:len(nome)-4]+" "+time+"roi2.jpg", roifora2)
    
    imgdesenho = cv2.rectangle(imgdesenho, (depois[2][0] - (5*razao), depois[2][1] - (5*razao)),
                               (depois[2][0] + (5*razao), depois[2][1] + (5*razao)),
                               (121, 39, 165), 10)
    
    roifora3 = imgcut[ (depois[2][1] - (5*razao)):(depois[2][1] + (5*razao)) , (depois[2][0] - (5*razao)):(depois[2][0] + (5*razao))] 
    cv2.imwrite("roi fora/"+nome[:len(nome)-4]+" "+time+"roi3.jpg", roifora3)
    
    
    
    
                      
    

    if os.path.isdir(pasta+"/detalhado/"):  # vemos de este diretorio ja existe
        cv2.imwrite(pasta+"/detalhado/" + nome, imgdesenho)

    else:
        os.mkdir(pasta+"/detalhado/")  # aqui criamos a pasta caso nao exista
        cv2.imwrite(pasta+"/detalhado/" + nome, imgdesenho)
        #wb = load_workbook(filename="resultado.xlsx")
        #wb.save(filename=pasta + "/detalhado/resultado.xlsx")

    #cv2.imwrite(pasta+"/detalhado/" + nome, imgdesenho)
    return (antes,depois)


# filename not an image file
def definirois(pasta,arquivos):
    #arquivos = listardiretorio(pasta)
    #vettempo = ["0s","5s","10s","20s","30s","60s"]
    conttempo = 0

    for arq in arquivos:

        global vet
        global count
        vetdois = []
        vet = []
        count = 0

        rois("Selecione 3 rois dentro da lesão e proximos a area do teste", arq,pasta)
        vetdois.append(vet)

        vet = []
        count = 0

        rois("Selecione 3 rois fora da lesão e proximos a area do teste", arq,pasta)
        vetdois.append(vet)

        
        if(conttempo%2==0):
            pontos = desenho_todos_quadrados(vetdois, arq, pasta,"0s")
        else:
            pontos = desenho_todos_quadrados(vetdois, arq, pasta,"30s")

        #criar_planilha_excel(pontos, pasta+"/"+arq, diferenca(pasta+"/"+arq),pasta,plan,vettempo[conttempo%6])
        conttempo =conttempo +1




