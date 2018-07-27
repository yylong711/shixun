import  org.ansj.domain.Result;
import  org.ansj.domain.Term;
import  org.ansj.splitWord.analysis.IndexAnalysis;

import java.util.*;

public class testIndexAnalysis {
    public static void main(String args[]){
        String str ="主副食品";

        Result res = IndexAnalysis.parse(str);


        System.out.println(res.getTerms());


    }

}
