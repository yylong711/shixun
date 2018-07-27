import com.huaban.analysis.jieba.JiebaSegmenter;

public class testJieba {
    //Index模式
    public static void testIndex(String[] sentences){
        System.out.println("Index方法————————————————————————————————————————————————————————————————————————————————————————————————————————————");
        JiebaSegmenter segmenter = new JiebaSegmenter();

        for (String sentence : sentences) {
            System.out.println("分词前：");
            System.out.println(sentence);

            System.out.println("分词后：");
            System.out.println(segmenter.process(sentence, JiebaSegmenter.SegMode.INDEX).toString());
        }

    }


    //seacrch模式
    public static void testSearch(String[] sentences){
        JiebaSegmenter segmenter = new JiebaSegmenter();
        System.out.println("Search方法————————————————————————————————————————————————————————————————————————————————————————————————————————————");
        for (String sentence : sentences) {
            System.out.println("分词前：");
            System.out.println(sentence);

            System.out.println("分词后：");
            System.out.println(segmenter.process(sentence, JiebaSegmenter.SegMode.SEARCH));
        }
    }


    public static void main(String args[]){
        String[] strs = new String[]{"这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。",
                "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", "结过婚的和尚未结过婚的"};
        testIndex(strs);
        testSearch(strs);

    }



}
