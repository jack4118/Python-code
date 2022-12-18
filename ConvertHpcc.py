from multiprocessing import dummy
import os
from re import X

def TestStart(Name):
    f.write("\n\n")
    f.write('Test ')
    # testfile = str(FileName[CountFile]).replace('.xml','')
    # f.write(testfile)
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

PreHeader_Path = "C:/HPCC/PreHeaders/"
for filename in os.listdir(PreHeader_Path):
   with open(os.path.join(PreHeader_Path, filename), 'r') as f:
       text = f.read()
       if '<FileName>' in text:
           FileName.append(filename)

# Find bdefs and usrv file
other_file = []

file_path = 'C:/HPCC/'
TempFileArray = (os.listdir(file_path))
for x in range(len(TempFileArray)):
    if 'bdefs' in TempFileArray[x]:
        other_file.append(TempFileArray[x])
    elif 'usrv' in TempFileArray[x]:
        other_file.append(TempFileArray[x])

my_file = open("C:/HPCC/hpcc.pkg")
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
f = open("C:/HPCC/HPCC_base.tpl", "w")
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
# for x in range(len(FileName)):
#     f.write("\nImport ")
#     f.write(FileName[x])
#     f.write(';')

# for x in range(len(other_file)):
#     f.write("\nImport ")
#     f.write(other_file[x])
#     f.write(';')

# Array Lists
Total_Device = []
First_Device = []
First_Device_Test = []
First_Device_Value = []
Device_Parameter = []
Parameter_Value = []
Total_Tests = []

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
        # print(line,' line at:', count + 1)
        line = line + ' Status = "Not Yet"'
        Total_Device.append(line + ' Count:' + str(count))
        count += 1
    else:
        count += 1

First_Device.append(Total_Device[0])

temp = ''
# Finish storing Device Array

for line in dummy_contents:
    if 'device' in line:
        temp = line.partition('="')[-1]
        temp = temp.partition('"')[0]
    break
count = 0
FirstDeviceCount = 0
TestCount = 0
for line in dummy_contents:
    if '<device name="' in line:
        if TestCount < 7:
            if TestCount != 0:
                line = line.partition('="')[-1]
                line = line.partition('"')[0]
                # print(line,' at line:', count + 1)
                count += 1
                TestCount += 1
                if First_Device[0] not in line:
                    break
            else:
                line = line.partition('="')[-1]
                line = line.partition('"')[0]
                # print(line,' at line:', count + 1)
                count += 1
                FirstDeviceCount = count
                TestCount += 1
    elif TestCount >= 3:
        break
    else:
        count += 1

# Get the distance count between Device 1 and device 2
TempCount = count
count = 0

for line in dummy_contents:
    if 'param name' in line:
        if count < TempCount:
            line = line.partition('="')[-1]
            line = line.partition('" ')[0]
            First_Device_Test.append(line)
            count += 1
        else:
            break
    else:
        count += 1


count = 0
# get the value for first test
for line in dummy_contents:
    if 'param name' in line:
        if count < TempCount:
            line = line.partition('value="')[-1]
            line = line.partition('"/>')[0]
            while '\n' in line:
                line = line.replace('\n','')
            while ' ' in line:
                line = line.replace(' ','')
            while '\t' in line:
                line = line.replace('\t', '')
            First_Device_Value.append(line)
            count += 1
        else:
            break
    else:
        count += 1

# TestStart(str(First_Device[0]).replace('"',''))
# print(First_Device[0])
# for x in range(len(First_Device_Test)):
#     TestContent(First_Device_Test[x],First_Device_Value[x])

# TestEnd()

# Get the Total Test
count = 0
for line in dummy_contents:
    if '<test name="' in line:
        line = line.partition('="')[-1]
        line = line.partition('binary')[0]
        while '\n' in line:
            line = line.replace('\n','')
        while ' ' in line:
            line = line.replace(' ','')
        while '\t' in line:
            line = line.replace('\t', '')
        Total_Tests.append(line)
        count += 1
    else:
        count += 1

# for x in range(len(Total_Tests)):
#     print(Total_Tests[x])


# Delete the Finished Device
del Total_Device[0]

count = 0
TestCount = 0
for line in dummy_contents:
    if count > FirstDeviceCount:
        if '<device name="' in line:
            if TestCount < 3:
                if TestCount != 0:
                    line = line.partition('="')[-1]
                    line = line.partition('"')[0]
                    # print(line,' at line:', count + 1)
                    count += 1
                    TestCount += 1
                    if Total_Device[0] not in line:
                        break
                else:
                    line = line.partition('="')[-1]
                    line = line.partition('"')[0]
                    # print(line,' at line:', count + 1)
                    count += 1
                    TestCount += 1
        elif TestCount >= 3:
            break
        else:
            count += 1
    else:
        count += 1

TempCount2 = count

count = 0
for line in dummy_contents:
    if count >= TempCount:
        # count += 1
        if '<test' in line:
            # print(line)
            Total_Device[0] = str(Total_Device[0]).replace('Status = "Not Yet"','Status ="Start"')
            count += 1
            break
        else:
            count += 1
    else:
        count += 1

# for x in range(len(Total_Device)):
#     print(Total_Device[x])

count = 0

for line in dummy_contents:
    if 'param name' in line:
        if count > TempCount:
            if count < TempCount2:
                line = line.partition('="')[-1]
                line = line.partition('" ')[0]
                # print(line)
                Device_Parameter.append(line)
                count += 1
            else:
                break
        else:
            count += 1
    else:
        count += 1

count = 0
# get the value for first test
for line in dummy_contents:
    if 'param name' in line:
        if count > TempCount:
            if count < TempCount2:
                line = line.partition('value="')[-1]
                line = line.partition('"/>')[0]
                while '\n' in line:
                    line = line.replace('\n','')
                while ' ' in line:
                    line = line.replace(' ','')
                while '\t' in line:
                    line = line.replace('\t', '')
                Parameter_Value.append(line)
                count += 1
            else:
                break
        else:
            count += 1
    else:
        count += 1

TestStart(str(Total_Tests[0]).replace('"',''))

Total_Tests[0] = str(Total_Tests[0]).replace('Status = "Not Yet"','Status ="Start"')
for x in range(len(First_Device_Test)):
    TestContent(First_Device_Test[x],First_Device_Value[x])

for x in range((1)):
    TestContent(Device_Parameter[x],Parameter_Value[x])

TestEnd()

count = 0
for line in dummy_contents:
    if count > TempCount:
        if '</device>' in line:
            # print(line,' at:', count + 1)
            EndCount = count
            break
        else:
            count += 1
    else:
        count += 1

for x in range(len(Total_Device)):
    if 'Status ="Start"' in Total_Device[x]:
        TempX = x

Total_Device[TempX] = str(Total_Device[TempX]).replace(' Status ="Start"',' Status ="End"')

for x in range(len(Total_Device)):
    if 'Status ="End"' in Total_Device[x]:
        TempX = x
del Total_Device[TempX]

count = 0
for line in dummy_contents:
    if count > TempCount:
        if '</test>' in line:
            Total_Tests[0] = str(Total_Tests[0]).replace(' Status ="Start"',' Status ="End"')
        else:
            count += 1
    else:
        count += 1
for x in range(len(Total_Tests)):
    if 'Status ="End"' in Total_Tests[x]:
        TempX = x
del Total_Tests[TempX]

count = 0
DeviceCount = 0
for line in dummy_contents:
    if count > EndCount:
        if '<device' in line:
            Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
            DeviceCount += 1
        elif '<test' in line:
            break
        else:
            count += 1
    else:
        count += 1


TestStart(str(Total_Tests[0]).replace('"',''))

Device_Parameter = []
Parameter_Value = []

DeviceCount = 0
count = 0
for line in dummy_contents:
    if count >= TempCount2:
        if '<param name="' in line:
            Param = line.partition('="')[-1]
            Param = Param.partition(' value')[0]
            Param = Param.replace('"',' ParamStatus ="Using" Count=' + str(count))
            line = line.replace('value=','vvalue=')
            line = line.partition('value="')[-1]
            line = line.replace('"/>',' ValueStatus ="Using" Count=' + str(count))
            # print(Param,line)
            while '\n' in line:
                line = line.replace('\n','')
            while '\t' in line:
                line = line.replace('\t', '')
            line = 'Variable =' + line
            # print(Param,line)
            Device_Parameter.append(Param)
            Parameter_Value.append(line)
            count += 1
        elif '<device' in line:
            Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
            TempCount2 = count
            DeviceCount += 1
            count += 1
        elif '<test name' in line:
            EndCount = count
            break
        else:
            count += 1
    else:
        count += 1



# Write into file
for x in range(len(First_Device_Test)):
    TestContent(First_Device_Test[x],First_Device_Value[x])

for x in range(len(Device_Parameter)):
    # print(Device_Parameter[x])
    paramx = str(Device_Parameter[x]).partition('ParamStatus')[0]
    paramy = str(Parameter_Value[x]).partition('ValueStatus')[0]
    paramy = paramy.replace('Variable =','')
    TestContent(paramx,paramy)

TestEnd()


# Remove the ending Parameter and Value
count = 0
for line in dummy_contents:
    if count > EndCount:
        if '</device' in line:
            # print(line, count + 1)
            for x in range(len(Total_Device)):
                if 'Status ="Start"' in Total_Device[x]:
                    TempX = x
            Total_Device[TempX] = str(Total_Device[TempX]).replace(' Status ="Start"',' Status ="End"')
            LastDevice = count
            EndCount = count
            break
        else:
            count += 1
    else:
        count += 1

# Delete Array
TempParam = []
TempValue = []
Del_Descending = []

count = 0
for line in dummy_contents:
    if count >= TempCount2:
        if '<param name="' in line:
            Param = line.partition('="')[-1]
            Param = Param.partition(' value')[0]
            Param = Param.replace('"',' ParamStatus ="Using" Count:'+ str(count))
            line = line.replace('value="','vvalue=')
            line = line.partition('value=')[-1]
            line = line.replace('"/>',' ValueStatus ="Using" Count:' + str(count))
            while '\t' in line:
                line = line.replace('\t','')
            while '\n' in line:
                line = line.replace('\n','')
            line = 'Variable =' + line
            TempParam.append(Param)
            TempValue.append(line)
            count += 1
        elif '<device' in line:
            Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
            DeviceCount += 1
            count += 1
        elif '<test name' in line:
            # EndCount = count
            break
        else:
            count += 1
    else:
        count += 1

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


# for x in range(len(Total_Device)):
#     if 'Status ="End"' in Total_Device[x]:
#         TempX = x
#         del Total_Device[TempX]
#     else:
#         break

count = 0
for line in dummy_contents:
    if count > EndCount:
        if'</test>' in line:
            del Total_Tests[0]
            # EndCount = count
            break
        else:
            count += 1
    else:
        count += 1

# for x in range(len(Total_Device)):
#     if 'Status ="End"' in Total_Device[x]:
#         del Total_Device[x]
#         break
for x in range(len(Total_Device)):
    if 'Status ="End"' in Total_Device[x]:
        TempDeviceCount = str(Total_Device[x]).partition('Count:')[-1]
        TempDeviceCount = int(TempDeviceCount)
        break
    else:
        TempDeviceCount = -1
        TempDeviceCount = int(TempDeviceCount)

if TempDeviceCount > -1:
    count = 0
    for line in dummy_contents:
        if count >= int(TempDeviceCount):
            if '<param name="' in line:
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
            # elif '<device' in line:
            #     Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
            #     DeviceCount += 1
            #     count += 1
            elif '<test name' in line:
                # EndCount = count
                break
            else:
                count += 1
        else:
            count += 1

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
    if 'Status ="End"' in Total_Device[x]:
        del Total_Device[x]
        break

print(len(Total_Tests))
for TestConvert in range(203):
# for TestConvert in range(len(Total_Tests) - 1):
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

    # TempEndDeviceCountArray.append(88)
    # print(TempEndDeviceCountArray)
    LatestStartDeviceArray = []
    if (len(TempEndDeviceCountArray)) > 0:
        for x in range(len(Total_Device)):
            if 'Status ="Start"' in Total_Device[x]:
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

    TestStart(str(Total_Tests[0]).replace('"',''))

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
                        Total_Device[DeviceCount] = str(Total_Device[DeviceCount]).replace('Status = "Not Yet"','Status ="Start"')
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

    # print(TempDeviceCountArray)
    for TempDeviceCount in range(len(TempDeviceCountArray)):
        if New_Device == True:
            count = 0
            for line in dummy_contents:
                if (len(TempDeviceCountArray)) > 0:
                    if count > TempDeviceCountArray[0]:
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
                            Device_Parameter.append(Param)
                            Parameter_Value.append(line)
                            count += 1
                        elif '<test name=' in line:
                            break
                        elif '</test>' in line:
                            break
                        elif '</device>' in line:
                            break
                        elif '<device name=' in line:
                            break
                        else:
                            count += 1
                    else:
                        count += 1
            if (len(TempDeviceCountArray)) > 0:
                del TempDeviceCountArray[0]

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
                    Device_Parameter.append(Param)
                    Parameter_Value.append(line)
                    TempParam.append(Param)
                    TempValue.append(line)
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
                else:
                    count += 1
            else:
                count += 1


    # Write into file
    for x in range(len(First_Device_Test)):
        TestContent(First_Device_Test[x],First_Device_Value[x])

    for x in range(len(Device_Parameter)):
        paramx = str(Device_Parameter[x]).partition('ParamStatus')[0]
        paramy = str(Parameter_Value[x]).partition('ValueStatus')[0]
        paramy = paramy.replace('Variable =','')
        TestContent(paramx,paramy)

    TestEnd()

    if Del_Test_Param == True:
        # Remove Value Array
        Del_Descending = []
        for x in range(len(Device_Parameter)):
            for y in range(len(TempParam)):
                if TempParam[y] in Device_Parameter[x]:
                    Del_Descending.append(x)
                    # print(TempParam[y], Device_Parameter[x])

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
            if 'Status ="Start"' in Total_Device[x]:
                y += 1
        for x in range(device_end_count):
            if y >=0 :
                Total_Device[y - 1] = str(Total_Device[y - 1]).replace('Status ="Start"', 'Status ="End"')
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




print('-------')
print('Total Tests:',len(Total_Tests))
print('-------')
print('TempCount',' TempCount2 ','EndCount',' LastDevice',' Last_Device_Count')
# print(TempCount,TempCount2, EndCount, LastDevice, Last_Device_Count)
print(TempCount,TempCount2, EndCount, LastDevice)
for x in range(len(Device_Parameter)):
    print(Device_Parameter[x],Parameter_Value[x])
print('-------')

for x in range(len(Total_Device)):
    print(Total_Device[x])
    
# for x in range(len(Total_Tests)):
#     print(Total_Tests[x])
