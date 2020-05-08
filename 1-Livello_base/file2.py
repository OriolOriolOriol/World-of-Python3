import shutil,os

#shutil.copy("C:\\Users\\claud\\Desktop\\Python3.6\\primo.txt","C:\\Users\\claud\\Desktop")#copio il file
#shutil.move("C:\\Users\\claud\\Desktop\\Python3.6\\secondo.txt","C:\\Users\\claud\\Desktop")#muovo il file
os.unlink("C:\\Users\\claud\\Desktop\\Python3.6\\primo.txt")#cancellazione permanenete di un file
os.rename("C:\\Users\\claud\\Desktop\\secondo.txt","C:\\Users\\claud\\Desktop\\Python3.6\\file_rinominato.txt")#rinominazione di un file