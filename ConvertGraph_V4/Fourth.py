import pandas as pd
import os

FilePath = 'C:/Users/cheelaml/Downloads/Gandhi_Request/FilePath.txt'

my_file = open(FilePath)

filepath_contents = my_file.readlines()

count = 0
for line in filepath_contents:
    if 'ExportCSVFilePath ' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        filepath  = line
        count += 1
        break
    else:
        count += 1

csv_file = []


TempFileArray = (os.listdir(file_path))
for x in range(len(TempFileArray)):
    if 'csv' in TempFileArray[x]:
        csv_file.append(TempFileArray[x])

print(len(csv_file))