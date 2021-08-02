from Parser import Parser
class CodeWriter:
 def __init__(self,command,STATUS,i,file):
        self.command=command
        self.status=STATUS
        self.i=i
        self.file=file



 def out(self):
   input=self.command


#####################################################################
    #PUSH OR POP
   if(self.status=="POP_PUSH"):
            segment={"local":"LCL","argument":"ARG","this":"THIS","that":"THAT",}
            comment="//"+str(input[0])+" "+str(input[1])+" "+str(input[2])+"\n"


            if(input[0]=="pop"):
              #pop statement
              if(input[1]=="temp"):
                 return(comment+"@SP\nM=M-1\nA=M\nD=M\n@R"+str(5+int(input[2]))+"\nM=D\n")
              if(input[1]=="static"):
                  return(comment+"@SP\nM=M-1\nA=M\nD=M\n"+"@"+str(self.file+"."+input[2])+"\nM=D\n")
              if(input[1]=="pointer"):
                  if(input[2]=="0"):
                      return(comment+"@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n")
                  else:
                      return(comment+"@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n")
              else:
                 return(comment+"@"+str(input[2])+"\n"+"D=A\n@"+str(segment[input[1]])+"\n"+"D=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n")



            else:
              #push statement
              if(input[1]=="constant"):
                  return(comment+"@"+str(input[2])+"\n"+"D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(input[1]=="temp"):

                  return(comment+"@R"+str(5+int(input[2]))+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(input[1]=="static"):
                    return(comment+"@"+str(self.file+"."+input[2])+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
              if(input[1]=="pointer"):
                  if(input[2]=="0"):
                       return(comment+"@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                  else:
                       return(comment+"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

              else:
                   return(comment+"@"+str(input[2])+"\n"+"D=A\n@"+str(segment[input[1]])+"\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")




#######################################################################
    #OPERATION
   if(self.status=="OP"):
               comment="//"+str(input[0])+"\n"
               #add
               if(input[0]=="add"):

                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n")
               #sub
               if(input[0]=="sub"):

                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n")
               #neg
               if(input[0]=="neg"):
                   return(comment+"@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n");
               #and
               if(input[0]=="and"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n")
               #or
               if(input[0]=="or"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n")
               #not
               if(input[0]=="not"):
                   return(comment+"@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n")

               #eq
               if(input[0]=="eq"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@eqt"+str(self.i))+"\nD;JEQ\n@neqt"+str(self.i)+"\nD;JNE\n(eqt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(neqt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"
               #gt
               if(input[0]=="gt"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@gt"+str(self.i))+"\nD;JGT\n@ngt"+str(self.i)+"\nD;JLE\n(gt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(ngt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"
               #lt
               if(input[0]=="lt"):
                   return(comment+"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@lt"+str(self.i))+"\nD;JLT\n@nlt"+str(self.i)+"\nD;JGE\n(lt"+str(self.i)+")\n@SP\nA=M\nM=-1\n@SP\nM=M+1\n@END"+str(self.i)+"\n0;JMP\n(nlt"+str(self.i)+")\n@SP\nA=M\nM=0\n@SP\nM=M+1\n(END"+str(self.i)+")\n"







######################################################################
  #GOTO
   if(self.status=="GOTO"):
              comment="//GOTO "+str(input[1])+"\n"
              return comment+"@"+str(input[1])+"\n0;JMP\n"




########################################################################
#IF-GOTO
   if(self.status=="IF-GOTO"):
            comment="//IF-GOTO "+str(input[1])+"\n"
            return comment+"@SP\nM=M-1\nA=M\nD=M\n@"+input[1]+"\nD;JNE\n"


##############################################################################

   if(self.status=="LABEL"):
           comment="//LABEL "+str(input[1])+"\n"
           return comment+"("+str(input[1])+")\n"






##########################################################################
    #FUNCTION
    #SYS_INIT
   if(self.status=="SYS_INIT"):
          comment="//SYS_INIT\n"

          str1=comment+"@256\nD=A\n@SP\nM=D\n@LCL\nM=-1\n@2\nD=A\n@ARG\nM=-D\n@3\nD=A\n@THIS\nM=-D\n@4\nD=A\n@THAT\nM=-D\n"
          obj=CodeWriter(["call",input[1],input[2]],"CALL","_sys","Sys")
          return str1+obj.out()+"("+input[1]+")\n"






    #PROCEDURES
         # comment="FUNCTION"
   if(self.status=="FUN"):
         comment="//function "+input[1]+" "+input[2]+"\n"
         str1=comment+"("+input[1]+")\n"
         command="@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
         for i in range(0,int(input[2])):
             str1=str1+command
         return str1

################################################################################
    #FUNCTION CALL


   if(self.status=="CALL"):
       comment="//call "+input[1]+" "+input[2]+"\n"
       str1=comment+"@ret_addr."+input[1]+"."+str(self.i)+"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@5\nD=A\n@"+input[2]+"\nD=D+A\n@SP\nD=M-D\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@"+input[1]+"\n0;JMP\n(ret_addr."+input[1]+"."+str(self.i)+")\n"
       return str1





################################################################################
   if(self.status=="RETURN"):

       return "//return\n@LCL\nD=M\n@FRAME\nM=D\n@5\nD=A\n@FRAME\nD=M-D\nA=D\nD=M\n@RET\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@FRAME\nA=M-1\nD=M\n@THAT\nM=D\n@2\nD=A\n@FRAME\nA=M-D\nD=M\n@THIS\nM=D\n@3\nD=A\n@FRAME\nA=M-D\nD=M\n@ARG\nM=D\n@4\nD=A\n@FRAME\nA=M-D\nD=M\n@LCL\nM=D\n@RET\nA=M\n0;JMP\n"
#######################################################################
      #NULL
   if(self.status=="NULL"):
          return ''
