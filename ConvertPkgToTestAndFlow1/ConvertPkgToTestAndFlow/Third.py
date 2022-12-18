############################################################
# Third Step --- Remove the symbol that will cause errors  #
############################################################
import os

myfile = 'C:/Users/cheelaml/OneDrive - Intel Corporation/Desktop/python/ConvertPkgToTestAndFlow/AdditionalFile/FilePath.txt'

my_file = open(myfile)
filepath_contents = my_file.readlines()

count = 0
for line in filepath_contents:
    if 'FinalConvertTest' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        FinalConvertTest = line
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

print(FinalConvertTest)
print(ExportFlow)

my_file = open(FinalConvertTest)
HPCC_contents = my_file.readlines()

f = open(FinalConvertTest, "w")

count = 0
for line in HPCC_contents:
    if '$' in line:
        line = line.replace('$','')
        f.write(line)
        count += 1
    elif '(' in line:
        line = line.replace('(','_')
        if ')' in line:
            line = line.replace(')','')
        if '.' in line:
            line = line.replace('.','p')
        f.write(line)
        count += 1
    elif 'Test ' in line:
        if '.' in line:
            if '(' in line:
                line = line.replace('(','_')
                if ')' in line:
                    line = line.replace(')','')
            line = line.replace('.','p')
            # print(line, count + 1)
            f.write(line)
            count += 1 
        elif '-' in line:
            line = line.replace('-','_')
            f.write(line)
            count += 1
        elif '(' in line:
            line = line.replace('(','_')
            if ')' in line:
                line = line.replace(')','')
            f.write(line)
            count += 1
        else:
            f.write(line)
            count += 1
    elif 'FlowItem ' in line:
        if '.' in line:
            if '(' in line:
                line = line.replace('(','_')
                if ')' in line:
                    line = line.replace(')','')
            line = line.replace('.','_')
            # print(line, count + 1)
            f.write(line)
            count += 1 
        elif '-' in line:
            line = line.replace('-','_')
            f.write(line)
            count += 1
        else:
            f.write(line)
            count += 1  
    else:
        f.write(line)
        count += 1

# For Flow Item Part (.flow)
my_file = open(ExportFlow)
HPCC_contents = my_file.readlines()

f = open(ExportFlow, "w")

count = 0
for line in HPCC_contents:
    if 'GoTo' in line:
        TempLine = line.partition('GoTo ')[-1]
        if '-' in TempLine:
            TempLine = TempLine.replace('-','_')
            # print(TempLine)
            CurrentLine = line.split()[:2]
            CurrentLine = " ".join(CurrentLine)
            # print('    ' + CurrentLine + ' ' + TempLine)
            f.write('    ' + CurrentLine + ' ' + TempLine)
        elif '(' in line:
            # print(line)
            line = line.replace('(','_')
            line = line.replace(')','')
            f.write(line)
        elif '.' in line:
            line = line.replace('.','p')
            f.write(line)
        else:
            f.write(line)
    elif '(' in line:
        # print(line)
        line = line.replace('(','_')
        line = line.replace(')','')
        f.write(line)
    else:
        f.write(line)