FlowDefs
{	
    TestPlanStartFlow = TestPlanStartFlow;
    TestPlanEndFlow = TestPlanEndFlow;
    LotStartFlow 	= LotStartFlow;
	LotEndFlow 		= LotEndFlow;
	MainFlow = DummyFlow;
	InitFlow = Init_Execute;
}


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




# Array File Name that contains <FileName> Tag
FileName = []

PreHeader_Path = "D:/User/cheelaml/dummy/HDMTOS/TOSReleaseRoot/TOSUserSDK/CalDiag/Common/PreHeaders/"
for filename in os.listdir(PreHeader_Path):
   with open(os.path.join(PreHeader_Path, filename), 'r') as f:
       text = f.read()
       if '<FileName>' in text:
           FileName.append(filename)

# Find bdefs and usrv file
other_file = []

file_path = 'D:/User/cheelaml/dummy/HDMTOS/TAL/CalDiagBase/CalDiagBaseUnitTests/DummyTP/Base/'
TempFileArray = (os.listdir(file_path))
for x in range(len(TempFileArray)):
    if 'bdefs' in TempFileArray[x]:
        other_file.append(TempFileArray[x])
    elif 'usrv' in TempFileArray[x]:
        other_file.append(TempFileArray[x])


my_file = open("D:/User/cheelaml/dummy/HDMTOS/TAL/CalDiagBase/CalDiagBaseUnitTests/DummyTP/dummy.pkg")
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
f = open("D:/User/cheelaml/dummy/HDMTOS/TAL/CalDiagBase/CalDiagBaseUnitTests/DummyTP/Base/dummyTP_base3.tpl", "w")
# write in the version
f.write("Version ")
f.write(ver)
f.write(";\n")

# ProgramStyle
f.write("ProgramStyle = Modular;")





FlowDefs
{	
    TestPlanStartFlow = TestPlanStartFlow;
    TestPlanEndFlow = TestPlanEndFlow;
    LotStartFlow 	= StartLotFlow;
	LotEndFlow 		= EndlotFlow;
	MainFlow = DummyFlow;
	InitFlow = Init_Execute;
}