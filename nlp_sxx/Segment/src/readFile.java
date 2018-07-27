import java.io.*;


public class readFile {

    public static float Precision=0;//准确率
    public static float Recall=0;//召回率
    public static float F=0;//F值
    public static float corectNum=0;//正确总数
    public static float allGoldNum=0;//标准集总词数
    public static float allMyNum=0;//对比集总词数



    public static void readTxtFile(String goldFilePath,String myFilePath){
        //文件按行读取
        try {

            //String encoding="GBK";

            File goldFile=new File(goldFilePath);
            File myFile=new File(myFilePath);


            if(goldFile.isFile() && goldFile.exists()&&myFile.isFile() && myFile.exists()){ //判断两个文件是否存在

                InputStreamReader read1 = new InputStreamReader(new FileInputStream(goldFile));//考虑到编码格式
                InputStreamReader read2 = new InputStreamReader(new FileInputStream(myFile));//同上

                BufferedReader goldBufferedReader = new BufferedReader(read1);
                BufferedReader myBufferedReader = new BufferedReader(read2);

                String goldLineTxt = null;
                String myLineTxt = null;

                while(((goldLineTxt = goldBufferedReader.readLine()) != null) && (myLineTxt = myBufferedReader.readLine()) != null){

                    //System.out.println("1111————"+goldLineTxt);
                    //System.out.println("2222————"+myLineTxt);

                    compar(goldLineTxt,myLineTxt);


                }

                read1.close();
                read2.close();

            }else{

                System.out.println("找不到指定的文件"+goldFilePath);

            }

        } catch (Exception e) {

            //System.out.println("读取文件内容出错"+goldFilePath);

            e.printStackTrace();

        }


        Recall =(float) corectNum / allGoldNum;
        Precision = (float) corectNum / allMyNum;
        F = (Recall*Precision*2)/(Recall+Precision);


    }





    public static void compar(String goldString,String myString){
        int   RANGE=3;//对比范围
        String[] goldList = goldString.split("\\s+");
        String[] myList = myString.split("\\s+");

        allGoldNum = allGoldNum+goldList.length;
        allMyNum = allMyNum+myList.length;


        int correctPos=0;//当前正确的最后一个位置
        //int correctCount=0;//黄金集中的匹配正确数量

        for (String currentGold : goldList){

            for (int j=0;j<RANGE;j++){
                if(correctPos+j>myList.length){
                    RANGE=3;
                    break;
                }

                //System.out.println("gold："+currentGold);
                //System.out.println("my："+myList[correctPos+j]);



                if(currentGold.equals(myList[correctPos+j])){
                    correctPos=correctPos+j+1;
                    corectNum++;
                    RANGE=3;//搜范围归为初始值
                    break;
                }else {
                    if (j==RANGE-1){
                        RANGE++;
                        break;
                    }
                }
            }

        }


    }


    public static void main(String arg[]) {
        String goldPath = "D:\\IDEA\\source\\test\\0.txt";
        String myPath = "D:\\IDEA\\source\\test\\0original.txt";
        readTxtFile(goldPath,myPath);

       // System.out.println("正确数： "+corectNum);
        //System.out.println("召回率： "+Precision);
        //System.out.println("准确率:  "+Recall);
        //System.out.println("F值：    "+F);
    }
}
