import os.path
from os import path

old = "sub_80020400"
new = "GCL_Cmd_Return_80020400"

def FixFileContent(fileName, old, new):
    with open(fileName,'r') as f:
        newlines = []
        for line in f.readlines():
            newlines.append(line.replace(old, new))

    with open(fileName, 'w') as f:
        for line in newlines:
            f.write(line)
        
if path.exists("..\\asm\\" + old + ".s"):
    os.rename("..\\asm\\" + old + ".s", "..\\asm\\" + new + ".s")
    FixFileContent("..\\asm\\" + new + ".s", old, new)
    FixFileContent("..\\build\\linker_command_file.txt", old, new)
else:
    print "Couldn't find ..\\asm\\" + old + ".s"
    
