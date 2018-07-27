import org.ansj.domain.Result;
import org.ansj.domain.Term;
import org.ansj.splitWord.analysis.*;

import  java.util.*;



public class firstAnsj {
    public  static void testToAnalysis(String[] str){
        //关注以下词性的词
        Set<String> expectedNature = new HashSet<String>()
        {{
            add("n");add("v");add("vd");add("vn");
            add("vx");add("vi");add("vl");add("vg");
            add("nt");add("nz");add("nw");add("nl");
            add("ng");add("userDefine");add("wh");
        }} ;
//
//        System.out.println("Start");
//
//        System.out.println(ToAnalysis.parse(str));
//
//        Result res = ToAnalysis.parse(str);
//        System.out.println(res.getTerms());
//
//        List<Term> terms = res.getTerms();
//        System.out.println(terms.size());
//
//        for(int i = 0;i<terms.size();i++ ){
//            String word = terms.get(i).getName();//词
//            String natureStr = terms.get(i).getNatureStr();//词性
//            if(expectedNature.contains(natureStr)){
//                System.out.println(word+" : "+natureStr);
//            }
//        }
        System.out.println("——————ToAnalysis——————");
        for (String sentence : str) {


            Result res = ToAnalysis.parse(sentence);

            List<Term> parse = res.getTerms();
            System.out.println(parse);
        }
    }


    public static void testBaseAnalysis(String[] str){
        System.out.println("——————BaseAnalysis——————");
        for (String sentence : str) {

            Result res = BaseAnalysis.parse(sentence);

            List<Term> parse = res.getTerms();
            System.out.println(parse);
        }
    }

    public static void testNLPAnalysis(String[] str){
        System.out.println("——————NLPAnalysis——————");
        for (String sentence : str) {

            Result res = NlpAnalysis.parse(sentence);

            List<Term> parse = res.getTerms();
            System.out.println(parse);
        }
    }

    public static void testIndexAnalysis(String[] str){
        System.out.println("——————IndexAnalysis——————");
        for (String sentence : str) {

            Result res = IndexAnalysis.parse(sentence);

            List<Term> parse = res.getTerms();
            System.out.println(parse);
        }
    }


    public static void testDicAnalysis(String[] str){
        System.out.println("——————IndexAnalysis——————");
        for (String sentence : str) {

            Result res = DicAnalysis.parse(sentence);

            List<Term> parse = res.getTerms();
            System.out.println(parse);
        }
    }

    public static void main(String args[]){
        String[] str = {"工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
                ,"这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。"};
        testBaseAnalysis(str);
        testIndexAnalysis(str);
        testNLPAnalysis(str);
        testToAnalysis(str);
        testDicAnalysis(str);
    }




}
