# from msilib.schema import File
import os
from re import X
# from pydoc import doc
# from re import L
# from tkinter import E
# from webbrowser import Chrome
# Start of the Test Function

def TestStart(Name):
    f.write("\n\n")
    f.write("Test ")
    testfile = str(FileName[CountFile]).replace('.xml','')
    f.write(testfile)
    f.write(' ')
    f.write(Name)
    f.write("\n{")
# End of the Test Function
def TestEnd():
    f.write("\n}")

# Test Function
def TestContent(Parameter, value):
    f.write('\n\t')
    f.write(Parameter)
    f.write(' = "')
    f.write(value)
    f.write('";')

def FlowStart1(Name):
    f.write('\n\n')
    f.write('Flow ')
    f.write(Name)
    f.write('\n{')

def FlowStart2(Test):
    f.write('\n\t')
    f.write('FlowItem ')
    f.write(Test)
    f.write('_eos0 ')
    f.write(Test)
    f.write('\n\t\t{')

def FlowEnd2():
    f.write('\n\t\t}')

def MainFlowStart(Num,Name):
    f.write('\n\t')
    f.write('FlowItem MainFlow_Execution1')
    f.write('_P')
    f.write(Num)
    f.write('_eos0 ')
    f.write(Name)
    f.write('\n\t\t{')
    
def FlowContent1(PortNumber):
    f.write('\n\t\t\t')
    f.write('Result ')
    f.write(PortNumber)
    f.write('\n\t\t\t{')

def FlowContent1End(PortNumber):
    f.write('\n\t\t\t\tReturn ')
    f.write(PortNumber)
    f.write(';')
    f.write('\n\t\t\t}')

def FlowContent2(Value):
    f.write('\n\t\t\t\t')
    f.write('Property PassFail')
    f.write(' = "')
    f.write(Value)
    f.write('";')

def MainFlowContent(Num):
    f.write('\n\t\t\t\t')
    f.write('GoTo MainFlow_Execution1_P')
    f.write(Num)
    f.write('_eos0')
    f.write(';')

def MainFlowEnd():
    f.write('\n\t\t\t}')

# Array File Name that contains <FileName> Tag
FileName = []

PreHeader_Path = "C:/DummyTest/PreHeaders/"
for filename in os.listdir(PreHeader_Path):
   with open(os.path.join(PreHeader_Path, filename), 'r') as f:
       text = f.read()
       if '<FileName>' in text:
           FileName.append(filename)

# Find bdefs and usrv file
other_file = []

file_path = 'C:/DummyTest'
TempFileArray = (os.listdir(file_path))
for x in range(len(TempFileArray)):
    if 'bdefs' in TempFileArray[x]:
        other_file.append(TempFileArray[x])
    elif 'usrv' in TempFileArray[x]:
        other_file.append(TempFileArray[x])



my_file = open("C:/DummyTest/dummy.pkg")
dummy_contents = my_file.readlines()

count = 0

# Get Version Number
for line in dummy_contents:
    if "<?xml version=" in line:
        break
    else:
        count += 1

d1 = '<?xml version="'
d2 = '"?>'
ver = line.replace(d1, "")
ver = ver.replace(d2, "")
if "\n" in ver:
    ver = ver.replace("\n", "")

# create mtpl file with otpl format
f = open("C:/DummyTest/dummyTP_base.mtpl", "w")
# write in the version
f.write("Version ")
f.write(ver)
f.write(";\n")

# ProgramStyle
f.write("ProgramStyle = Modular;")


# TestPlan
count = 0
d1 = '<device name="'
for line in dummy_contents:
    if d1 in line:
        line = line.partition('" ')[0]
        line = line.replace(d1,'')
        while ' ' in line:
            line = line.replace(' ','')
        TestPlan = line.replace('\n','')
        break
    else:
        count += 1.

f.write("\n\nTestPlan ")
f.write(TestPlan)
f.write(';')

# Import
# Pre-headers Path

f.write('\n')
# import All the xml
for x in range(len(FileName)):
    f.write("\nImport ")
    f.write(FileName[x])
    f.write(';')

for x in range(len(other_file)):
    f.write("\nImport ")
    f.write(other_file[x])
    f.write(';')

CountFileTests = []
for CountFile in range(len(FileName)):
    xml = PreHeader_Path + FileName[CountFile]
    xml_file = open(xml)
    xml_contents = xml_file.readlines()

    if CountFile == 0:
        # Array Lists
        Test = [] # record the title of the DummyTestClass
        TestNumber = [] # record the number for all the test in dummy.pkg
        ParameterArray = [] # record the the variable name
        ChoiceArray = [] # value of the testoperation
        ParamValueArray = [] # record the value of the variable
        FlowItem = []

        count = 0
        testCount = 0
        for line in dummy_contents:
            if 'test name' in line:
                testCount += 1
                # line = line.partition('name="')[-1]
                line = line.partition('" ')[0]
                while '\n' in line:
                    line = line.replace('\n','')
                while ' ' in line:
                    line = line.replace(' ','')
                line = line.replace('<testname',str(testCount))
                # print(line)
                Test.append(line)
                count += 1
            else:
                count += 1
        # Test.sort(reverse = True)

        for x in range(len(Test)):
            count = 0
            for line in dummy_contents:
                if (str(Test[x]).partition('="')[-1]) in line:
                    line = line.partition('number')[-1]
                    line = line.partition('" ')[0]
                    while '\n' in line:
                        line = line.replace('\n','')
                    while ' ' in line:
                        line = line.replace(' ','')
                    line = line.replace('="',str(x+1)+'=')
                    TestNumber.append(line)
                    # print(line,' line:',count + 1)
                    count += 1
                    break
                else:
                    count += 1

            Dummy_Count = count
            count2 = 0
            # TestNumber.sort(reverse = True)
            for line2 in dummy_contents:
                if count2 >= Dummy_Count:
                    if 'value="' in line2:
                        line2 = line2.partition('<param ')[-1]
                        line2 = line2.replace('name',(str(Test[x]).partition('="')[-1]))
                        line2 = line2.replace('"','')
                        line2 = line2.replace('/>','')
                        # print(line2)
                        ParamValueArray.append(line2)
                        count2 += 1
                    else:
                        count2 += 1
                        break
                else:
                    count2 += 1

        
        count = 0

        d1 = '<Parameter  name="'
        d2 = '<Parameter name="'
        d3 = '<Choice>'

        for line in xml_contents:
            if d1 in line:
                line = line.partition('" ')[0]
                line = line.replace(d1,'')
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                ParameterArray.append(line)
                count += 1
            elif d2 in line:
                line = line.partition('" ')[0]
                line = line.replace(d2,'')
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                ParameterArray.append(line)
                count += 1
            
            elif d3 in line:
                line = line.partition('</Choice>')[0]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                # print(line)
                ChoiceArray.append(line)

        count = 0
        TempParamValue = 0
        ChoiceArrayCount = len(ChoiceArray)
        # for x in range(len(TestNumber)):
        #     print(TestNumber[x])
        # for x in range(len(Test)):
        #     print(Test[x])
        # for x in range(len(ChoiceArray)):
        #     print(ChoiceArray[x])
        
        ChoiceArray2 = []
        for x in range(len(TestNumber)):
            for y in range(len(ChoiceArray)):
                if (str(TestNumber[x]).partition('=')[-1]).casefold() == (str(ChoiceArray[y]).partition('>')[-1]).casefold():
                    line = (ChoiceArray[y])
                    line = str(line).replace('<Choice',str(TestNumber[x]).partition('=')[0])
                    line = str(line).replace('>','="')
                    ChoiceArray2.append(line)
                    
        for x in range(len(ChoiceArray2)):
            print(ChoiceArray2[x])
        TempArray = []
        for x in range(len(ChoiceArray2) + 1):
            y = len(ChoiceArray2) - 1
            if str(x) in str(ChoiceArray2[y]).partition('="')[0]:
                # print(x)
                ChoiceArray2[y] = (str(ChoiceArray2[y]).replace('="','="<Choice>'+ str(x) + '-'))
                TempArray.append(str(ChoiceArray2[y]).partition('="')[-1])
            elif x != 0:
                while(str(x) not in str(ChoiceArray2[y]).partition('="')[0]):
                    y -= 1
                    if str(x) in str(ChoiceArray2[y]).partition('="')[0]:
                        # print(x)
                        ChoiceArray2[y] = (str(ChoiceArray2[y]).replace('="','="<Choice>'+ str(x) + '-'))
                        # print(ChoiceArray[y])
                        TempArray.append(str(ChoiceArray2[y]).partition('="')[-1])
        # TempArray.sort(reverse = True)
        
        # Start of callDiagDummyTestClass
        for x in range(len(Test)):
            TestStartVariable = str(Test[x]).partition('="')[-1]
            FlowItem.append(TestStartVariable)
            # print(TestStartVariable,', ',xml)
            TestStart(TestStartVariable)
            for y in range(len(ParameterArray)):
                if ParameterArray[y] == 'TestOperation':
                    if 'Used' not in TempArray[count]:
                        TempChoice = TempArray[count]
                        TempChoice = str(TempChoice).replace('<Choice>','')
                        TempChoice = TempChoice.partition('-')[-1]
                        TestContent(ParameterArray[y], TempChoice)
                        TempArray[count] = str(TempArray[count]).replace('<Choice>','<ChoiceUsed>')
                        count += 1

                elif (str(Test[x]).partition('="')[-1]) in ParamValueArray[TempParamValue]: # if Add in Add=Number2 value=1.0 (True)
                    for z in range(len(ParamValueArray)):
                        if ParameterArray[y] in ParamValueArray[z]:
                            if TestStartVariable in ParamValueArray[z]:
                                TempValue = str(ParamValueArray[z]).partition('value=')[-1]
                                while '\n' in TempValue:
                                    TempValue = TempValue.replace('\n','')
                                while ' ' in TempValue:
                                    TempValue = TempValue.replace(' ','')
                                TestContent(ParameterArray[y],TempValue)
                                TempParamValue += 1
                else:
                    TempParamValue += 1
            TestEnd()
        # End of callDiagDummyTestClass
        # for x in range(len(ParamValueArray)):
        #     print(ParamValueArray[x])
        
    # Start of CallDiagInit
    elif CountFile == 1:
        CountFileTests.append('Basic_Init_Execution')
        TestStart('Basic_Init_Execution')
        # Array Lists
        Test = [] # record the title of the DummyTestClass
        ParameterArray = [] # record the the variable name
        ChoiceArray = [] # value of the testoperation
        ParamValueArray = [] # record the value of the variable

        count = 0
        Entry = 0
        for line in xml_contents:
            if 'Parameter name="' in line:
                line = line.partition('="')[-1]
                line = line.partition('" ')[0]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                ParameterArray.append(line)
                count += 1
            elif 'Default' in line:
                line = line.partition('>')[-1]
                line = line.partition('</')[0]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                ParamValueArray.append(line)
                count += 1
            else:
                count += 1
        TestContent(ParameterArray[Entry],ParamValueArray[Entry])
        Entry += 1

        count = 0
        for line in xml_contents:
            if 'FileName' in line:
                line = line.partition('>')[-1]
                line = line.partition('</')[0]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                xml = PreHeader_Path + line
                xml_file = open(xml)
                xml_contents = xml_file.readlines()
                break
            else:
                count += 1
        count = 0
        for line in xml_contents:
            if 'BypassInstance' in line:
                line = line.partition('="')[-1]
                line = line.partition('" ')[0]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                ParameterArray.append(line)
                count += 1
                break
            else:
                count += 1
        TempCount = count
        count = 0
        for line in xml_contents:
            if count >= TempCount:
                if 'Default' in line:
                    line = line.partition('>')[-1]
                    line = line.partition('</')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    ParamValueArray.append(line)
                    count += 1
                    break
                else:
                    count += 1
            else:
                count += 1
        TestContent(ParameterArray[Entry],ParamValueArray[Entry])
        Entry += 1       
        TestEnd()
    # End of CallDiagInit

    # Start of CallDiagLotOperation
    elif CountFile == 2:
        # Array Lists
        Test = [] # record the title of the DummyTestClass
        ParameterArray = [] # record the the variable name
        ChoiceArray = [] # value of the testoperation
        ParamValueArray = [] # record the value of the variable
        OperationMode = []

        count = 0
        Entry = 0
        Entry2 = 0
        ChoiceEntry = 0
        for line in xml_contents:
            if 'select' in line:
                line = line.partition('select ')[-1]
                line = line.partition('">')[0]
                word1 = line.partition(' or ')[0]
                word2 = line.partition(' or ')[-1]
                OperationMode.append(word1)
                OperationMode.append(word2)
            else:
                count += 1

        for x in range(len(OperationMode)):
            CountFileTests.append('Basic_'+OperationMode[x])
            TestStart('Basic_'+OperationMode[x])
            count = 0
            for line in xml_contents:
                if '<Parameter  name="' in line:
                    line = line.partition('="')[-1]
                    line = line.partition('" ')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    ParameterArray.append(line)
                    count += 1
                    break
                else:
                    count += 1
            count = 0
            for line in xml_contents:
                if '<Choice>' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if (len(ChoiceArray)) == 0:
                        ChoiceArray.append(line)
                    elif line not in ChoiceArray:
                        ChoiceArray.append(line)
                    count += 1
                else:
                    count += 1
            
            count = 0
            for line in xml_contents:
                if 'FileName' in line:
                    line = line.partition('>')[-1]
                    line = line.partition('</')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    xml = PreHeader_Path + line
                    xml_file = open(xml)
                    xml_contents = xml_file.readlines()
                    break
                else:
                    count += 1
            
            count = 0
            for line in xml_contents:
                if 'BypassInstance' in line:
                    line = line.partition('="')[-1]
                    line = line.partition('" ')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if line not in ParameterArray:
                        ParameterArray.append(line)
                        # print(line)

                    count += 1
                    break
                else:
                    count += 1
            TempCount = count
            count = 0
            for line in xml_contents:
                Entry = 0
                if count >= TempCount:
                    if 'Default' in line:
                        line = line.partition('>')[-1]
                        line = line.partition('</')[0]
                        while ' 'in line:
                            line = line.replace(' ','')
                        while '\n' in line:
                            line = line.replace('\n','')
                        while '\t' in line:
                            line = line.replace('\t','')
                        if line not in ParamValueArray:
                            ParamValueArray.append(line)
                            # print(line)
                        count += 1
                        break
                    else:
                        count += 1
                else:
                    count += 1
            TestContent(ParameterArray[Entry],ChoiceArray[ChoiceEntry])
            Entry += 1
            TestContent(ParameterArray[Entry],ParamValueArray[Entry2])
            ChoiceEntry += 1
            TestEnd()
            
    elif CountFile == 3:
        # Array Lists
        Test = [] # record the title of the DummyTestClass
        ParameterArray = [] # record the the variable name
        ChoiceArray = [] # value of the testoperation
        ParamValueArray = [] # record the value of the variable
        OperationMode = []

        count = 0
        Entry = 0
        Entry2 = 0
        ChoiceEntry = 0

        for line in xml_contents:
            if 'select' in line:
                line = line.partition('select ')[-1]
                line = line.partition('">')[0]
                word1 = line.partition(' or ')[0]
                word2 = line.partition(' or ')[-1]
                OperationMode.append(word1)
                OperationMode.append(word2)
            else:
                count += 1
        for x in range(len(OperationMode)):
            CountFileTests.append('Basic_'+OperationMode[x])
            TestStart('Basic_'+OperationMode[x])
            count = 0
            for line in xml_contents:
                if '<Parameter  name="' in line:
                    line = line.partition('="')[-1]
                    line = line.partition('" ')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    ParameterArray.append(line)
                    count += 1
                    break
                else:
                    count += 1
            count = 0
            for line in xml_contents:
                if '<Choice>' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if (len(ChoiceArray)) == 0:
                        ChoiceArray.append(line)
                    elif line not in ChoiceArray:
                        ChoiceArray.append(line)
                    count += 1
                else:
                    count += 1
            
            count = 0
            for line in xml_contents:
                if 'FileName' in line:
                    line = line.partition('>')[-1]
                    line = line.partition('</')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    xml = PreHeader_Path + line
                    xml_file = open(xml)
                    xml_contents = xml_file.readlines()
                    break
                else:
                    count += 1
            
            count = 0
            for line in xml_contents:
                if 'BypassInstance' in line:
                    line = line.partition('="')[-1]
                    line = line.partition('" ')[0]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if line not in ParameterArray:
                        ParameterArray.append(line)

                    count += 1
                    break
                else:
                    count += 1
            TempCount = count
            count = 0
            for line in xml_contents:
                Entry = 0
                if count >= TempCount:
                    if 'Default' in line:
                        line = line.partition('>')[-1]
                        line = line.partition('</')[0]
                        while ' 'in line:
                            line = line.replace(' ','')
                        while '\n' in line:
                            line = line.replace('\n','')
                        while '\t' in line:
                            line = line.replace('\t','')
                        if line not in ParamValueArray:
                            ParamValueArray.append(line)
                        count += 1
                        break
                    else:
                        count += 1
                else:
                    count += 1
            TestContent(ParameterArray[Entry],ChoiceArray[ChoiceEntry])
            Entry += 1
            TestContent(ParameterArray[Entry],ParamValueArray[Entry2])
            ChoiceEntry += 1
            TestEnd()
    # End of CallDiagLotOperation
FlowDef = []
# Flow TestPlan
for CountFile in range(len(FileName)):
    xml = PreHeader_Path + FileName[CountFile]
    xml_file = open(xml)
    xml_contents = xml_file.readlines()
    
  
    if CountFile == 0:
        # Array List
        PortNumber = []
        PortNumberValue = []
        
        rangeCount = 0
        for x in range(len(FlowItem)):
            count = 0
            
            for line in xml_contents:
                if 'PortNumber' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    PortNumber.append(line)
                    count += 1
                    rangeCount += 1
                else:
                    count += 1
            count = 0
            for line in xml_contents:
                if 'PortType' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if line == 'Error':
                        line = line.replace('Error','Fail')
                    PortNumberValue.append(line)
                    count += 1
                else:
                    count += 1
        Flow = 'Dummy' + 'Flow'
        FlowStart1(Flow)
        FlowDef.append(Flow)
        for x in range(len(FlowItem)):
            temp = (x)
            MainFlowStart(str(temp + 1),FlowItem[x])

            for y in range(len(FlowItem)):
                FlowContent1(PortNumber[y])
                FlowContent2(PortNumberValue[y])
                if x == 0:
                    if str(PortNumber[y]) == '1':
                        f.write('\n\t\t\t\t')
                        f.write('SetBin SoftBins.b01000000_PASS;')
                if (temp + 2) <= (len(FlowItem)):
                    MainFlowContent(str(temp + 2))
                    MainFlowEnd()
                else:
                    FlowContent1End(PortNumber[y])
            FlowContent1('96')    
            FlowContent2('Bypass')
            if (temp + 2) > 4:
                MainFlowContent(str(temp + 1))
            else:
                MainFlowContent(str(temp + 2))
            MainFlowEnd()
            FlowEnd2()
        TestEnd()
        
    elif CountFile == 1:
        Flow = 'Init_Execute'
        FlowStart1(Flow)
        FlowDef.append(Flow)
        FlowStart2(CountFileTests[0])
        CountFileTests[0] = str(CountFileTests[0]).replace('Basic','Basic_Used')

        # Array List
        PortNumber = []
        PortNumberValue = []

        count = 0
        for line in xml_contents:
            if 'PortNumber' in line:
                line = line.partition('</')[0]
                line = line.partition('>')[-1]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                PortNumber.append(line)
                count += 1
            else:
                count += 1
        count = 0
        for line in xml_contents:
            if 'PortType' in line:
                line = line.partition('</')[0]
                line = line.partition('>')[-1]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                if line == 'Error':
                    line = line.replace('Error','Fail')
                PortNumberValue.append(line)
                count += 1
            else:
                count += 1


        for x in range(len(PortNumber)):
            FlowContent1(PortNumber[x])
            FlowContent2(PortNumberValue[x])
            FlowContent1End(PortNumber[x])
        FlowContent1('96')    
        FlowContent2('Bypass')
        FlowContent1End('96')
        FlowEnd2()
        TestEnd()
    elif CountFile == 2:
        # Array List
        FlowItem = []
        PortNumber = []
        PortNumberValue = []
        OperationMode = []
        ChoiceArray = [] # value of the testoperation

        count = 0
        Entry = 0
        Entry2 = 0
        ChoiceEntry = 0
        for line in xml_contents:
            if 'select' in line:
                line = line.partition('select ')[-1]
                line = line.partition('">')[0]
                word1 = line.partition(' or ')[0]
                word2 = line.partition(' or ')[-1]
                OperationMode.append(word1)
                OperationMode.append(word2)
            else:
                count += 1
        count = 0
        for line in xml_contents:
            if 'PortNumber' in line:
                line = line.partition('</')[0]
                line = line.partition('>')[-1]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                    
                PortNumber.append(line)
                count += 1
            else:
                count += 1

        count = 0
        for line in xml_contents:
            if 'PortType' in line:
                line = line.partition('</')[0]
                line = line.partition('>')[-1]
                while ' 'in line:
                    line = line.replace(' ','')
                while '\n' in line:
                    line = line.replace('\n','')
                while '\t' in line:
                    line = line.replace('\t','')
                if line == 'Error':
                    line = line.replace('Error','Fail')
                PortNumberValue.append(line)
                count += 1
            else:
                count += 1

        for x in range(len(OperationMode)):
            Flow = str(OperationMode[x]) + 'Flow'
            FlowStart1(Flow)
            FlowDef.append(Flow)
            FlowStart2(CountFileTests[x + 1])
            CountFileTests[x + 1] = str(CountFileTests[x + 1]).replace('Basic','Basic_Used')
            
            for y in range(len(PortNumber)):
                FlowContent1(PortNumber[y])
                FlowContent2(PortNumberValue[y])
                FlowContent1End(PortNumber[y])
            FlowContent1('96')    
            FlowContent2('Bypass')
            FlowContent1End('96')
            FlowEnd2()
            TestEnd()    
    elif CountFile == 3:
        OperationMode = []
        count = 0
        Entry = 0
        Entry2 = 0
        ChoiceEntry = 0
        for line in xml_contents:
            if 'select' in line:
                line = line.partition('select ')[-1]
                line = line.partition('">')[0]
                word1 = line.partition(' or ')[0]
                word2 = line.partition(' or ')[-1]
                OperationMode.append(word1)
                OperationMode.append(word2)
            else:
                count += 1


        for x in range(len(OperationMode)):
            Flow = str(OperationMode[x]) + 'Flow'
            FlowStart1(Flow)
            FlowDef.append(Flow)
            FlowStart2(CountFileTests[x + 3])
            CountFileTests[x + 3] = str(CountFileTests[x + 3]).replace('Basic','Basic_Used')
            
            # Array List
            PortNumber = []
            PortNumberValue = []

            count = 0
            for line in xml_contents:
                if 'PortNumber' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    PortNumber.append(line)
                    count += 1
                else:
                    count += 1
            count = 0
            for line in xml_contents:
                if 'PortType' in line:
                    line = line.partition('</')[0]
                    line = line.partition('>')[-1]
                    while ' 'in line:
                        line = line.replace(' ','')
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    if line == 'Error':
                        line = line.replace('Error','Fail')
                    PortNumberValue.append(line)
                    count += 1
                else:
                    count += 1


            for x in range(len(PortNumber)):
                FlowContent1(PortNumber[x])
                FlowContent2(PortNumberValue[x])
                FlowContent1End(PortNumber[x])
            
            FlowContent1('96')    
            FlowContent2('Bypass')
            FlowContent1End('96')
            FlowEnd2()
            TestEnd()
    
FlowVariable = []
FlowVariable.append('MainFlow')
FlowVariable.append('InitFlow')
FlowVariable.append('LotStartFlow')
FlowVariable.append('LotEndFlow')
FlowVariable.append('TestPlanStartFlow')
FlowVariable.append('TestPlanEndFlow')


f.write('\n\n')
f.write('FlowDefs')
f.write('\n{')
for x in range(len(FlowVariable)):
    f.write('\n\t')
    f.write(FlowVariable[x])
    f.write(' = ')
    f.write(FlowDef[x])
    f.write(';')
f.write('\n}')
