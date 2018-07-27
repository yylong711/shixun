
import jdk.internal.org.objectweb.asm.tree.analysis.Analyzer;
import org.wltea.analyzer.core.IKSegmenter;
import org.wltea.analyzer.lucene.IKAnalyzer;
import java.io.StringReader;

import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;
import org.wltea.analyzer.lucene.IKAnalyzer;
import java.io.IOException;
import java.util.*;

public class testIKAnalyzer {
     public static void testRefineAnalysis(String[] str)throws IOException{
         System.out.println("——————Refine分词后：——————");
         for (String sentence : str) {

             IKSegmenter analyzer = new IKSegmenter(new StringReader(sentence), false);
             while (analyzer.next() != null) {
                 System.out.println(analyzer.next());
             }
         }
     }

     public static void testSmartAnalysis(String[] str) throws  IOException {
         System.out.println("——————Smart分词后：——————");
         for (String sentence : str) {

             IKSegmenter analyzer = new IKSegmenter(new StringReader(sentence), true);
             while (analyzer.next() != null) {
                 System.out.println(analyzer.next().toString());

             }
         }
     }

    public static void main(String args[]){
        String[] str = {"这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。","工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"};
        System.out.println("原句："+str);

        try{
            testRefineAnalysis(str);
            testSmartAnalysis(str);
        }catch (Exception io){
            System.out.println(io.getCause());
        }

    }



}
