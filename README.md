What, what is this?

This project aims to completely reverse engineer Metal Gear Solid for PlayStation back to C source code which when compiled produces the same assembly code.

How to build.

1.	Clone down this repo.
2.	Clone down the PSYQ SDK repo from: https://github.com/FoxdieTeam/psyq_sdk.git
3.	Open this repo in VS code or whatever editor you like to use.
4.	Open a powershell window and cd into the build directory.
5.	To build issue the command “powershell -File .\build.ps1 -psyq_path4dot4 C:\path_to\psyq_repo\psyq_4.4\bin -psyq_path4dot3  C:\path_to\psyq_repo\psyq_4.3\bin”
6.	At the end you should see an “OK” confirming that the built binaries hash matches the original games binary hash.

How to decompile a function.

Using IDA or Ghidra disassemble the original game binary, or use one that you compiled yourself provided that the output was OK. Now choose a .s file from the asm directory where that function isn’t part of the “mts” system and also isn’t part of “psyq”.
Given the address of the function go to this location in your reversing tool. Delete the .s file and create a .c file. In the .c file write a function with the same name as the file and build. The build will not be OK as your empty function will no longer build a matching binary.
Now comes the hard part, implement the function such that it matches the functionality of the assembly and build again. Repeat this until your build is OK – i.e your C code is functionally the same and produces exactly the same assembly as the original function.
To diff the original assembly VS your assembly you can use the “mdasm” tool from: https://github.com/FoxdieTeam/mdasm.git and edit build.ps1 to pass mdasm.exe the correct file start and end offset for the function you are working on. You can find these offsets in build\function_offsets.txt

Help I am totally stuck?

Join our discord here https://discord.gg/tTvhQ8w and ask for help in #metal_gear_dev
