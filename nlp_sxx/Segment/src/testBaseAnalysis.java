import org.ansj.domain.Term;
import org.ansj.domain.Result;
import org.ansj.splitWord.analysis.BaseAnalysis;

import java.util.*;

public class testBaseAnalysis {
    public static void main(String arg[]){

        String str = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作";

        Result res = BaseAnalysis.parse(str);

        List<Term> parse = res.getTerms();
        System.out.println(parse);
    }

}
