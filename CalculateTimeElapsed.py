import os

FilePath = 'C:/Users/cheelaml/OneDrive - Intel Corporation/Desktop/python/FilePath.txt'

my_file = open(FilePath)

filepath_contents = my_file.readlines()

#####################################
# Import FilePath from FilePath.txt #
#####################################

ConsoleLogFile = str(filepath_contents)

ConsoleLogFile = (ConsoleLogFile.partition(" = '")[-1])
ConsoleLogFile = (ConsoleLogFile.partition("'")[0])
while '\n' in ConsoleLogFile:
    ConsoleLogFile = ConsoleLogFile.replace('\n','')
# print(ConsoleLogFile)

my_console = open(ConsoleLogFile)
ConsoleFilePath_Contents = my_console.readlines()

# Store into array
LogArray = []

count = 1
for line in ConsoleFilePath_Contents:
    if "Time Elapsed" in line:
        if "StopOther(): 0s" not in line:
            if 'Tester Initialization:' in line:
                time = (str(line).partition('Tester Initialization:')[-1])
            else:
                time = (str(line).partition('Time Elapsed:')[-1])
            time = time.partition('s')[0]

            while '\n' in time:
                time = time.replace('\n','')
            while ' ' in time:
                time = time.replace(' ','')
            LogArray.append(time)
            count+=1

print("Total Count:" + str(count))
print("Array Size:" + str(len(LogArray)))

SubTotal = 0
for x in range(len(LogArray)):
    print("Current Array Size:" + str(len(LogArray)))
    if len(LogArray) >= 1:
        Total = float(LogArray[0]) + float(LogArray[1])
        SubTotal = SubTotal + Total
        print(SubTotal)
        print("Delete 0 and 1")
        for y in range(2):
            del LogArray[0]
        # print(LogArray[0])
        # break
    elif (len(LogArray)) == 0:
        print("Stopping For Loop, End Program")
        break

print('\nTotal Running Time(in Seconds):' + str(SubTotal) + " In Minutes: " + (str(SubTotal/60)), ' In Hours: ' + str((SubTotal/60)/60))

