
package org.apdplat.evaluation.impl;

import java.util.*;

import org.apdplat.evaluation.Evaluation;
import org.apdplat.evaluation.EvaluationResult;
import org.apdplat.word.WordSegmenter;
import org.apdplat.word.segmentation.SegmentationAlgorithm;

/**
 * word分词器分词效果评估
 */
public class WordEvaluation extends Evaluation implements org.apdplat.evaluation.WordSegmenter{
    @Override
    public List<EvaluationResult> run() throws Exception {
        List<EvaluationResult> list = new ArrayList<>();
        for(SegmentationAlgorithm segmentationAlgorithm : SegmentationAlgorithm.values()){
            System.out.println("开始评估 word分词 "+segmentationAlgorithm.getDes());
            list.add(run(segmentationAlgorithm));
            //每评估完一种算法就保存一次报告
            Evaluation.generateReport(list, "word分词器分词效果评估报告.txt");
        }
        return list;
    }
    private EvaluationResult run(SegmentationAlgorithm segmentationAlgorithm) throws Exception{
        //对文本进行分词
        String resultText = "temp/result-text-"+segmentationAlgorithm.name()+".txt";
        float rate = segFile(testText, resultText, text -> WordEvaluation.seg(text, segmentationAlgorithm));
        //对分词结果进行评估
        EvaluationResult evaluationResult = evaluate(resultText, standardText);
        evaluationResult.setAnalyzer("word分词 "+segmentationAlgorithm.getDes());
        evaluationResult.setSegSpeed(rate);
        return evaluationResult;
    }
    @Override
    public Map<String, String> segMore(String text) {
        Map<String, String> map = new HashMap<>();
        for(SegmentationAlgorithm segmentationAlgorithm : SegmentationAlgorithm.values()){
            map.put(segmentationAlgorithm.getDes(), seg(text, segmentationAlgorithm));
        }
        return map;
    }
    private static String seg(String text, SegmentationAlgorithm segmentationAlgorithm) {
        StringBuilder result = new StringBuilder();
        WordSegmenter.segWithStopWords(text, segmentationAlgorithm)
                .stream()
                .forEach(word -> result.append(word.getText()).append(" "));
        return result.toString();
    }
    public static void main(String[] args) throws Exception{
        new WordEvaluation().run();
    }
}