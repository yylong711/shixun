
package org.apdplat.evaluation.impl;

import com.huaban.analysis.jieba.JiebaSegmenter;
import com.huaban.analysis.jieba.JiebaSegmenter.SegMode;
import com.huaban.analysis.jieba.SegToken;

import java.util.*;

import org.apdplat.evaluation.Evaluation;
import org.apdplat.evaluation.EvaluationResult;
import org.apdplat.evaluation.Segmenter;
import org.apdplat.evaluation.WordSegmenter;

/**
 * Jieba分词器分词效果评估
 *  */
public class JiebaEvaluation extends Evaluation implements WordSegmenter{
    private static final JiebaSegmenter JIEBA_SEGMENTER = new JiebaSegmenter();
    @Override
    public List<EvaluationResult> run() throws Exception {
        List<EvaluationResult> list = new ArrayList<>();
        
        System.out.println("开始评估 Jieba "+SegMode.INDEX);
        list.add(run(SegMode.INDEX));
        Evaluation.generateReport(list, "Jieba分词器分词效果评估报告.txt");
        
        System.out.println("开始评估 Jieba "+SegMode.SEARCH);
        list.add(run(SegMode.SEARCH));
        Evaluation.generateReport(list, "Jieba分词器分词效果评估报告.txt");
        
        return list;
    }
    private EvaluationResult run(final SegMode segMode) throws Exception{
        // 对文本进行分词
        String resultText = "temp/result-text-"+segMode+".txt";
        float rate = segFile(testText, resultText, new Segmenter(){
            @Override
            public String seg(String text) {
                return JiebaEvaluation.seg(text, segMode);
            }
        });
        // 对分词结果进行评估
        EvaluationResult result = evaluate(resultText, standardText);
        result.setAnalyzer("Jieba "+segMode);
        result.setSegSpeed(rate);
        return result;
    }
    @Override
    public Map<String, String> segMore(String text) {
        Map<String, String> map = new HashMap<>();
        map.put("INDEX", seg(text, SegMode.INDEX));
        map.put("SEARCH", seg(text, SegMode.SEARCH));
        return map;
    }
    private static String seg(String text, SegMode segMode) {
        StringBuilder result = new StringBuilder();
        for(SegToken token : JIEBA_SEGMENTER.process(text, segMode)){
            result.append(token.word.getToken()).append(" ");
        }
        return result.toString();
    }
    public static void main(String[] args) throws Exception{
        new JiebaEvaluation().run();
    }
}