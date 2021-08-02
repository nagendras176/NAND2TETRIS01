from sys import argv
from Parser import Parser
from Mapper import Mapper

if(len(argv)==2):
    print("opening file %s"%(argv[1]))
    file=open(argv[1],'r')
    output_file=argv[1][:-3]+".asm"
    write_line=open(output_file,'w')
    commands=file.readlines();
    j=0
    #print(commands)
    #for i in commands:
    #    print(i)
    for i in commands:
        parse_str=Parser(i[:-1])

        res=Mapper(parse_str.out(),parse_str.status_code,j,argv[1][-3])

        write_line.write(res.out())
        j=j+1
    write_line.close()

else:
    print("invalid argument\n")
