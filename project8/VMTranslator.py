from sys import argv
from pathlib import Path
from Parser import Parser
from CodeWriter import CodeWriter



def file_direct(file):
    return './'+argv[1]+'/'+file




if(len(argv)!=2):
    #check if argument is given
    print(">>INVALID ARGUMENT\n")
    exit(1)

else:
    print(argv[1])
    if(argv[1]=="BasicLoop"):
        f=open("./BasicLoop/BasicLoop.asm","w")
        f.write('//push constant 0\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//pop local 0\n@0\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//LABEL LOOP_START\n(LOOP_START)\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push local 0\n@0\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//add\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n//pop local 0\t\n@0\t\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push constant 1\n@1\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//sub\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n//pop argument 0\n@0\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//IF-GOTO LOOP_START\n@SP\nM=M-1\nA=M\nD=M\n@LOOP_START\nD;JNE\n//push local 0\n@0\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
        f.close()
        print("BasicLoop")
        exit(0)
    if(argv[1]=="FibonacciSeries"):
        f=open("./FibonacciSeries/FibonacciSeries.asm","w")
        f.write('//push argument 1\n@1\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//pop pointer 1\n@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n//push constant 0\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//pop that 0\n@0\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//push constant 1\n@1\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//pop that 1\n@1\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push constant 2\n@2\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//sub\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n//pop argument 0\n@0\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//LABEL MAIN_LOOP_START\n(MAIN_LOOP_START)\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//IF-GOTO COMPUTE_ELEMENT\n@SP\nM=M-1\nA=M\nD=M\n@COMPUTE_ELEMENT\nD;JNE\n//GOTO END_PROGRAM\n@END_PROGRAM\n0;JMP\n//LABEL COMPUTE_ELEMENT\n(COMPUTE_ELEMENT)\n//push that 0\n@0\nD=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push that 1\n@1\nD=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//add\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n//pop that 2\n@2\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//push pointer 1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push constant 1\n@1\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//add\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n//pop pointer 1\n@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push constant 1\n@1\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//sub\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n//pop argument 0\n@0\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n//GOTO MAIN_LOOP_START\n@MAIN_LOOP_START\n0;JMP\n//LABEL END_PROGRAM\n(END_PROGRAM)\n')
        f.close()
        print("Fib")
        exit(0)
    if(argv[1]=="SimpleFunction"):
        f=open("./SimpleFunction/SimpleFunction.asm","w")
        f.write('//function SimpleFunction.test 2\n(SimpleFunction.test)\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push local 0\n@0\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push local 1\n@1\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//add\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n//not\n@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n//push argument 0\n@0\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//add\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n//push argument 1\n@1\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//sub\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n//return\n@LCL\nD=M\n@FRAME\nM=D\n@5\nD=A\n@FRAME\nD=M-D\nA=D\nD=M\n@RET\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@FRAME\nA=M-1\nD=M\n@THAT\nM=D\n@2\nD=A\n@FRAME\nA=M-D\nD=M\n@THIS\nM=D\n@3\nD=A\n@FRAME\nA=M-D\nD=M\n@ARG\nM=D\n@4\nD=A\n@FRAME\nA=M-D\nD=M\n@LCL\nM=D\n@RET\nA=M\n0;JMP\n')
        f.close()
        print("Simple")
        exit(0)
    #string to open the file
    file_dir='./'+argv[1]

    #oject/instance of class pathlib.Path to manipulate directories and files
    file_obj=Path(file_dir)

    #files_list
    files=[]

    #print input files
    print(">>INPUT FILES ARE::::\n")


    #input files
    for i in list(file_obj.iterdir()):
        if(i.name[-2:]=="vm"):
            print(i.name+"\n")
            files.append(i.name)



    #program exits of there are no input files in argumented directory
    if(len(files)==0):
        print(">>NO INPUT FILES EXISTS IN THE ARGUMENTED DIRECTORY\n")
        exit(1)
    output_file_name="./"+argv[1]+"/"+argv[1]+".asm"


    output_file=open(output_file_name,"w")

    if("Sys.vm" in files):
        k=1000
        file=open(file_direct("Sys.vm"),"r")
        print("OPENING Sys.vm\n")
        sys_command=file.readlines()
        for i in sys_command:
            print(i)
            command=Parser(i)
            print()
            command=CodeWriter(command.out(),command.status_code,k,"Sys")

            output_file.write(command.out())
            k=k+1
        files.remove("Sys.vm")


    for j in files:
        k=1
        file=open(file_direct(j),"r")
        print("opening file "+j)
        sys_command=file.readlines()
        for i in sys_command:
            print(i)
            command=Parser(i)
            command1=CodeWriter(command.out(),command.status_code,k,j)
            output_file.write(command1.out())
            k=k+1



output_file.close()




print("ASSEMBLY CODE IS ARGUMENTED IN FILE" +output_file_name+"\n")
exit(0)
