import os
import time

##############################################
# First Step --- Export Temp.test and .flow  #
##############################################

myfile = 'C:/Users/cheelaml/OneDrive - Intel Corporation/Desktop/python/ConvertPkgToTestAndFlow/AdditionalFile/FilePath.txt'


def BP2(filepath):
    TestFile = "BpTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def BPS(filepath):
    TestFile = "BpsTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile
    
def FP(filepath):
    TestFile = "FpTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def HDDPS(filepath):
    TestFile = "HddpsTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def HPCC(filepath):
    TestFile = "HpccTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def PSE(filepath):
    TestFile = "PseTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def RC2(filepath):
    TestFile = "RcTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def TC2(filepath):
    TestFile = "TcTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile


my_file = open(myfile)
filepath_contents = my_file.readlines()

count = 0
for line in filepath_contents:
    if 'TestType' in line:
            line = line.partition(" '")[-1]
            line = line.partition("'")[0]
            TestType = line

count = 0
for line in filepath_contents:
    if 'TestCommunicationInformation' in line:
            line = line.partition(" '")[-1]
            line = line.partition("'")[0]
            TempFilePath = line
            filepath = (TempFilePath + TestType + '/' + TestType + '/')
            # print(filepath)

if TestType == 'HPCC':
    filepath = HPCC(filepath)
elif TestType == 'BP2':
    filepath = BP2(filepath)
elif TestType == 'BPS':
    filepath = BPS(filepath)
elif TestType == 'FP':
    filepath = FP(filepath)
elif TestType == 'HDDPS':
    filepath = HDDPS(filepath)
elif TestType == 'PSE':
    filepath = PSE(filepath)
elif TestType == 'RC2':
    filepath = RC2(filepath)
elif TestType == 'TC2':
    filepath = TC2(filepath)

Filepath = str(format(filepath))
my_file = open(Filepath)
TestTypefilepath_contents = my_file.readlines()

TestList = []
count = 0
for line in TestTypefilepath_contents:
    if 'static const' in line:
        line = line.partition('string ')[-1]
        line = line.partition(';')[0]
        while ' ' in line:
            line = line.replace(' ','')
        line = line.lower()
        TestList.append(line)

count = 0
for line in filepath_contents:
    if 'PreheaderFilePath' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        PreheaderFilePath = line
        count += 1
        break
    else:
        count += 1
for ReRun in range(4):
    EndCount = count
    count = 0
    for line in filepath_contents:
        if count >= EndCount:
            if 'OtherFilePath' in line:
                line = line.partition(" '")[-1]
                line = line.partition("'")[0]
                OtherFilePath = line
                count += 1
                break
            elif 'PKGFilePath' in line:
                line = line.partition(" '")[-1]
                line = line.partition("'")[0]
                PKGFilePath = line
                count += 1
                break
            elif 'ExportTest' in line:
                line = line.partition(" '")[-1]
                line = line.partition("'")[0]
                ExportTest = line
                count += 1
                break
            elif 'ExportFlow' in line:
                line = line.partition(" '")[-1]
                line = line.partition("'")[0]
                ExportFlow = line
                count += 1
                break
            else:
                count += 1
        else:
            count += 1
count = 0
for line in filepath_contents:
    if 'FinalConvertTest' in line:
        line = line.partition(" '")[-1]
        line = line.partition("'")[0]
        FinalConvertTest = line
        break

print(PreheaderFilePath)
print(OtherFilePath)
print(PKGFilePath)
print(ExportTest)
print(ExportFlow)
print(FinalConvertTest)

# End of "Need To Modify"

def TestStart(Name,testfile):
    f.write("\n\n")
    f.write('Test ')
    f.write(testfile)
    f.write(' ')
    f.write(Name)
    f.write("\n{")
# End of the Test Function
def TestEnd():
    f.write("\n}")

# Test Function
def TestContent(Parameter, value):
    f.write('\n    ')
    f.write(Parameter)
    f.write(' = "')
    f.write(value)
    f.write('";')

def FlowStart1(Name,Temp):
    f.write('\n\n')
    for x in range(Temp):
        f.write('    ')
    f.write('Flow ')
    f.write(Name)
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('{')

def FlowStart2(Test):
    f.write('\n    ')
    f.write('FlowItem ')
    f.write(Test)
    f.write('_eos0 ')
    f.write(Test)
    f.write('\n\t{')

def FlowEnd2(Temp):
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('}')

def MainFlowStart(Num,Name,Temp,flow):
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('FlowItem ')
    f.write(flow)
    f.write('_Execution1')
    f.write('_P')
    f.write(Num)
    f.write('_eos0 ')
    f.write(Name)
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('{')

def FlowContent1(PortNumber,Temp):
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('Result ')
    f.write(PortNumber)
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('{')

def FlowContent1End(PortNumber,Temp):
    f.write('\tReturn ')
    f.write(PortNumber)
    f.write(';')

def FlowContent2(Value,Temp):
    f.write('    ')
    f.write('Property PassFail')
    f.write(' = "')
    f.write(Value)
    f.write('";')

def MainFlowContent(Port,name):
    f.write('    ')
    f.write(Port)
    f.write(' GoTo ')
    f.write(name)

def MainFlowEnd(Temp):
    f.write('\n')
    for x in range(Temp):
        f.write('    ')
    f.write('}')

def ReturnFlow(Port): # Only for Return -4
    f.write('    ')
    f.write(Port)
    f.write(' Return ')
    f.write(Port)

def Increment(Port,PortValue):
    f.write('    ')
    f.write(Port)
    f.write(' IncrementCounters ')
    f.write(PortValue)

def SetBins1(Port):
    f.write('    ')
    f.write(Port)
    f.write(' SetBin SoftBins.b99730002_FF_HVDPS2_5_TIER_1_ALARM')

def SetBins2(Port):
    f.write('    ')
    f.write(Port)
    f.write(' SetBin SoftBins.b99730001_FF_HVDPS2_5_TIER_E_ALARM')

def SetBins3(Port):
    f.write('    ')
    f.write(Port)
    f.write(' SetBin SoftBins.b98730001_FF_HVDPS2_5_SOFTWARE_EXCEP')

def SetBins4(Port):
    f.write('    ')
    f.write(Port)
    f.write(' SetBin SoftBins.b98730002_FF_HVDPS2_5GENERIC_DIAG_EXCEP')

def SetBins5(Port, Name):
    f.write('    ')
    f.write(Port)
    f.write(' SetBin SoftBins.b42730002_')
    f.write(Name)

def BP2(filepath):
    TestFile = "BpTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def BPS(filepath):
    TestFile = "BpsTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile
    
def FP(filepath):
    TestFile = "FpTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def HDDPS(filepath):
    TestFile = "HddpsTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def HPCC(filepath):
    TestFile = "HpccTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def PSE(filepath):
    TestFile = "PseTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def RC2(filepath):
    TestFile = "RcTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile

def TC2(filepath):
    TestFile = "TcTestList.h"
    # print(filepath + TestFile)
    headerfile = (filepath + TestFile)
    return headerfile


# Array File Name that contains <FileName> Tag
FileName = []

# Record All test after convert
TestWithPath = []

PreHeader_Path = PreheaderFilePath 
for filename in os.listdir(PreHeader_Path):
   with open(os.path.join(PreHeader_Path, filename), 'r') as f:
       text = f.read()
       if '<FileName>' in text:
            # print(filename)
            FileName.append(filename)

# Find bdefs and usrv file
other_file = []

file_path = OtherFilePath 
TempFileArray = (os.listdir(file_path))
for x in range(len(TempFileArray)):
    if 'bdefs' in TempFileArray[x]:
        other_file.append(TempFileArray[x])
    elif 'usrv' in TempFileArray[x]:
        other_file.append(TempFileArray[x])


my_file = open(PKGFilePath)
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
f = open(ExportTest, "w")
# write in the version
f.write("Version ")
f.write(ver)
f.write(";\n")

# ProgramStyle
f.write("ProgramStyle = Modular;")

# TestPlan
f.write("\n\nTestPlan ")
f.write('HPCC')
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
ChoicesTest = []
for CountFile in range(len(FileName)):
    xml = PreHeader_Path + FileName[CountFile]
    xml_file = open(xml)
    xml_contents = xml_file.readlines()

    count = 0
    # CalDiagDummyTestClass.xml
    if CountFile == 0:
        for line in xml_contents:
            if '<Choices>' in line:
                EndCount = count
                break
            else:
                count += 1

        count = 0
        for line in xml_contents:
            if count > EndCount:
                if '<Choice>' in line:
                    line = line.partition('>')[-1]
                    line = line.partition('<')[0]
                    while '\n' in line:
                        line = line.replace('\n','')
                    while '\t' in line:
                        line = line.replace('\t','')
                    while ' ' in line:
                        line = line.replace(' ','')
                    ChoicesTest.append(line)
                    count += 1
                elif '</Choices>' in line:
                    break
                else:
                    count += 1
            else:
                count += 1

# Array Lists
Total_Device = []
Total_Tests = []
Device_Parameter = []
Parameter_Value = []

count = 0
for line in dummy_contents:
    if '<device' in line:
        line = line.partition('="')[-1]
        line = line.partition('binary')[0]
        while '\n' in line:
            line = line.replace('\n','')
        while ' ' in line:
            line = line.replace(' ','')
        while '\t' in line:
            line = line.replace('\t', '')
        line = line + ' Status = "Not Yet"'
        Total_Device.append(line + ' Count:' + str(count))
        count += 1
    else:
        count += 1

count = 0
TotalTest_Numbers = []
for line in dummy_contents:
    if '<test name=' in line:
        TestOperation = ""
        number = line.partition('number="')[-1]
        number = number.partition('" ')[0]

        line = line.partition('name="')[-1]
        line = line.partition(' binary')[0]
        while ' ' in line:
            line = line.replace(' ','')
        while '\n' in line:
            line = line.replace('\n','')
        while '\t' in line:
            line = line.replace('\t','')
        number = "TestName = " + line.partition('"')[0] + " TestOperation = " + number
        TotalTest_Numbers.append(number)
        Total_Tests.append(line)
        count += 1
    else:
        count += 1
# Save testflow name for flow file
TestFlowArrayName = []
# print(TotalTest_Numbers[0])
# Finish storing Device Array
FirstTest = True
for TestingLoopFirstTry in range(len(Total_Tests)):
    if FirstTest == True:
        testname = str(Total_Tests[0]).replace('"','')
        while '-' in testname:
            testname = testname.replace('-','_')
        while '(' in testname:
            testname = testname.replace('(','_')
            testname = testname.replace(')','')
        while '.' in testname:
            testname = testname.replace('.','p')
        # for Search in range(len(TotalTest_Numbers)):
        #     if testname in str(TotalTest_Numbers[Search]).partition(' TestOperation')[0]:
        #         TestOperationNumber = str(TotalTest_Numbers[Search]).partition(' TestOperation = ')[-1]
        # print(TestOperationNumber)

        for Search in range(len(TotalTest_Numbers)):
            if testname in str(TotalTest_Numbers[Search]).partition(' TestOperation')[0]:
                TestOperationNumber = str(TotalTest_Numbers[Search]).partition(' TestOperation = ')[-1]
        # print(testname + " and " +TestOperationNumber)
        TestOperationName = ""
        for SecondSearch in range(len(TestList)):
            if TestOperationNumber == str(TestList[SecondSearch]):
                # print("matching " + str(TestList[SecondSearch]) + " with " + TestOperationNumber)
                TestOperationName = str(TestList[SecondSearch])
                break
            elif TestOperationNumber != str(TestList[SecondSearch]):
                TestOperationName = ""


        # Get the number name by using endcount
        count = 0
        for line in dummy_contents:
            if count > EndCount:
                if '<test name=' in line:
                    line = line.partition('number="')[-1]
                    line = line.partition('" timeout=')[0]
                    # print(line)
                    for x in range(len(ChoicesTest)):
                        if line in ChoicesTest[x]:
                            CountFile = 0
                            testfile = str(FileName[CountFile]).replace('.xml','')
                            break
                        else:
                            testfile = ''
                    break
                else:
                    count += 1
            else:
                count += 1
        
        DeviceCount = 0
        New_Device = False
        count = 0
        TempDeviceCountArray = []
        for line in dummy_contents:
            if '<device name=' in line:
                for x in range(len(Total_Device)):
                    if 'Status = "Not Yet"' in Total_Device[x]:
                        DeviceCount = x
                        Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status = "Start"')
                        DeviceCount += 1
                        New_Device = True
                        Last_Device_Count = count
                        EndCount = count
                        TempDeviceCountArray.append(count)
                        # print(count)
                        break
                count += 1
            elif '<test name' in line:
                break
            else:
                count += 1


        # Backup the Original Array
        BackUp_Device = []
        SecondCombine = []
        for x in range(len(Device_Parameter)):
            BackUp_Device.append(Device_Parameter[x])
        # print(TempDeviceCountArray)
        RepeatArray = []
        SecondRepeatArray = [] #check again the value
        # for TempDeviceCount in range(len(TempDeviceCountArray)):
        if New_Device == True:
            # Check How many Start Status
            CurrentStartDeviceArray = []
            for x in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[x]:
                    CurrentStartDeviceArray.append(str(Total_Device[x]).partition('Count:')[-1])

            # Remove First Device
            # del CurrentStartDeviceArray[0]

            RangeCount = len(CurrentStartDeviceArray)
            # for xDevice in range(len(CurrentStartDeviceArray)-1):
            TempParam = []
            TempValue = []
            del_count = []

            for xDevice in range(RangeCount):
                count = 0
                for line in dummy_contents:
                    if count > int(CurrentStartDeviceArray[0]):
                        if '<param name=' in line:
                            Param = line.partition('="')[-1]
                            Param = Param.partition(' value')[0]
                            while ' ' in Param:
                                Param = Param.replace(' ','')
                            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                            line = line.replace('value=','vvalue=')
                            line = line.partition('value="')[-1]
                            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                            while '\n' in Param:
                                Param = Param.replace('\n','')
                            while '\t' in Param:
                                Param = Param.replace('\t','')
                            while '\n' in line:
                                line = line.replace('\n','')
                            while '\t' in line:
                                line = line.replace('\t','')
                            line = 'Variable =' + line
                            for checkRepeat in range(len(Device_Parameter)):
                                if str(Param).partition(' ParamStatus')[0] == str(Device_Parameter[checkRepeat]).partition(' ParamStatus')[0]:
                                    del_count.append(checkRepeat)

                            Device_Parameter.append(Param)
                            Parameter_Value.append(line)
                            count += 1
                        elif '<test name=' in line:
                            break
                        elif '</test>' in line:
                            break
                        elif '</device>' in line:
                            break
                        elif '<device' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1
                if (len(CurrentStartDeviceArray)) > 0:
                    del CurrentStartDeviceArray[0]

            # delete the repeat
            del_count = (list(set(del_count)))
            del_count.sort(reverse=True)
            # print(del_count)
            
            conditionRange = len(del_count)
            for delCount in range(conditionRange):
                del Device_Parameter[del_count[0]]
                del Parameter_Value[del_count[0]]
                if len(del_count) > 0:
                    del del_count[0]
        TempCount = count
        count = 0
        # Decide the condition
        count = 0
        Del_Test_Param = False
        for line in dummy_contents:
            if count > EndCount:
                if '<test name' in line:
                    Del_Test_Param = True
                    EndCount = count
                    count += 1
                    break
                else:
                    Del_Test_Param = False
                    count += 1
            else:
                count += 1

        # second time checking the condition
        TempCount = count
        count = 0
        if Del_Test_Param == True:
            for line in dummy_contents:
                if count >= TempCount:
                    if '</test>' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1

        if (count - TempCount) == 0:
            Del_Test_Param = False
        elif (count - TempCount) > 1:
            Del_Test_Param = True

        del_count = []
        if Del_Test_Param == True:
            TTempCount = count
            count = 0
            for line in dummy_contents:
                if count > EndCount:
                    if '<param name="' in line:
                        Param = line.partition('="')[-1]
                        Param = Param.partition(' value')[0]
                        while ' ' in Param:
                            Param = Param.replace(' ','')
                        Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                        line = line.replace('value=','vvalue=')
                        line = line.partition('value="')[-1]
                        line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                        while '\n' in Param:
                            Param = Param.replace('\n','')
                        while '\t' in Param:
                            Param = Param.replace('\t','')
                        while '\n' in line:
                            line = line.replace('\n','')
                        while '\t' in line:
                            line = line.replace('\t','')
                        line = 'Variable =' + line

                        for checkRepeat in range(len(Device_Parameter)):
                            if str(Param).partition(' ParamStatus')[0] == str(Device_Parameter[checkRepeat]).partition(' ParamStatus')[0]:
                                del_count.append(checkRepeat)
                                
                        Device_Parameter.append(Param)
                        Parameter_Value.append(line)
                        TempParam.append(Param)
                        TempValue.append(line)
                        SecondRepeatArray.append(Param)
                        SecondCombine.append(Param)
                        count += 1

                    elif '</device>' in line:
                        break
                    elif '</test>' in line:
                        EndCount = count
                        break
                    elif '<test name' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1

        # delete the repeat
        del_count = (list(set(del_count)))
        del_count.sort(reverse=True)
        # print(del_count)

        conditionRange = len(del_count)
        for delCount in range(conditionRange):
            # print(Device_Parameter[del_count[0]],Parameter_Value[del_count[0]])
            del Device_Parameter[del_count[0]]
            del Parameter_Value[del_count[0]]
            if len(del_count) > 0:
                del del_count[0]


        # Write into file
        testfile = str(FileName[0]).replace('.xml','')

        CurrentlyStart = []
        for checkDevice in range(len(Total_Device)):
            if 'Status = "Start"' in Total_Device[checkDevice]:
                CurrentlyStart.append(str(Total_Device[checkDevice]).partition('" ')[0])
        Temptestname = ('___'.join(CurrentlyStart) + '___' +testname)
        TestWithPath.append(Temptestname)
        testname = (''.join(CurrentlyStart) + '' +testname)
        TestStart(testname,testfile)
        TempTestFlow = testfile + ' ' + testname
        TestFlowArrayName.append(TempTestFlow)

        for x in range(len(Device_Parameter)):
            paramx = str(Device_Parameter[x]).partition('ParamStatus')[0]
            paramy = str(Parameter_Value[x]).partition(' ValueStatus')[0]
            paramy = paramy.replace('Variable =','')
            TestContent(paramx,paramy)
        TestContent('TestOperation',TestOperationName)
        TestEnd()
        FirstTest = False

        LastDevice = 0
        count = 0
        for line in dummy_contents:
            if count > EndCount:
                if '</device>' in line:
                    LastDevice = count
                    Del_Last_Device = True
                    EndCount = count
                    break
                elif '<test name' in line:
                    # EndCount = count
                    break
                else:
                    count += 1
            else:
                count += 1
        
        if Del_Test_Param == True:
        # Remove Value Array
            Del_Descending = []
            for x in range(len(Device_Parameter)):
                for y in range(len(TempParam)):
                    if TempParam[y] in Device_Parameter[x]:
                        Del_Descending.append(x)
                        # print(TempParam[y], Device_Parameter[x])
                        break

            Del_Descending.sort(reverse = True)
            for x in range(len(Del_Descending)):
                del Device_Parameter[Del_Descending[x]]

            # Remove Value Array
            Del_Descending = []
            for x in range(len(Parameter_Value)):
                for y in range(len(TempValue)):
                    if TempValue[y] in Parameter_Value[x]:
                        # print(TempValue[y], Parameter_Value[x])
                        Del_Descending.append(x)
                        # print(x)
                        break
            Del_Descending.sort(reverse = True)

            Del_Descending.sort(reverse = True)

            for x in range(len(Del_Descending)):
                del Parameter_Value[Del_Descending[x]]

            # delete the last test
            del Total_Tests[0]

            y = 0
            for x in range(len(Total_Device)):
                if 'Status ="End"' in Total_Device[x]:
                    y += 1
            for DeleteEnd in range(y):
                for x in range(len(Total_Device)):
                    if 'Status ="End"' in Total_Device[x]:
                        del Total_Device[x]
                        break
            # update LastDevice
            count = 0
            for line in dummy_contents:
                if count >= LastDevice:
                    if '</device>' in line:
                        # print(line, count + 1)
                        LastDevice = count
                        count += 1
                    elif '<device name' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1
            

            for Close in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[Close]:
                    line = str(Total_Device[Close]).partition('Count:')[-1]
                    LatestStartDevice = int(line)
            # print(LatestStartDevice)           
            
            for Close in range(len(Total_Device)):
                if str(LatestStartDevice) == str(Total_Device[Close]).partition('Count:')[-1]:
                    # print(Total_Device[Close])
                    del Total_Device[Close]
                    break
            

    elif FirstTest == False:
        # Next Test Start
        # Delete Array
        TempParam = []
        TempValue = []
        Del_Descending = []
        TempEndDeviceCountArray = []

        Del_Last_Device = False
        count = 0
        for line in dummy_contents:
            if count > EndCount:
                if count > LastDevice:
                    if '</device>' in line:
                        LastDevice = count
                        Del_Last_Device = True
                        EndCount = count
                        TempEndDeviceCountArray.append(count)
                        break
                    elif '<test name' in line:
                        # EndCount = count
                        break
                    else:
                        count += 1
                else:
                    count += 1
            else:
                count += 1
    
        # Check is the next line is </device> or not
        count = 0
        for line in dummy_contents:
            if count > EndCount:
                if '</device>' in line:
                    TempEndDeviceCountArray.append(count)
                elif '<device name' in line:
                    break
                elif '<test name' in line:
                    break
                else:
                    count += 1
            else:
                count += 1

        # print(TempEndDeviceCountArray)

        LatestStartDeviceArray = []
        if (len(TempEndDeviceCountArray)) > 0:
            for x in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[x]:
                    line = str(Total_Device[x]).partition('Count:')[-1]
                    LatestStartDevice = int(line)
                    # print(LatestStartDevice)
                    LatestStartDeviceArray.append(LatestStartDevice)

            for EndDeviceCount in range(len(TempEndDeviceCountArray)):
                # print('hi')
                if (len(LatestStartDeviceArray)) > 0:
                    del_device_count = (LatestStartDeviceArray[(len(LatestStartDeviceArray))-1])
                    del (LatestStartDeviceArray[(len(LatestStartDeviceArray))-1])
                # print('del_device_count:',del_device_count)

                count = 0
                for line in dummy_contents:
                    if count > del_device_count:
                        if '<param name=' in line:
                            Param = line.partition('="')[-1]
                            Param = Param.partition(' value')[0]
                            while ' ' in Param:
                                Param = Param.replace(' ','')
                            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                            line = line.replace('value=','vvalue=')
                            line = line.partition('value="')[-1]
                            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                            while '\n' in Param:
                                Param = Param.replace('\n','')
                            while '\t' in Param:
                                Param = Param.replace('\t','')
                            while '\n' in line:
                                line = line.replace('\n','')
                            while '\t' in line:
                                line = line.replace('\t','')
                            line = 'Variable =' + line
                            # print(Param, line)
                            TempParam.append(Param)
                            TempValue.append(line)
                            count += 1
                        elif '<test name=' in line:
                            break
                        elif '</test>' in line:
                            break
                        elif '</device>' in line:
                            break
                        elif '<device name' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1
                # Remove Value Array
                Del_Descending = []

                for x in range(len(Device_Parameter)):
                    for y in range(len(TempParam)):
                        if TempParam[y] in Device_Parameter[x]:
                            # print(TempParam[y], Device_Parameter[x])
                            Del_Descending.append(x)
                Del_Descending.sort(reverse = True)
                for x in range(len(Del_Descending)):
                    del Device_Parameter[Del_Descending[x]]

                # Remove Value Array
                Del_Descending = []

                for x in range(len(Parameter_Value)):
                    for y in range(len(TempValue)):
                        if TempValue[y] in Parameter_Value[x]:
                            # print(TempValue[y], Parameter_Value[x])
                            Del_Descending.append(x)
                            # print(x)
                Del_Descending.sort(reverse = True)

                for x in range(len(Del_Descending)):
                    del Parameter_Value[Del_Descending[x]]

                for x in range(len(Total_Device)):
                    if 'Count:' + str(del_device_count) in Total_Device[x]:
                        # print(Total_Device[x])
                        del Total_Device[x]
                        # print('Got it')
                        break

            # print(LatestStartDeviceArray)
        Del_Last_Device = False
        testname = str(Total_Tests[0]).replace('"','')
        while '-' in testname:
            testname = testname.replace('-','_')
        while '(' in testname:
            testname = testname.replace('(','_')
            testname = testname.replace(')','')
        while '.' in testname:
            testname = testname.replace('.','p')
        # print(testname)
        for Search in range(len(TotalTest_Numbers)):
            if testname in str(TotalTest_Numbers[Search]).partition(' TestOperation')[0]:
                TestOperationNumber = str(TotalTest_Numbers[Search]).partition(' TestOperation = ')[-1]
        # print(testname + " and " +TestOperationNumber)
        TestOperationName = ""
        for SecondSearch in range(len(TestList)):
            if TestOperationNumber == str(TestList[SecondSearch]):
                # print("matching " + str(TestList[SecondSearch]) + " with " + TestOperationNumber)
                TestOperationName = str(TestList[SecondSearch])
                break
            elif TestOperationNumber != str(TestList[SecondSearch]):
                TestOperationName = ""
                # print("Not match")
        # print(TestOperationName)
        # Get the number name by using endcount
        count = 0
        # print(ChoicesTest)
        for line in dummy_contents:
            if count > EndCount:
                if '<test name=' in line:
                    line = line.partition('number="')[-1]
                    line = line.partition('" timeout=')[0]
                    # print(line)
                    for x in range(len(ChoicesTest)):
                        if line in ChoicesTest[x]:
                            # print(ChoicesTest[x])
                            CountFile = 0
                            testfile = str(FileName[CountFile]).replace('.xml','')
                            break
                        else:
                            testfile = ''
                    break
                else:
                    count += 1
            else:
                count += 1


        DeviceCount = 0
        New_Device = False
        count = 0
        TempDeviceCountArray = []
        for line in dummy_contents:
            if count >= EndCount:
                if '<device name=' in line:
                    for x in range(len(Total_Device)):
                        if 'Status = "Not Yet"' in Total_Device[x]:
                            DeviceCount = x
                            Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status = "Start"')
                            DeviceCount += 1
                            New_Device = True
                            Last_Device_Count = count
                            EndCount = count
                            TempDeviceCountArray.append(count)
                            # print(count)
                            break
                    count += 1
                elif '<test name' in line:
                    break
                else:
                    count += 1
            else:
                count += 1


        # Backup the Original Array
        BackUp_Device = []
        SecondCombine = []
        for x in range(len(Device_Parameter)):
            BackUp_Device.append(Device_Parameter[x])
        # print(TempDeviceCountArray)
        RepeatArray = []
        SecondRepeatArray = [] #check again the value
        # for TempDeviceCount in range(len(TempDeviceCountArray)):
        if New_Device == True:
            # Check How many Start Status
            CurrentStartDeviceArray = []
            for x in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[x]:
                    CurrentStartDeviceArray.append(str(Total_Device[x]).partition('Count:')[-1])

            # Remove First Device
            # del CurrentStartDeviceArray[0]

            RangeCount = len(CurrentStartDeviceArray)
            # for xDevice in range(len(CurrentStartDeviceArray)-1):
            TempParam = []
            TempValue = []
            del_count = []

            for xDevice in range(RangeCount):
                count = 0
                for line in dummy_contents:
                    if count > int(CurrentStartDeviceArray[0]):
                        if '<param name=' in line:
                            Param = line.partition('="')[-1]
                            Param = Param.partition(' value')[0]
                            while ' ' in Param:
                                Param = Param.replace(' ','')
                            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                            line = line.replace('value=','vvalue=')
                            line = line.partition('value="')[-1]
                            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                            while '\n' in Param:
                                Param = Param.replace('\n','')
                            while '\t' in Param:
                                Param = Param.replace('\t','')
                            while '\n' in line:
                                line = line.replace('\n','')
                            while '\t' in line:
                                line = line.replace('\t','')
                            line = 'Variable =' + line
                            # print(Param, line)
                            # check the repeat
                            for checkRepeat in range(len(Device_Parameter)):
                                if str(Param).partition(' ParamStatus')[0] == str(Device_Parameter[checkRepeat]).partition(' ParamStatus')[0]:
                                    # print(Device_Parameter[checkRepeat])
                                    del_count.append(checkRepeat)

                            Device_Parameter.append(Param)
                            Parameter_Value.append(line)
                            count += 1
                        elif '<test name=' in line:
                            break
                        elif '</test>' in line:
                            break
                        elif '</device>' in line:
                            break
                        elif '<device' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1
                if (len(CurrentStartDeviceArray)) > 0:
                    del CurrentStartDeviceArray[0]

            # delete the repeat
            del_count = (list(set(del_count)))
            del_count.sort(reverse=True)
            # print(del_count)

            conditionRange = len(del_count)
            for delCount in range(conditionRange):
                # print(Device_Parameter[del_count[0]],Parameter_Value[del_count[0]])
                del Device_Parameter[del_count[0]]
                del Parameter_Value[del_count[0]]
                if len(del_count) > 0:
                    del del_count[0]

        elif New_Device == False:
            # Check How many Start Status
            CurrentStartDeviceArray = []
            for x in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[x]:
                    CurrentStartDeviceArray.append(str(Total_Device[x]).partition('Count:')[-1])

            # Remove First Device
            # del CurrentStartDeviceArray[0]

            RangeCount = len(CurrentStartDeviceArray)
            # for xDevice in range(len(CurrentStartDeviceArray)-1):
            TempParam = []
            TempValue = []
            for xDevice in range(RangeCount):
                count = 0
                for line in dummy_contents:
                    if count > int(CurrentStartDeviceArray[0]):
                        if '<param name=' in line:
                            Param = line.partition('="')[-1]
                            Param = Param.partition(' value')[0]
                            while ' ' in Param:
                                Param = Param.replace(' ','')
                            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                            line = line.replace('value=','vvalue=')
                            line = line.partition('value="')[-1]
                            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                            while '\n' in Param:
                                Param = Param.replace('\n','')
                            while '\t' in Param:
                                Param = Param.replace('\t','')
                            while '\n' in line:
                                line = line.replace('\n','')
                            while '\t' in line:
                                line = line.replace('\t','')
                            line = 'Variable =' + line
                            # print(Param, line)
                            TempParam.append(Param)
                            TempValue.append(line)
                            for checkRepeat in range(len(Device_Parameter)):
                                if str(Param).partition(' ParamStatus')[0] == str(Device_Parameter[checkRepeat]).partition(' ParamStatus')[0]:
                                    RepeatArray.append(Param)
                                    # print('The REPEAT:',Device_Parameter[checkRepeat])
                            if Param not in RepeatArray:
                                Device_Parameter.append(Param)
                                Parameter_Value.append(line)
                                SecondRepeatArray.append(Param)
                                SecondCombine.append(Param)
                            count += 1
                        elif '<test name=' in line:
                            break
                        elif '</test>' in line:
                            break
                        elif '</device>' in line:
                            break
                        elif '<device' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1
                del CurrentStartDeviceArray[0]

        New_Device = False

        TempCount = count
        count = 0
        # Decide the condition
        count = 0
        Del_Test_Param = False
        for line in dummy_contents:
            if count > EndCount:
                if '<test name' in line:
                    Del_Test_Param = True
                    EndCount = count
                    count += 1
                    break
                else:
                    Del_Test_Param = False
                    count += 1
            else:
                count += 1

        # second time checking the condition
        TempCount = count
        count = 0
        if Del_Test_Param == True:
            for line in dummy_contents:
                if count >= TempCount:
                    if '</test>' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1

        if (count - TempCount) == 0:
            Del_Test_Param = False
        elif (count - TempCount) > 1:
            Del_Test_Param = True

        del_count = []
        if Del_Test_Param == True:
            TTempCount = count
            count = 0
            for line in dummy_contents:
                if count > EndCount:
                    if '<param name="' in line:
                        Param = line.partition('="')[-1]
                        Param = Param.partition(' value')[0]
                        while ' ' in Param:
                            Param = Param.replace(' ','')
                        Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                        line = line.replace('value=','vvalue=')
                        line = line.partition('value="')[-1]
                        line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                        while '\n' in Param:
                            Param = Param.replace('\n','')
                        while '\t' in Param:
                            Param = Param.replace('\t','')
                        while '\n' in line:
                            line = line.replace('\n','')
                        while '\t' in line:
                            line = line.replace('\t','')
                        line = 'Variable =' + line
                        # print(Param, line)
                        # check the repeat
                        for checkRepeat in range(len(Device_Parameter)):
                            if str(Param).partition(' ParamStatus')[0] == str(Device_Parameter[checkRepeat]).partition(' ParamStatus')[0]:
                                # print('The Repeat - ',Param,Device_Parameter[checkRepeat])
                                # print(checkRepeat)
                                del_count.append(checkRepeat)
                                
                        Device_Parameter.append(Param)
                        Parameter_Value.append(line)
                        TempParam.append(Param)
                        TempValue.append(line)
                        SecondRepeatArray.append(Param)
                        SecondCombine.append(Param)
                        count += 1
                    # elif '<device' in line:
                    #     Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
                    #     TempCount2 = count
                    #     DeviceCount += 1
                    #     count += 1
                    elif '</device>' in line:
                        break
                    elif '</test>' in line:
                        EndCount = count
                        break
                    elif '<test name' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1

        # delete the repeat
        del_count = (list(set(del_count)))
        del_count.sort(reverse=True)
        # print(del_count)

        conditionRange = len(del_count)
        for delCount in range(conditionRange):
            # print(Device_Parameter[del_count[0]],Parameter_Value[del_count[0]])
            del Device_Parameter[del_count[0]]
            del Parameter_Value[del_count[0]]
            if len(del_count) > 0:
                del del_count[0]


        # Write into file
        testfile = str(FileName[0]).replace('.xml','')

        CurrentlyStart = []
        for checkDevice in range(len(Total_Device)):
            if 'Status = "Start"' in Total_Device[checkDevice]:
                CurrentlyStart.append(str(Total_Device[checkDevice]).partition('" ')[0])
        Temptestname = ('___'.join(CurrentlyStart) + '___' +testname)
        TestWithPath.append(Temptestname)
        testname = (''.join(CurrentlyStart) + '' +testname)
        while '.' in testname:
            testname = testname.replace('.','p')
        TestStart(testname,testfile)
        TempTestFlow = testfile + ' ' + testname
        TestFlowArrayName.append(TempTestFlow)
        

        for x in range(len(Device_Parameter)):
            paramx = str(Device_Parameter[x]).partition('ParamStatus')[0]
            paramy = str(Parameter_Value[x]).partition(' ValueStatus')[0]
            paramy = paramy.replace('Variable =','')
            TestContent(paramx,paramy)
        TestContent('TestOperation',str(TestOperationName))
        TestEnd()
        
        if Del_Test_Param == True:
            # Remove Value Array
            Del_Descending = []
            for x in range(len(Device_Parameter)):
                for y in range(len(TempParam)):
                    if TempParam[y] in Device_Parameter[x]:
                        Del_Descending.append(x)
                        # print(TempParam[y], Device_Parameter[x])
                        break

            Del_Descending.sort(reverse = True)
            for x in range(len(Del_Descending)):
                del Device_Parameter[Del_Descending[x]]

            # Remove Value Array
            Del_Descending = []
            for x in range(len(Parameter_Value)):
                for y in range(len(TempValue)):
                    if TempValue[y] in Parameter_Value[x]:
                        # print(TempValue[y], Parameter_Value[x])
                        Del_Descending.append(x)
                        # print(x)
                        break
            Del_Descending.sort(reverse = True)

            Del_Descending.sort(reverse = True)

            for x in range(len(Del_Descending)):
                del Parameter_Value[Del_Descending[x]]

            # delete the last test
            del Total_Tests[0]

            y = 0
            for x in range(len(Total_Device)):
                if 'Status ="End"' in Total_Device[x]:
                    y += 1
            for DeleteEnd in range(y):
                for x in range(len(Total_Device)):
                    if 'Status ="End"' in Total_Device[x]:
                        del Total_Device[x]
                        break
            # update LastDevice
            count = 0
            for line in dummy_contents:
                if count >= LastDevice:
                    if '</device>' in line:
                        # print(line, count + 1)
                        LastDevice = count
                        count += 1
                    elif '<device name' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1
        elif Del_Test_Param == False:
            # update the data
            count = 0
            device_end_count = 0
            for line in dummy_contents:
                if count > EndCount:
                    if '<device name' in line:
                        TempCount2 = count
                        break
                    elif '</test>' in line:
                        break
                    elif '</device>' in line:
                        device_end_count += 1
                        LastDevice = count
                        # print(line,' count:',count + 1)
                        count += 1
                    else:
                        count += 1
                else:
                    count += 1
            EndCount = count
            del_count = []
            y = 0
            for x in range(len(Total_Device)):
                if 'Status = "Start"' in Total_Device[x]:
                    y += 1
            for x in range(device_end_count):
                if y >=0 :
                    Total_Device[y - 1] = str(Total_Device[y - 1]).replace('Status = "Start"', 'Status ="End"')
                    y -= 1
                else:
                    break
            for x in range(len(Total_Device)):
                for y in range(device_end_count):
                    if 'Status ="End"' in Total_Device[x]:
                        del_count.append(int((str(Total_Device[x]).partition('Count:')[-1])))

            # print(del_count)
            # print(y)
            # print(device_end_count)

            for Del_Data in range(len(del_count)):
                count = 0
                for line in dummy_contents:
                    if count > del_count[0]:
                        if '<param name' in line:
                            Param = line.partition('="')[-1]
                            Param = Param.partition(' value')[0]
                            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
                            line = line.replace('value=','vvalue=')
                            line = line.partition('value="')[-1]
                            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
                            line = 'Variable =' + line
                            while '\n' in line:
                                line = line.replace('\n','')
                            while '\t' in line:
                                line = line.replace('\t', '')
                            while '\n' in Param:
                                Param = Param.replace('\n','')
                            while '\t' in Param:
                                Param = Param.replace('\t', '')
                            # print(Param,line)
                            TempParam.append(Param)
                            TempValue.append(line)
                            count += 1
                        elif '</device>' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1

                # Remove Value Array
                Del_Descending = []

                for x in range(len(Device_Parameter)):
                    for y in range(len(TempParam)):
                        if TempParam[y] in Device_Parameter[x]:
                            # print(TempParam[y], Device_Parameter[x])
                            Del_Descending.append(x)
                Del_Descending.sort(reverse = True)
                for x in range(len(Del_Descending)):
                    del Device_Parameter[Del_Descending[x]]

                # Remove Value Array
                Del_Descending = []

                for x in range(len(Parameter_Value)):
                    for y in range(len(TempValue)):
                        if TempValue[y] in Parameter_Value[x]:
                            # print(TempValue[y], Parameter_Value[x])
                            Del_Descending.append(x)
                            # print(x)
                Del_Descending.sort(reverse = True)

                for x in range(len(Del_Descending)):
                    del Parameter_Value[Del_Descending[x]]
                del del_count[0]

            # delete the last test
            del Total_Tests[0]

            y = 0
            for x in range(len(Total_Device)):
                if 'Status ="End"' in Total_Device[x]:
                    y += 1
            for DeleteEnd in range(y):
                for x in range(len(Total_Device)):
                    if 'Status ="End"' in Total_Device[x]:
                        del Total_Device[x]
                        break
            # update LastDevice
            count = 0
            for line in dummy_contents:
                if count >= LastDevice:
                    if '</device>' in line:
                        # print(line, count + 1)
                        LastDevice = count
                        count += 1
                    elif '<device name' in line:
                        break
                    else:
                        count += 1
                else:
                    count += 1


# New Flow file

TestFlowArray = []
count = 0
for line in dummy_contents:
    if count > EndCount:
        if '<test ref' in line:
            Clone = line
            Clone = line.partition("@name='")[-1]
            # print(Clone)
            while "@name='" in Clone:
                TempClone = Clone.partition("@name='")[-1]
                # print(TempClone)
                Clone = (Clone.partition("' ")[0] + TempClone)
            while ' ' in Clone:
                Clone = Clone.replace(' ','')
            while '-' in Clone:
                Clone = Clone.replace('-','_')
            while '(' in Clone:
                Clone = Clone.replace('(','_')
                Clone = Clone.replace(')','')
            while '.' in Clone:
                Clone = Clone.replace('.','p')
            Clone = Clone.partition("']")[0]
            # print(Clone)
            # TestFlowArray.append(Clone + '___' + line)
            TestFlowArray.append(Clone)
            count += 1
        else:
            count += 1
    else:
        count += 1
# print(str(TestWithPath).replace('___',''))
# print(TestFlowArray)
# print('###########################\n\n\n')
# print(str(TestWithPath).replace('___',''))
# Store the new TestFlow name (with path)
TestFlowArrayPath = []
# Match the testflow with Testname (with path)
for y in range(len(TestFlowArray)):
    for x in range(len(TestWithPath)):
        if str(TestFlowArray[y]) == str(TestWithPath[x]).replace('___',''):
            # print(str(TestWithPath[x]).replace('___',''))
            while '-' in TestWithPath[x]:
                TestWithPath[x] = str(TestWithPath[x]).replace('-','_')
            while '(' in TestWithPath[x]:
                TestWithPath[x] = str(TestWithPath[x]).replace('(','_')
                TestWithPath[x] = str(TestWithPath[x]).replace(')','')
            TestFlowArrayPath.append(TestWithPath[x])
            break
# print(str(TestWithPath[0]).replace('___',''))
# print((TestFlowArray))
# print((TestFlowArrayPath))
PortNumber = []
PortNumberValue = []

PortNumber.append('-4')
PortNumber.append('-3')
PortNumber.append('-2')
PortNumber.append('-1')
PortNumber.append('0')
PortNumber.append('1')
PortNumber.append('70')
PortNumber.append('71')
PortNumber.append('96')


PortNumberValue.append('FF_HVDPS2_5_TIER_1_ALARM')
PortNumberValue.append('FF_HVDPS2_5_TIER_E_ALARM')
PortNumberValue.append('FF_HVDPS2_5_SOFTWARE_EXCEP')
PortNumberValue.append('FF_HVDPS2_5GENERIC_DIAG_EXCEP')
PortNumberValue.append('FF_')


Tab = 0
Num = 1
ResultTab = Tab
ResultTab += 1
Flow = 'MainFlow'

# create flow file
f = open(ExportFlow, "w")
# set the flow name
testflow = 'HpccTestFlow'
f.write('TESTFLOW_START:')
f.write(testflow)
f.write('\n')
if '.' in (TestFlowArrayName[0]):
    (TestFlowArrayName[0]) = str(TestFlowArrayName[0]).replace('.','p')
    f.write(str(TestFlowArrayName[0]))
else:
    f.write(str(TestFlowArrayName[0].partition(' ')[0]))
    f.write(' ')
    f.write(str(TestFlowArrayPath[0]).replace('___',''))

TempMainFlow = 1
for convertFlow in range(len(PortNumber)):
    f.write('\n')
    if str(PortNumber[convertFlow]) == '-4': 
        ReturnFlow(PortNumber[convertFlow])
        f.write('\n')
        Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
        f.write('\n')
        SetBins1(PortNumber[convertFlow])
    elif str(PortNumber[convertFlow]) == '-3':
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
        f.write('\n')
        Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
        f.write('\n')
        SetBins2(PortNumber[convertFlow])
    elif str(PortNumber[convertFlow]) == '-2':
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
        f.write('\n')
        Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
        f.write('\n')
        SetBins3(PortNumber[convertFlow])
    elif str(PortNumber[convertFlow]) == '-1':
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
        f.write('\n')
        Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
        f.write('\n')
        SetBins4(PortNumber[convertFlow])
    elif str(PortNumber[convertFlow]) == '0':
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
        NameForPort = str(PortNumberValue[convertFlow]) + str(TestFlowArrayPath[TempMainFlow - 1]).replace('___','')
        f.write('\n')
        Increment(PortNumber[convertFlow],NameForPort)
        f.write('\n')
        SetBins5(PortNumber[convertFlow],NameForPort)
    elif str(PortNumber[convertFlow]) == '1':
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
        f.write('\n')
        f.write('    1 SetBin SoftBins.b01000000_PASS')
    else:
        MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[TempMainFlow]).replace('___',''))
for xFlow in range(len(TestFlowArrayPath)):
    if xFlow ==0:
        xFlow += 1
    elif (xFlow + 1) < (len(TestFlowArrayPath)):
        # Test Name
        f.write('\n')
        f.write(str(TestFlowArrayName[0].partition(' ')[0]))
        f.write(' ')
        if '.' in TestFlowArrayPath[xFlow]:
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('.','p')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            if '-' in TestFlowArrayPath[xFlow]:
                while '-' in TestFlowArrayPath[xFlow]:
                    TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
                # print(TestFlowArrayPath[xFlow])
        elif '-' in TestFlowArrayPath[xFlow]:
            while '-' in TestFlowArrayPath[xFlow]:
                TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            # print(TestFlowArrayPath[xFlow])
        elif '(' in TestFlowArrayPath[xFlow]:
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('(','_')
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace(')','')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
        else:
            if '-' in TestFlowArrayPath[xFlow]:
                while '-' in TestFlowArrayPath[xFlow]:
                    TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            else:
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
        for convertFlow in range(len(PortNumber)):
            f.write('\n')
            if str(PortNumber[convertFlow]) == '-4': 
                ReturnFlow(PortNumber[convertFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins1(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-3':
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins2(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-2':
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins3(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-1':
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins4(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '0':
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
                NameForPort = str(PortNumberValue[convertFlow]) + str(TestFlowArrayPath[xFlow]).replace('___','')
                f.write('\n')
                Increment(PortNumber[convertFlow],NameForPort)
                f.write('\n')
                SetBins5(PortNumber[convertFlow],NameForPort)
            elif str(PortNumber[convertFlow]) == '1':
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
            else:
                MainFlowContent(PortNumber[convertFlow],str(TestFlowArrayPath[xFlow + TempMainFlow]).replace('___',''))
    else:
        f.write('\n')
        f.write(str(TestFlowArrayName[0].partition(' ')[0]))
        f.write(' ')
        if '.' in TestFlowArrayPath[xFlow]:
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('.','p')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            if '-' in TestFlowArrayPath[xFlow]:
                while '-' in TestFlowArrayPath[xFlow]:
                    TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
                # print(TestFlowArrayPath[xFlow])
        elif '-' in TestFlowArrayPath[xFlow]:
            while '-' in TestFlowArrayPath[xFlow]:
                TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            # print(TestFlowArrayPath[xFlow])
        elif '(' in TestFlowArrayPath[xFlow]:
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('(','_')
            TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace(')','')
            f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
        else:
            if '-' in TestFlowArrayPath[xFlow]:
                while '-' in TestFlowArrayPath[xFlow]:
                    TestFlowArrayPath[xFlow] = str(TestFlowArrayPath[xFlow]).replace('-','_')
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
            else:
                f.write(str(TestFlowArrayPath[xFlow]).replace('___',''))
        for convertFlow in range(len(PortNumber)):
            f.write('\n')
            if str(PortNumber[convertFlow]) == '-4': 
                ReturnFlow(PortNumber[convertFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins1(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-3':
                ReturnFlow(PortNumber[convertFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins2(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-2':
                ReturnFlow(PortNumber[convertFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins3(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '-1':
                ReturnFlow(PortNumber[convertFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],PortNumberValue[convertFlow])
                f.write('\n')
                SetBins4(PortNumber[convertFlow])
            elif str(PortNumber[convertFlow]) == '0':
                ReturnFlow(PortNumber[convertFlow])
                NameForPort = str(PortNumberValue[convertFlow]) + str(TestFlowArrayPath[xFlow])
                f.write('\n')
                Increment(PortNumber[convertFlow],NameForPort)
                f.write('\n')
                SetBins5(PortNumber[convertFlow],NameForPort)
            elif str(PortNumber[convertFlow]) == '1':
                ReturnFlow(PortNumber[convertFlow])
            else:
                ReturnFlow(PortNumber[convertFlow])


f.write('\nFLOW_END')
print('-------')

#####################################################
# Second Step --- Convert .test into final version  #
#####################################################



