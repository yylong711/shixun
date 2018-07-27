import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class stringReplace
{
    public static void main(String args[]){
        String directoryPath="D:\\IDEA\\source\\test";
        List<String> list = new ArrayList<String>();

        File baseFile = new File(directoryPath);
        File[] files = baseFile.listFiles();

        //得到文件夹下的文件
        for (File file : files) {
            list.add(file.getAbsolutePath());
        }



        for(String filePath : list) {


            System.out.println(filePath);

        }
    }
}
