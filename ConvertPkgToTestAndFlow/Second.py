#####################################################
# Second Step --- Convert .test into final version  #
#####################################################

import os
myfile = 'C:/Users/cheelaml/OneDrive - Intel Corporation/Desktop/python/ConvertPkgToTestAndFlow/AdditionalFile/FilePath.txt'

my_file = open(myfile)
filepath_contents = my_file.readlines()

count = 0
for line in filepath_contents:
    if 'ExportTest' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportTest = line
        count += 1
        break
    else:
        count += 1
count = 0
for line in filepath_contents:
    if 'ExportFlow' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        ExportFlow = line
        count += 1
        break
    else:
        count += 1
count = 0
for line in filepath_contents:
    if 'FinalConvertTest' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        FinalConvertTest = line
        break
    else:
        count += 1


print(ExportTest)
print(ExportFlow)

my_file = open(ExportTest)
test_contents = my_file.readlines()

my_file = open(ExportFlow)
flow_contents = my_file.readlines()

# Store .flow all mainflow test name
flowArray = []

# Store .test all mainflow test name
testArray = []

count = 0
for line in flow_contents:
    if 'CalDiagDummyTestClass' in line:
        line = line.partition('Class ')[-1]
        # print(line)
        flowArray.append(line)
        count += 1
    else:
        count += 1

count = 0
for line in test_contents:
    if 'Test CalDiagDummyTestClass' in line:
        line = line.partition('Class ')[-1]
        # print(line,count + 1)
        line = line + ' Count:' + str(count)
        testArray.append(line)
        count += 1
    else:
        count += 1

# Summarize the final test name into array
FinalArray = []
for x in range(len(testArray)):
    for y in range(len(flowArray)):
        if str(testArray[x]).partition(' Count')[0] == str(flowArray[y]):
            # print(testArray[x], flowArray[y])
            FinalArray.append(testArray[x])
            break

# create mtpl file with otpl format
f = open(FinalConvertTest, "w")

count = 0
for Copy in test_contents:
    if 'Test ' not in Copy:
        f.write(Copy)
    else:
        break 

for FinalConvert in range(len(FinalArray)):
    # find the line count
    if (len(FinalArray)) > 0:
        EndCount = (str(FinalArray[0]).partition(' Count:')[-1])
    count = 0
    for Copy in test_contents:
        if count >= int(EndCount):
            if '}' not in Copy:
                f.write(Copy)
                count += 1
            else:
                f.write(Copy)
                break
        else:
            count += 1

    # finish the FinalArray, Delete the top one
    del FinalArray[0]