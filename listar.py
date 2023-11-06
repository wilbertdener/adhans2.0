import os

def listardiretorio(pasta):

    #caminho = r'fotos'
    lista = os.listdir(pasta)
    extensao_imagens = [".png", ".bmp", ".dib",  ".jpeg", ".jpg", ".jp2",  ".webp", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".pfm", ".sr",".ras", ".tiff",".tif" , ".exr ", ".hdr",".pic"]

    lista_imagens = []

    for li in lista:
        for ex in extensao_imagens:
            if (li[len(li) - len(ex):] == ex):
                lista_imagens.append(li)

    return lista_imagens



