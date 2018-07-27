import org.ansj.domain.Result;
import  org.ansj.domain.Term;
import org.ansj.splitWord.analysis.NlpAnalysis;

import java.util.*;

public class testNlpAnalysis {



    public static  void main(String arg[]) {
        String str = "洁面仪配合洁面深层清洁毛孔 清洁鼻孔面膜碎觉使劲挤才能出一点点皱纹 脸颊毛孔修复的看不见啦 草莓鼻历史遗留问题没辙 脸和脖子差不多颜色的皮肤才是健康的 长期使用安全健康的比同龄人显小五到十岁 28岁的妹子看看你们的鱼尾纹";

        Result res = NlpAnalysis.parse(str);

        List<Term> parse = res.getTerms();
        System.out.println(parse);
    }


}
