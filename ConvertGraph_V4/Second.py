import os

FilePath = 'C:/Users/cheelaml/Downloads/Gandhi_Request/FilePath.txt'

my_file = open(FilePath)

filepath_contents = my_file.readlines()

#####################################
# Import FilePath from FilePath.txt #
#####################################
count = 0
for line in filepath_contents:
    if 'ExportSorting' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportSorting = line
        count += 1
        break
    else:
        count += 1

count = 0
for line in filepath_contents:
    if 'ExportFilePath' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportFilePath = line
        count += 1
        break
    else:
        count += 1
############################
# End of Import File Path  #
############################

my_file = open(ExportSorting)
log_contents = my_file.readlines()

# create file
f = open(ExportFilePath,'w')

# find the range of the file
Current = 0.0
RangeCount = 0

for line in log_contents:
    while '\n' in line:
        line = line.replace('\n','')
    if (str(Current) + ',') not in line:
        Current = (line.partition(',')[0])
        # print(Current)
        f.write('Next\n')
        f.write(line)
        f.write('\n')
        # print(line)
        RangeCount += 1
    else:
        # print(line)
        f.write(line)
        f.write('\n')


