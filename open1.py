import re

count = 0
tab = 0

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
for x in range(30):
    count = count + 1

    for line in file_contents:
        if file_contents[count] in line:
            break

    d1 = '<param name="'
    d2 = '" value="'
    d3 = '"/>'
    d4 = '<test name="'
    d5 = '</test>'
    if d4 in line:
        f.write("\n\t{")
        # D4 Start

        # if got test name, tab++
        tab += 1

        variable1 = line.replace(d1, "")
        string = variable1.partition('executionMode="')[-1]
        executionMode = string.replace('">',"")
        executionMode = executionMode.replace("\n","")
        
        # remove executionMode from variable1
        string = variable1.partition('configurable="')[-1]
        temp = '" ' + 'executionMode="' + executionMode + '">'
        string = string.replace(temp, "")
        string = string.replace("\n","")

        configurable = string
        
        # next word "disabled"
        string = variable1.partition('disabled="')[-1]
        temp = '" configurable="' + configurable + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")


        disabled = string

        # next word "type"
        string = variable1.partition('type="')[-1]
        temp = '" disabled="' + disabled + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")


        type = string

        # next word "interactive"
        string = variable1.partition('interactive="')[-1]
        temp = '" type="' + type + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")

        interactive = string

        # next word "destructive"
        string = variable1.partition('destructive="')[-1]
        temp = '" interactive="' + interactive + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")

        destructive = string

        # next word "timeout"
        string = variable1.partition('timeout="')[-1]
        temp = '" destructive="' + destructive + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")

        timeout = string

        # next word "number"
        string = variable1.partition('number="')[-1]
        temp = '" timeout="' + timeout + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")

        number = string

        # next word "binary"
        string = variable1.partition('binary="')[-1]
        temp = '" number="' + number + temp
        string = string.replace(temp, "")
        string = string.replace("\n","")

        binary = string
    
    # end of D4
        dd1 = '<test name="'
        dd2 = '"'
        variable1 = variable1.replace(dd1, "")

        # extract all the value from it
        variable1 = variable1.replace(binary, "")
        variable1 = variable1.replace(number, "")
        variable1 = variable1.replace(timeout, "")
        variable1 = variable1.replace(destructive, "")
        variable1 = variable1.replace(interactive, "")
        variable1 = variable1.replace(type, "")
        variable1 = variable1.replace(disabled, "")
        variable1 = variable1.replace(configurable, "")
        variable1 = variable1.replace(executionMode, "")

        variable1 = variable1.replace(dd2, "")
        variable1 = variable1.replace(" binary=", "")
        variable1 = variable1.replace(" number=", "")
        variable1 = variable1.replace(" timeout=", "")
        variable1 = variable1.replace(" destructive=", "")
        variable1 = variable1.replace(" interactive=", "")
        variable1 = variable1.replace(" type=", "")
        variable1 = variable1.replace(" disabled=", "")
        variable1 = variable1.replace(" configurable=", "")
        variable1 = variable1.replace(" executionMode=", "")
        variable1 = variable1.replace(">", "")
        variable1 = variable1.replace(" ", "")
        if "\n" in variable1:
            variable1 = variable1.replace("\n","")    

        # write into the file
        f.write("\n\t")
        for x in range(tab):
            f.write("\t")
        f.write("Test =")
        f.write(variable1)
        f.write(' ')
        f.write(" binary =")
        f.write(binary)
        f.write('"')
        f.write(' number ="')
        f.write(number)
        f.write('"')
        f.write(' timeout ="')
        f.write(timeout)
        f.write('"')
        f.write(' destructive ="')
        f.write(destructive)
        f.write('"')
        f.write(' interactive ="')
        f.write(interactive)
        f.write('"')
        f.write(' type ="')
        f.write(type)
        f.write('"')
        f.write(' disabled ="')
        f.write(disabled)
        f.write('"')
        f.write(' configurable ="')
        f.write(configurable)
        f.write('"')
        f.write(' executionMode ="')
        f.write(executionMode)
        f.write('";')    
            
    elif d5 in line:
        f.write("\n\t")
        for x in range(tab):
            f.write("\t")
        f.write("Test End")
        f.write("\n\t}")
        tab -= 1
    else:
        variable1 = line.replace(d1, "")
        string = variable1.partition('value="')[-1]
        string = string.replace('"/>',"")
        s1 = "['"
        s2 = "']"
        s3 = "\n"
        # check s1,s2,s3 in word or not
        if s1 in string:
            if s2 in string:
                if s3 in string:
                    string = string.replace(s1,"")
                    string = string.replace(s2,"")
                    string = string.replace(s3, "")
                else:
                    string = string.replace(s1,"")
                    string = string.replace(s2,"")
            
            else:
                string = string.replace(s1,"")
        elif s2 in string:
            if s3 in string:
                string = string.replace(s2,"")
                string = string.replace(s3, "")        
            else:
                string = string.replace(s2,"")        
        elif s3 in string:
            string = string.replace(s3, "")

        variable1 = variable1.replace(string,"")
        variable1 = variable1.replace(d2,"")
        variable1 = variable1.replace(d3,"")
        variable1 = variable1.replace(" ","")
        variable1 = variable1.replace("\n", "")
        # find integer
        result = re.findall(r"[-+]?\d*\.\d+|\d+", variable1)
        result = str(result)
        if result:
            result = result.replace("['","")
            result = result.replace("']", "")

        # write into the file
        f.write("\n\t")
        for x in range(tab):
            f.write("\t")
        f.write(variable1)
        f.write(' ="')
        f.write(string)
        f.write('";')

f.close()

print("All Process Done, Convert Successful!")