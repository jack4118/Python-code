# To check how many stpl file in here

import os

filepath = "C:\\Users\\cheelaml\\OneDrive - Intel Corporation\\Desktop\\OTPL_Test_List\\Hvdps\\Hvildps.stpl"
Filepath = str(format(filepath))
my_file = open(Filepath)

STPLFile_contents = my_file.readlines()

# Print out Full File Path
count = 0
count2 = 0
Name = []
Name2 = []
for line in STPLFile_contents:
    if 'mtpl' in line:
        while '\n' in line:
            line = line.replace('\n', '')
        while ';' in line:
            line = line.replace(';', '')
        while ' ' in line:
            line = line.replace(' ', '')
        Name.append(line)
        print(line)
        count += 1

print('\n################################')
#Summarize File
for line in range(len(Name)):
    if '\\' in str(Name[line]):
        List = str(Name[line]).partition('\\')[-1]
    elif 'Final' in str(Name[line]):
        List = str(Name[line])
        while ' ' in List:
            List = List.replace(' ','')

    for line in range(2):
        if '\\' in List:
            List = List.partition('\\')[-1]
        else:
            break
    if '.mtpl' in List:
        List = List.replace('.mtpl', '')
    print(List)
    Name2.append(List)

print('\nTotal STPL = ' + str(count))

# List out the test

filepath = 'C:\\Users\\cheelaml\\OneDrive - Intel Corporation\\Desktop\\OTPL_Test_List\\Hvdps\\FilePath.txt'
Filepath = str(format(filepath))
my_file = open(Filepath)

ModulesFile_contents = my_file.readlines()

for line in ModulesFile_contents:
    if 'Module = ' in line:
        line = line.partition("Module = ")[-1]
        while '\n' in line:
            line = line.replace('\n','')
        Modules = (line)
    elif 'Test = ' in line:
        line = line.partition("Test = ")[-1]
        while '\n' in line:
            line = line.replace('\n','')
        Test = (line)

for i in range(len(Name2)):
    if 'Final' in Name2[i]:
        Name2[i] = str(Name2[i]).partition('Final')[-1]
        filepath = 'C:\\Users\\cheelaml\\OneDrive - Intel Corporation\\Desktop\\OTPL_Test_List\\Hvdps\\Recipes\\' + Name2[i] + '.mtpl'
    else:
        filepath = ('C:\\Users\\cheelaml\\OneDrive - Intel Corporation\\Desktop\\OTPL_Test_List\\Hvdps\\'+ Modules + '\\' + Name2[i] +'\\' + Name2[i] + '.mtpl' )
    # For RCTC3 issue update
    if 'FuncFeaturetTest' in Name2[i]:
        filepath = ('C:\\Users\\cheelaml\\OneDrive - Intel Corporation\\Desktop\\OTPL_Test_List\\Hvdps\\'+ Modules + '\\Rc3FFTest\\' + Name2[i] + '.mtpl' )
    Filepath = str(format(filepath))
    my_file = open(Filepath)
    Tests = 0
    print('\n#################\nAll Test from ' + Name2[i] + '.mtpl' + ':')
    ModulesFile_contents = my_file.readlines()
    count = 0
    for line in ModulesFile_contents:
        if 'Test ' in line:
            if '#' not in line:
                if ' = ' not in line:
                    while '\n' in line:
                        line = line.replace('\n','')
                    print(line)
                    count += 1
                    Tests +=1
        else:
            count += 1
    print('\nTotal Tests: ' + str(Tests))