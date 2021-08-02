class Parser:
    status_code=''
    def __init__(self,command):
        self.com=command


    def filter_line(self,str):
       #function to remove comment and new line charater
       return (str.split('//')[0]).split('\n')[0].split(' ')

    def out(self):
        out=self.filter_line(self.com)




        if(out[0] in ["add","sub","neg","and","or","not","eq","gt","lt"]):
            self.status_code="OP"
            return out
        #parsing push or pop
        elif(out[0]=="push" or out[0]=="pop"):
            self.status_code="POP_PUSH"
            return out
        elif(out[0]=="function"):
            if(out[1]=="Sys.init"):
               self.status_code="SYS_INIT"
               return out
            else:
               self.status_code="FUN"
               return out
        elif(out[0]=="call"):
            self.status_code="CALL"
            return out
        elif(out[0]=="if-goto"):
            self.status_code="IF-GOTO"
            return out
        elif(out[0]=="goto"):
            self.status_code="GOTO"
            return out
        elif(out[0]=="label"):
            self.status_code="LABEL"
            return out
        elif(out[0]=="return"):
            self.status_code="RETURN"
            return out
        else:

            self.status_code="NULL"
            return out
