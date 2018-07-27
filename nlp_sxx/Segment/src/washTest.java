import org.nlpcn.commons.lang.occurrence.Count;

import java.io.BufferedReader;

import java.io.File;

import java.io.FileInputStream;

import java.io.FileWriter;

import java.io.IOException;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class washTest {

    /**

     * 功能：Java读取txt文件的内容

     * 步骤：1：先获得文件句柄

     * 2：获得文件句柄当做是输入一个字节码流，需要对这个输入流进行读取

     * 3：读取到输入流后，需要读取生成字节流

     * 4：一行一行的输出。readline()。

     * 备注：需要考虑的是异常情况

     */

    public static int count =52847 ;



    public static void readTxtFile(String filePath){

        try {

            //String encoding="GBK";

            File file=new File(filePath);

            if(file.isFile() && file.exists()){ //判断文件是否存在

                InputStreamReader read = new InputStreamReader(

                        new FileInputStream(file));//考虑到编码格式

                BufferedReader bufferedReader = new BufferedReader(read);

                String lineTxt = null;

                while((lineTxt = bufferedReader.readLine()) != null){
                        //标点
                        lineTxt = lineTxt.replaceAll("\\pP","");
                        //字母
                        lineTxt = lineTxt.replaceAll("\\p{Alpha}","");
                        //空格
//                        lineTxt = lineTxt.replaceAll(" ","");
//                        lineTxt = lineTxt.replaceAll("  ","");
//                        lineTxt = lineTxt.replaceAll("   ","");

                        writeTxtFile(lineTxt);

                     //去掉非结构化的数据

                    //System.out.println(lineTxt);

                }

                read.close();

            }else{

                System.out.println("找不到指定的文件"+filePath);

            }

        } catch (Exception e) {

            System.out.println("读取文件内容出错"+filePath);

            e.printStackTrace();

        }

    }

    public static void writeTxtFile(String txt){

        String writePath = "D:\\IDEA\\source\\geo\\"+"washed-geo"+".txt";
        //test
        //String writePath = "D:\\IDEA\\source\\testResult\\"+count+".txt";

        File file = new File(writePath);

        FileWriter writer;

        try {

            writer = new FileWriter(file, true);

            writer.write(txt);

            writer.write("\r\n");

            writer.close();

        } catch (IOException e) {

            e.printStackTrace();

        }

    }

    public static void main(String args[]){
        String directoryPath="D:\\IDEA\\source\\geo";
        //test
        //String directoryPath="D:\\IDEA\\source\\test";
        List<String> list = new ArrayList<String>();

        File baseFile = new File(directoryPath);
        File[] files = baseFile.listFiles();

        //得到文件夹下的文件
        for (File file : files) {
                list.add(file.getAbsolutePath());
        }



        for(String filePath : list) {


            long current = System.currentTimeMillis();

            readTxtFile(filePath);

            System.out.println(System.currentTimeMillis() - current + "ms" + "————" + filePath+"————"+count);

            count++;
        }
        System.out.println(count);
    }

}