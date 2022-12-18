import os

FilePath = 'C:/Users/cheelaml/Downloads/Gandhi_Request/FilePath.txt'

my_file = open(FilePath)

filepath_contents = my_file.readlines()

#####################################
# Import FilePath from FilePath.txt #
#####################################
count = 0
for line in filepath_contents:
    if 'LogFilePath' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        LogFilePath = line
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

count = 0
for line in filepath_contents:
    if 'CurrentSlot' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        CurrentSlot = line
        count += 1
        break
    else:
        count += 1

count = 0
for line in filepath_contents:
    if 'CurrentType' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        CurrentType = str(line)
        count += 1
        break
    else:
        count += 1

count = 0
for line in filepath_contents:
    if 'ExportSorting' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportSorting = str(line)
        count += 1
        break
    else:
        count += 1     
############################
# End of Import File Path  #
############################

# read and distribute them in table form
my_file = open(LogFilePath)
SimplifyLog_contents = my_file.readlines()

count = 0
# Store into array
LogArray = []

CurrentDate = ''

for line in SimplifyLog_contents:
    if 'Ad9914_' in line:
        if 'Sync Cal load failed' in line:
            # print(line)
            count += 1
        elif 'failed to sync to state, gross errors' in line:
            # print(line)
            count += 1
        else:
            DateTime = line.partition('[')[-1]
            DateTime = DateTime.partition(']')[0]
            line = line.partition('Slot ')[-1]
            Slot = line.partition(': ')[0]
            Type = line.partition('Ad9914_')[-1]
            if ' syncing' in Type:
                Type = Type.partition(' syncing')[0]
            elif 'synced to state ' in Type:
                Type = Type.partition('synced to state ')[0]
            while ' ' in Type:
                Type = Type.replace(' ','')
            Y_V = line.partition('state ')[-1]
            TempLog = (Slot + ',' + Type + ',' + Y_V + ',' + DateTime)
            while '\n' in TempLog:
                TempLog = TempLog.replace('\n','')
            LogArray.append(TempLog)
            count += 1
    else:
        count +=1
# create file
f = open(ExportFilePath,'w')

for x in range(len(LogArray)):
    # print(LogArray[x])
    f.write(LogArray[x])
    f.write('\n')

# create file
f = open(ExportSorting,'w')

x= 1.0
z = 0
TempArray = []
for Sorting in range(100):
    count = 1
    for y in range(len(LogArray)):
        if (str(x) + ',') in LogArray[y]:
            if (',' + str(z) + ',') in LogArray[y]:
                # print(LogArray[y])
                TempLine = LogArray[y] + ',' + str(count)
                f.write(TempLine)
                f.write('\n')
                # TempArray.append(LogArray[y])
                count += 1
    x += 1.0

x= 1.0
z = 0
TempArray = []
for Sorting in range(100):
    count = 1
    for y in range(len(LogArray)):
        if (str(x) + ',') in LogArray[y]:
            if (',' + str(z + 1) + ',') in LogArray[y]:
                # print(LogArray[y])
                TempLine = LogArray[y] + ',' + str(count)
                f.write(TempLine)
                f.write('\n')
                # TempArray.append(LogArray[y])
                count += 1
    x += 1.0


