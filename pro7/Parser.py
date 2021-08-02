class Parser:

    def __init__(self,command):
        self.com=command
        print(self.com)
    def out(self):
        if(len(self.com)!=0):
            if(self.com[0]=='/'):
                 self.status_code="NULL"
                 return '\0'
        if(len(self.com)==0):
              self.status_code="NULL"
              return '\0'

        ls=self.com.split(' ')
        if(len(ls)==1):
            self.status_code="OP"
            return ls
        else:
            self.status_code="MEM"
            return ls
