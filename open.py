import re

count = 0

my_file = open("c:/HDMT-AutoConfigure_Diag.pkg")
file_contents = my_file.readlines()

alarm_text = open(r'C:/alarm_text.txt','w')

#find "Current Clamp Alarm Test" , once find, then break
find = "Current Clamp Alarm Test"

for line in file_contents:
    if find in line:
        break
    else:
        count = count + 1

DisCount = count + 1
# print("Founded word in line = ", DisCount)
# print("Word before delete : ")
# print(line)

# clear the unnecessary words from the result
d1 = '        <device name="'
d2 = ' (Single Rail)" binary="" timeout="60" configurable="no" executionMode="local">'
line = line.replace(d1, "")
line = line.replace(d2, "")


# print("Word after delete :")
# remove any space from it
line = re.sub(r"\s+", "", line)
# print(line)

# create mtpl file with otpl format
f = open("c:/CurrentClampAlarmTest.mtpl", "w")
f.write("Test HvildpsParametricTestClass ")
f.write(line)
f.write("\n{")

#next word processing
for x in range(5):
    count = count + 1

    for line in file_contents:
        if file_contents[count] in line:
            break

    d1 = '<param name="'
    d2 = '" value="'
    d3 = '"/>'
    variable1 = line.replace(d1, "")
    variable1 = variable1.replace(d2,"")
    variable1 = variable1.replace(d3,"")
    variable1 = variable1.replace(" ","")
    variable1 = variable1.replace("\n", "")
    

    # variable2 = ""
    
    # for m in variable1:
    #     if m.isdigit():
    #         variable2 = variable2 + m
    # print("Find numbers from string:",variable2) 

    result = re.findall(r"[-+]?\d*\.\d+|\d+", variable1)
    result = str(result)
    result = result.replace("['","")
    result = result.replace("']", "")

    print(variable1)
    print(result)
    if str(result) in variable1:
        print("Found!")
    else:
        print("not found!")
    
    variable1 = variable1.replace(result,"")
    print("After work: ", variable1)

    # write into the file
    f.write("\n\t")
    f.write(variable1)
    f.write(' ="')
    f.write(result)
    f.write('";')

f.close()

print("Process done.")