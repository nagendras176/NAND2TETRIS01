class Mapper:
    output=''



    def __init__(self,command,status_code,i,file_name):
        self.input=command
        self.in_status=status_code
        self.i=i
        self.file=file_name
    def out(self):

        segment={"local":"LCL","argument":"ARG","this":"THIS","that":"THAT",}
        temp_i=self.i
        if(self.in_status=="null"):

            return "\n"
        if(self.in_status=="MEM"):

            comment="//"+str(self.input[0])+" "+str(self.input[1])+" "+str(self.input[2])+"\n"


            if(self.input[0]=="pop"):
              #pop statement
              if(self.input[1]=="temp"):
                 return(comment+"@SP\nM=M-1\nA=M\nD=M\n@R"+str(5+int(self.input[2]))+"\nM=D\n")
              if(self.input[1]=="static"):
                  return(comment+"@SP\nM=M-1\nA=M\nD=M\n"+"@"+str(self.file+"."+self.input[2])+"\nM=D\n")
              if(self.input[1]=="pointer"):
                  if(self.input[2]=="0"):
                      return(comment+"@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n")
                  else:
                      return(comment+"@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n")
              else:
                 return(comment+"@"+str(self.input[2])+"\n"+"D=A\n@"+str(segment[self.input[1]])+"\n"+"D=M+D\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n")



            else:
              #push statement
              if(self.input[1]=="constant"):
                  return(comment+"@"+str(self.input[2])+"\n"+"D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(self.input[1]=="temp"):

                  return(comment+"@R"+str(5+int(self.input[2]))+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(self.input[1]=="static"):
                    return(comment+"@"+str(self.file+"."+self.input[2])+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(self.input[1]=="pointer"):
                  if(self.input[2]=="0"):
                       return(comment+"@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                  else:
                       return(comment+"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

              else:
                   return(comment+"@"+str(self.input[2])+"\n"+"D=A\n@"+str(segment[self.input[1]])+"\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

        else:
               comment="//"+str(self.input[0])+"\n"
               #add
               if(self.input[0]=="add"):

                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n")
               #sub
               if(self.input[0]=="sub"):

                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n")
               #neg
               if(self.input[0]=="neg"):
                   return(comment+"@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n");
               #and
               if(self.input[0]=="and"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n")
               #or
               if(self.input[0]=="or"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n")
               #not
               if(self.input[0]=="not"):
                   return(comment+"@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n")

               #eq
               if(self.input[0]=="eq"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@eqt"+str(self.i))+"\nD;JEQ\n@neqt"+str(self.i)+"\nD;JNE\n(eqt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(neqt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"
               #gt
               if(self.input[0]=="gt"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@gt"+str(self.i))+"\nD;JGT\n@ngt"+str(self.i)+"\nD;JLE\n(gt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(ngt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"
               #lt
               if(self.input[0]=="lt"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@lt"+str(self.i))+"\nD;JLT\n@nlt"+str(self.i)+"\nD;JGE\n(lt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(nlt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"
     
