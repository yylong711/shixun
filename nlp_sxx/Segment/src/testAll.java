import java.io.IOException;

public class testAll {
    public static  void main(String args[]) {
        String[] str = new String[]{"这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。", "我不喜欢日本和服。", "雷猴回归人间。",
                "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", "结过婚的和尚未结过婚的"};
        try {
            //ansj
            firstAnsj.testBaseAnalysis(str);
            firstAnsj.testIndexAnalysis(str);
            firstAnsj.testNLPAnalysis(str);
            firstAnsj.testToAnalysis(str);

            //IK
            testIKAnalyzer.testRefineAnalysis(str);
            testIKAnalyzer.testSmartAnalysis(str);

            //Jie
            testJieba.testSearch(str);
            testJieba.testIndex(str);
        }catch (IOException io){
            io.printStackTrace();
        }
    }
}
