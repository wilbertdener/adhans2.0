import cv2

def tamanho(local):
    imgdesenho = cv2.imread(local)
    if (imgdesenho.shape[0] > imgdesenho.shape[1]):
        imgdesenho = cv2.resize(imgdesenho, (760, 1100))#(380, 550))#dobrar tamanho
    else:
        imgdesenho = cv2.resize(imgdesenho, (1100, 760))#(550, 380))#dobrar tamanho

    return imgdesenho

def convertponto(local,ponto):
    imgdesenho = cv2.imread(local)

    if (imgdesenho.shape[0] > imgdesenho.shape[1]):
        #(380, 550)

        ponto1 = int((ponto[0] * imgdesenho.shape[1]) / 760)
        ponto2 = int((ponto[1] * imgdesenho.shape[0]) / 1100)
    else:
        # (550, 380)

        ponto1 = int((ponto[0] * imgdesenho.shape[1])/1100)
        ponto2 = int((ponto[1] * imgdesenho.shape[0])/760)

        #ponto1 = int((ponto[0] * 550) / imgdesenho.shape[1])
        #ponto2 = int((ponto[1] * 3800) / imgdesenho.shape[0])


    return (ponto1,ponto2)


def diferenca(local):
    img = cv2.imread(local)


    if (img.shape[0] > img.shape[1]):
        #(380, 550)]
        razao = img.shape[0]/1100

    else:
        # (550, 380)
        razao = img.shape[1] / 1100



    return int(razao)
