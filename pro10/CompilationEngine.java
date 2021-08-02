import java.io.File;
import  java.lang.String;

public class CompilationEngine{

    private static boolean is_jack_file(String str)
    {    
        if((str.substring(str.length()-4,str.length())).equals("jack"))
        {  
            return true;
        }
        return false;
    }

    

    public static void main(String[] args) 
    {
       if(args.length!=1)
        {   System.out.println(args.length);
            System.out.println("INVALID ARGUMENT");
            System.exit(0);
        }
       
       String dir="./"+args[0];

       File inputs=new File(dir);

       boolean is_exists=inputs.exists();
       boolean is_file=inputs.isFile();
      boolean is_directory=inputs.isDirectory();
       
       if(is_exists)
       {
           if(is_file)
           {
               System.out.println(dir+" IS FILE");
           }

           else{
               System.out.println(dir+" IS DIRECTORY");
           }
       }
       
       else{
               System.out.println("NO SUCH FILE/DIRECTORY EXISTS");
       }

       if(is_directory)
       { 
           for(File f:inputs.listFiles())
           {    
               if(is_jack_file(f.getName()))
               {
                   JackTokenizer toc_obj=new JackTokenizer(f);
                   toc_obj.iterate();
               }
           }
       }
    
       

    }
}