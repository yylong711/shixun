
package org.apdplat.evaluation.impl;

import edu.fudan.nlp.cn.tag.CWSTagger;

import java.util.*;

import org.apdplat.evaluation.Evaluation;
import org.apdplat.evaluation.EvaluationResult;
import org.apdplat.evaluation.Segmenter;
import org.apdplat.evaluation.WordSegmenter;

/**
 * FudanNLP分词器分词效果评估
 */
public class FudanNLPEvaluation extends Evaluation implements WordSegmenter{
    private static CWSTagger tagger = null;
    static{
        try{
            tagger = new CWSTagger("lib/fudan/fudannlp/1.6.1/fudannlp_seg.m");
            tagger.setEnFilter(true);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    @Override
    public List<EvaluationResult> run() throws Exception {
        List<EvaluationResult> list = new ArrayList<>();
        
        System.out.println("开始评估 FudanNLP");
        list.add(run(tagger));
        
        Evaluation.generateReport(list, "FudanNLP分词器分词效果评估报告.txt");
        
        return list;
    }
    private EvaluationResult run(final CWSTagger tagger) throws Exception{
        // 对文本进行分词
        String resultText = "temp/result-text-FudanNLP.txt";
        float rate = segFile(testText, resultText, new Segmenter(){
            @Override
            public String seg(String text) {
                return tagger.tag(text);                
            }
        });
        // 对分词结果进行评估
        EvaluationResult result = evaluate(resultText, standardText);
        result.setAnalyzer("FudanNLP");
        result.setSegSpeed(rate);
        return result;
    }
    @Override
    public Map<String, String> segMore(String text) {
        Map<String, String> map = new HashMap<>();
        map.put("FudanNLP", tagger.tag(text));
        return map;
    }
    public static void main(String[] args) throws Exception{
        new FudanNLPEvaluation().run();
    }
}