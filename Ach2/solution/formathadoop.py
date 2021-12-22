import os

#Рабочая директория
path = "/Users/instajons/Desktop/mapreduce/txt/format/"

#Получаем массив нужных директорий
file_list = os.listdir(path)
file_list = [x for x in file_list if x[0:4] == "user"]
file_list = sorted(file_list)

#Форматируем результаты hadoop
pathroot = "/Users/instajons/Desktop/mapreduce/txt/"
for folder in file_list:
    path = "/Users/instajons/Desktop/mapreduce/txt/format/" + folder + "/" + folder + "exp"

    #Удаляем битые последние строки в файле
    with open(path + "/part-00000", 'rb+') as filehandle:
        filehandle.seek(-30, os.SEEK_END)
        filehandle.truncate()

    data = open(path + "/part-00000", 'r')
    text = data.read()

    #Удаляем символы null
    text = text.replace('\0', '')
    name = folder + "format" + ".txt"
    txt = open(pathroot + name, "w", encoding='utf-8')

    #Сохраняем результат
    txt.write('\ufeff')
    txt.write(text)
