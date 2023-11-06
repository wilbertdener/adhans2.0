


fluxo
main -> definirois[selecionar]
    definirois -> rois[], criar_todos_quadrados[], criar_planilha_excel[excel]
        rois-> tamanho[tamanho]
        criar_todos_quadrados->diferenca[]
        criar_planilha_excel->comparaind[]




#razao so funciona para o tamanha de foto utilizado - somente para imagens menores que 1100x760 - uma camera de 8mp -> 3266x2449


# tamanho dos rois varia de acordo com o tamanho da imagem,
# padronizei com tamanho (760, 1100) nesse tamanho o roi é definido 10x10
# razão = tamanho_original/1100
# 10*razao
#excel -> comparaind