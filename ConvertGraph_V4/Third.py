import os

FilePath = 'C:/Users/cheelaml/Downloads/Gandhi_Request/FilePath.txt'

my_file = open(FilePath)

filepath_contents = my_file.readlines()

#####################################
# Import FilePath from FilePath.txt #
#####################################
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
    if 'ExportCSVFilePath ' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportCSVFilePath = line
        count += 1
        break
    else:
        count += 1
############################
# End of Import File Path  #
############################

my_file = open(ExportFilePath)
log_contents = my_file.readlines()

# find the range of the file
count = 0
RangeCount = 0
for line in log_contents:
    if 'Next' in line:
        # print(line)
        RangeCount += 1
        count += 1
    else:
        count += 1


count = 0
Have = 0
LogArray = []
EndCount = 0

for Converting in range(RangeCount):
# for Converting in range(4):
    FileNo = Converting + 1
    # create file
    file = ExportCSVFilePath + 'File' + str(FileNo) +'.csv'
    f = open(file,'w')
    f.write('Slot,Type,Y-Axis,Date and Time,X-Axis\n')
    for line in log_contents:
        if count >= EndCount:
            if Have > 0:
                if 'Next' in line:
                    # print('Slot,Type,Old_A,Old_B,New_A,New_B,X_values\n')
                    # f.write('Slot,Type,Old_A,Old_B,New_A,New_B,X_values\n')
                    count += 1
                    break
                else:
                    print(line, Have)
                    f.write(line)
                    Have += 1
                    count += 1
            else:
                if 'Next' in line:
                    # print('Slot,Type,Old_A,Old_B,New_A,New_B,X_values\n')
                    # f.write('Slot,Type,Old_A,Old_B,New_A,New_B,X_values\n')
                    count += 1
                else:
                    print(line, Have)
                    f.write(line)
                    Have += 1
                    count += 1
        else:
            count += 1
    EndCount = count
    count = 0
    print('Endcount = ', EndCount)
