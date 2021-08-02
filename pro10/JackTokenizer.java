import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
public class JackTokenizer{
    private File file;
    JackTokenizer(File file)
    {
        this.file=file;
    }

    public void extract_tokens()
    {  try{
        Scanner lines=new Scanner(this.file);
    
    
        while(lines.hasNextLine())
        {
           System.out.println(lines.nextLine());      
        }

    }
    catch(FileNotFoundException e){
        System.out.println(e);
    }
    }


}