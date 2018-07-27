

public class comparision {
    public static float Precision=0;//准确率
    public static float Recall=0;//召回率
    public static float F=0;//F值
    public static int   RANGE=3;//对比范围


    public static void compar(String goldPath,String myPath){
        String[] goldList = new String[]{"a","b","c","d","e","f","g"};
        String[] myList = new String[]{"a","bc","d","e","f","g"} ;

        int correctPos=0;//当前正确的最后一个位置
        int correctCount=0;//黄金集中的匹配正确数量

        for (String currentGold : goldList){
            for (int j=0;j<RANGE;j++){

                System.out.println("gold："+correctPos+"——"+currentGold);
                System.out.println("my："+j+"——"+myList[correctPos+j]);


                if(currentGold.equals(myList[correctPos+j])){
                    correctPos=correctPos+j+1;
                    correctCount++;
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


        System.out.println("正确数： "+correctCount);
        Recall =(float) correctCount / goldList.length;
        Precision = (float) correctCount / myList.length;
        F = (Recall*Precision*2)/(Recall+Precision);





    }


    public static  void main(String args[]){
        String goldPath = "D:\\IDEA\\source\\icwb2-data\\gold\\as_testing_gold.txt" ;
        String myPath   = "D:\\IDEA\\source\\icwb2-data\\testing\\as_test.txt";
        compar(goldPath,myPath);

        System.out.println("召回率： "+Precision);
        System.out.println("准确率:  "+Recall);
        System.out.println("F值：    "+F);

    }

}
