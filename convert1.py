# Start of the Test Function
from ssl import SSLSocket


def TestStart(Name):
    f.write("\n\n")
    f.write("Test ")
    f.write(xml)
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

count = 0

my_file = open("c:/HDMT-AutoConfigure_Diag.pkg")
file_contents = my_file.readlines()

alarm_text = open(r'C:/alarm_text.txt','w')

# Get Version Number
for line in file_contents:
    if "<?xml version=" in line:
        break
    else:
        count += 1

# print("Version found in line: ", count + 1)
d1 = '<?xml version="'
d2 = '"?>'
ver = line.replace(d1, "")
ver = ver.replace(d2, "")
if "\n" in ver:
    ver = ver.replace("\n", "")

# create mtpl file with otpl format
f = open("c:/CurrentClampAlarmTest.mtpl", "w")
# write in the version
f.write("Version ")
f.write(ver)
f.write(";\n")

# ProgramStyle
f.write("ProgramStyle = Modular;")


# TestPlan
# Select AlarmTest as TestPlan
count = 0
for line in file_contents:
    if '<device name="Alarm Test"' in line:
        break
    else:
        count += 1

# print("Line:",line)
Temp = line.partition('" ')[0]
d1 = '<device name="'
TestPlan = Temp.replace(d1,"")
TestPlan = TestPlan.replace(" ","")
# TestPlan Founded

# TestPlan
f.write("\n\nTestPlan ")
f.write(TestPlan)
f.write(';')

# Import
xml = "HvildpsParametricTestClass"
f.write("\n\nImport ")
f.write(xml)
f.write(".xml;")

# Test Counter Definition
# Skip this first

# Test
# print("Current Count at:", count + 1)

TargetCount = count + 1
StartCount = TargetCount
count = 0
# Find end of the targetcount
EndTargetCount = TargetCount
for line in file_contents:
    if count >= EndTargetCount:
        if '</device>' in line:
            break
        else:
            count += 1
    else:
        count += 1
EndTargetCount = count
# print(EndTargetCount + 1)s

count = 0
TestNameArray = [] # use to store all the Test in device
for line in file_contents:
    if count >= TargetCount:
        if '<test name="' in line:
            TestNameArray.append(line)
            count += 1
        elif '</device>' in line:
            break
        elif '</test>' in line:       
            count += 1
        else:
            count += 1
    else:
        count += 1
lenTest = len(TestNameArray) # calculate the legth of the array

count  = 0
EndTest = [] # Store the count when found </test> tag
StartOfTest = 0
for line in file_contents:
    if count >= TargetCount:
        if '<test name="' in line:
            StartOfTest = count
            count += 1
        elif '</device>' in line:
            break
        elif '</test>' in line:
            StartOfTest =  count - StartOfTest - 1
            EndTest.append(StartOfTest)
            count += 1
        else:
            count += 1
    else:
        count += 1
        

# Start DpsAttributes
count = 0
Par = [] # Create Array for parameters
Val = [] # Create Array for parameter's value
p = 0 # Calculate the length of the Array
total_test = 0
tabTest = 0 # tab space purpose
tabDps = 0
tempTab = 0
for line in file_contents:
    if count >= TargetCount:
        if count <= EndTargetCount:
            if '<param name=' in line:
                # TempTest = '<test name="' + TestNameOri
                # if TempTest in line:
                param = line.partition('" ')[0]
                param = param.replace('<param name="', '')
                param = param.replace(' ', '')
                param = param.replace('\n', '')
                if 'TestPoint' in line:
                    if tabDps >= 1:
                        if tempTab <1:
                            param = '\tTestCondition_' + param
                            tabTest = 1
                            tabDps = 0
                            tempTab = 1
                        else:
                            param = 'TestCondition_' + param
                            tabTest = 1
                            tabDps = 0
                            tempTab = 0
                    elif tabDps < 1:
                        param = 'TestCondition_' + param
                        tabTest = 1
                else:
                    if tabTest >= 1:
                        if tempTab < 1:
                            param = '\tDpsAttributes_' + param
                            tabDps = 1
                            tabTest = 0
                            tempTab = 1
                        else:
                            param = 'DpsAttributes_' + param
                            tabDps = 1
                            tabTest = 0
                            tempTab = 0
                    elif tabTest < 1:
                        param = 'DpsAttributes_' + param
                        tabDps = 1

                value = line.partition('value="')[-1]
                value = value.replace('"/>', '')
                value = value.replace(' ', '')
                value = value.replace('\n', '')
                Par.append(param)
                Val.append(value)
                count += 1
                p += 1
            elif '<device name=' in line:
                count += 1
            elif '<test name=' in line:
                count += 1
            elif '</test>' in line:
                count += 1
                
    else:
        count += 1

size = len(Par)

count = 0
paramTest = []
paramCount = 0
arrayTest = []
arrayCount = 0
for line in file_contents:
    if count >= StartCount:
        if count<=EndTargetCount:
            if '<param name="' in line:
                paramCount += 1
                count += 1
            elif '<device name="' in line:
                paramTest.append(paramCount)
                arrayTest.append(arrayCount)
                count += 1
            elif '<test name="' in line:
                paramTest.append(paramCount)
                arrayTest.append(arrayCount)
                count += 1
                arrayCount += 1
            elif '</test>' in line:
                paramTest.append(paramCount)
                arrayTest.append(arrayCount)
                count += 1
            elif '</device>' in line:
                paramTest.append(paramCount)
                arrayTest.append(arrayCount)
                count += 1
    else:
        count += 1


paramValue = 0
ExecutingParam = 0
TestParam = [] # re-store back value
for y in range(len(paramTest)):
    if y >= 1:
        if (paramTest[y]-paramTest[y-1]) > 0:
            if arrayTest[y] == 0:
                # paramValue will be the Array 1
                paramValue = (paramTest[y] + paramTest[y - 1]) - paramTest[y-1]
            elif arrayTest[y] >= 1:
                # print('E->',ExecutingParam,' pV->',paramValue,' pT->',paramTest[y],' aT->',arrayTest[y])
                ExecutingParam = paramValue + (paramTest[y] - paramTest[y - 1])
                arrayTest[y] = -1
            TestParam.append(ExecutingParam)

# for y in range(len(TestParam)):
#     print(TestParam[y])


for TestLoop in range(lenTest): 
    # Extract the TestName
    TestName = str(TestNameArray[TestLoop]).partition('" ')[0]
    TestName = TestName.partition('="')[-1]
    TestNameOri = TestName
    TestName = TestName.replace(" ", "")
    TestExecuting = 0 # Currently Producing <Param> tags
    # Call the writeFunction of test
    TestStart(TestName)
    # Test start
    
    # used Test
    TestNameArray[TestLoop] = str(TestNameArray[TestLoop]).replace('test name','test name used')
    # print('Test 0 ->',TestNameArray[Test])

    # Read xml file
    count = 0
    FileName = "HvildpsParametricTestClass.xml"
    path = "C:/Users/cheelaml/Downloads/CalDiagTestProgram/CalDiag/HVILDPS/PreHeaders/" + FileName
    xmlFile = open(path)

    xmlContents = xmlFile.readlines()
    pattern = '<FileName>'

    for line in xmlContents:
        if pattern in line:
            break
        else:
            count += 1

    FileName2 = line.partition('</FileName>')[0]
    FileName2 = FileName2.replace(pattern,'')
    FileName2 = FileName2.replace('\n','')
    FileName2 = FileName2.replace(' ','')
    # Get File Name

    # path for the FileName
    path2 = 'C:/Users/cheelaml/Downloads/CalDiagTestProgram/CalDiag/preheaders/' + FileName2

    xmlFile2 = open(path2)
    xmlContents2 = xmlFile2.readlines()

    # set count as 0
    count = 0
    for line in xmlContents2:
        if 'Parameter  name="' in line:
            break
        else:
            count += 1

    Parameter = line.partition('" ')[0]
    Parameter = Parameter.replace('<Parameter  name="',"")
    Parameter = Parameter.replace('\n', '')
    Parameter = Parameter.replace(' ', '')

    tempCount = count
    # find the value of Parameter1
    for line in xmlContents2:
        if count >= tempCount:
            if '<Default>' in line:
                break
            else:
                count += 1
        else:
            print("Error")
            break

    value = line.partition('</Default>')[0]
    value = value.replace('<Default>',"")
    value = value.replace('\n', '')
    value = value.replace(' ', '')

    # Write into File
    TestContent(Parameter, value)

    # BoardType
    # set count as 0
    count = 0
    for line in xmlContents:
        if 'Parameter name="' in line:
            break
        else:
            count += 1

    Parameter = line.partition('" ')[0]
    Parameter = Parameter.replace('<Parameter name="',"")
    Parameter = Parameter.replace('\n', '')
    Parameter = Parameter.replace(' ', '')

    tempCount = count

    # find the value of Parameter1
    for line in xmlContents:
        if count >= tempCount:
            if '<Default>' in line:
                break
            else:
                count += 1
        else:
            print("Error")
            break

    value = line.partition('</Default>')[0]
    value = value.replace('<Default>',"")
    value = value.replace('\n', '')
    value = value.replace(' ', '')
    TestContent(Parameter, value)
    BoardType = value

    # TestOperation
    count = 0
    for line in xmlContents:
        if '"TestOperation"' in line:
            break
        else:
            count += 1

    Parameter = line.partition('" ')[0]
    Parameter = Parameter.replace('<Parameter name="',"")
    Parameter = Parameter.replace('\n', '')
    Parameter = Parameter.replace(' ', '')

    tempCount = count
    for line in xmlContents:
        if count >= tempCount:
            if '<TestProgram>' in line:
                break
            else:
                count += 1
        else:
            print("Error")
            break

    value = line.partition('</TestProgram>')[0]
    value = value.replace('<TestProgram>',"")
    value = value.replace('\n', '')
    value = value.replace(' ', '')

    if value == "String":
        value = TestName
    TestContent(Parameter, value)

    # find total test
    test = []
    t = 0 # length of the array
    count = 0
    for line in file_contents:
        if count >= TargetCount:
            if count<= EndTargetCount:
                if '<test name="' in line:
                    # test = line.partition('name="')[-1]
                    line = line.partition('" ')[0]
                    test.append(line)
                    t += 1
                else:
                    count += 1
        else:
            count += 1

    count = 0
    temp = 0
    TempCount = [] # use to store count
    
    for line in file_contents:
        if count >= StartCount:
            if count<=EndTargetCount:
                # check first test
                if '<test name="' in line:
                    TempCount.append(count)
                    count += 1
                    temp += 1
                    break
                else:
                    count += 1
        else:
            count += 1

    pArray = 0
    pVariable = 0
    for i in range(temp):
        if temp >= 1:
            if i < 1:
                p = (TempCount[i] - StartCount)
                pArray = p
                pVariable += 1
        else:
            break
    
    count = 0
    total_test = 0
    i = 0
    pTemp = 0
    for x in range(len(TestNameArray)):
        p = pVariable
        for line in file_contents:
            if total_test == 0:
                if i < pArray:
                    if count >= StartCount:
                        if count<=EndTargetCount: 
                            if 'device name="' in line:
                                count += 1
                                p -= 1
                            elif '<test name="' in line:
                                count += 1
                                i += 1
                                p -= 1
                                pTemp += 1
                            elif '</test>' in line:
                                count += 1
                                i += 1
                                p -= 1
                                pTemp += 1
                            else:
                                TestContent(Par[i], Val[i])
                                i += 1
                                count += 1
                                TestExecuting += 1
                                
                    else:
                        count += 1
                else:
                    total_test += 1
                    TargetCount = count
                    count = 0
                    i -= 1
                    break 
            elif total_test >= 1:
                if i < size:
                    if count >= TargetCount:
                        if count<=EndTargetCount:
                            if 'test name="' in line:
                                count += 1
                                p -= 1
                                pTemp += 1
                            elif '</test>' in line:
                                count += 1
                                p -= 1
                                pTemp += 1
                            else:
                                if 'Used' not in Par[TestExecuting]:
                                    TestContent(Par[TestExecuting], Val[TestExecuting])
                                    # after use, then replace word
                                    Par[TestExecuting] = str(Par[TestExecuting]).replace('Dps','DpsUsed')
                                    if i == (TestParam[x] - 1):
                                        TestParam.remove(TestParam[x])
                                        break
                                    i += 1
                                    count += 1   
                                    TestExecuting += 1
                                else:
                                    TestExecuting += 1
                                    count += 1  
                                    i += 1

                    else:
                        count += 1
                else:
                    total_test += 1
                    break 

    TestEnd()
    print("Finish Convert ",TestName)
