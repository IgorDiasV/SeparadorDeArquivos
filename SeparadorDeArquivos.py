import os
import shutil
arquivos=os.listdir() #  pega o nome de todos os arquivos
extensoes=[".pdf",".png",".jpeg",".csv",".mp3",".ods",".rar",".zip",".vhd"]
def moverArquivo(nome,ext):
    if(os.path.isfile("./"+ext+"/"+nome)):
        print("arquivo repetido")
        return
    if(os.path.isdir(ext)):
        shutil.move(nome,"./"+ext)
    else:
        os.mkdir(ext)
        shutil.move(nome, "./" + ext)

for nome in arquivos:
    for ext in extensoes:
        if(nome.endswith(ext)):
            moverArquivo(nome,ext[1:])
            break

