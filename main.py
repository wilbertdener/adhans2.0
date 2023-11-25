from listar import *
import os
import cv2
from tamanho import *
from excel import *
from selecionar import *
from rois import *
from filtros import *



    #definirois('pasta',['img 0s', 'img 30s'])
definirois('imagens',['hans1.jpg','hans2.jpg'])
    #salva_no_bd(nome1= None ,nome2=None)
salva_no_bd('hans1','hans2')
df_padr = get_dados_pad_by_foto('hans')
df_full = get_dados_full_foto('hans')
filtro_individual(df_padr,df_full)
#probabilidade_foto('hans')
