import os

#Рабочая директория
path = "/Users/instajons/Desktop/mapreduce/txt/format"

#Получаем массив нужных директорий
file_list = os.listdir(path)
file_list = [x for x in file_list if x[0:4] == "user"]
file_list = sorted(file_list)

#MapReduce для каждого файла, сохраняем результат в ту же папку
for file in file_list:
    command = "/Users/instajons/hadoop/hadoop-3.3.0/bin/hdfs dfs -put /Users/instajons/Desktop/mapreduce/txt/format/" + file + " /" + file
    os.system(command)
    command = "/Users/instajons/hadoop/hadoop-3.3.0/bin/yarn jar /Users/instajons/hadoop/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -input /" + file + " -output /" + file + "exp" + " -file /Users/instajons/hadoop/proj/mapper.py -file /Users/instajons/hadoop/proj/reducer.py -mapper \"python3 mapper.py\" -reducer \"python3 reducer.py\""
    os.system(command)
    command = "/Users/instajons/hadoop/hadoop-3.3.0/bin/hdfs dfs -copyToLocal /" + file + "exp" +  " /Users/instajons/Desktop/mapreduce/txt/format/" + file
    os.system(command)
