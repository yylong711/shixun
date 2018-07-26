
package org.apdplat.evaluation.impl;

import com.chenlb.mmseg4j.ComplexSeg;
import com.chenlb.mmseg4j.Dictionary;
import com.chenlb.mmseg4j.MMSeg;
import com.chenlb.mmseg4j.MaxWordSeg;
import com.chenlb.mmseg4j.Seg;
import com.chenlb.mmseg4j.SimpleSeg;
import com.chenlb.mmseg4j.Word;
import java.io.IOException;
import java.io.StringReader;
import java.util.*;

import org.apdplat.evaluation.Evaluation;
import org.apdplat.evaluation.EvaluationResult;
import org.apdplat.evaluation.Segmenter;
import org.apdplat.evaluation.WordSegmenter;

/**
 * MMSeg4j分词器分词效果评估
 */
public class MMSeg4jEvaluation extends Evaluation implements WordSegmenter{
    private static final Dictionary DIC = Dictionary.getInstance();
    private static final SimpleSeg SIMPLE_SEG = new SimpleSeg(DIC);
    private static final ComplexSeg COMPLEX_SEG = new ComplexSeg(DIC);
    private static final MaxWordSeg MAX_WORD_SEG = new MaxWordSeg(DIC);
    @Override
    public List<EvaluationResult> run() throws Exception {
        List<EvaluationResult> list = new ArrayList<>();
        
        System.out.println("开始评估 MMSeg4j ComplexSeg");
        list.add(run(COMPLEX_SEG));
        Evaluation.generateReport(list, "MMSeg4j分词器分词效果评估报告.txt");
        
        System.out.println("开始评估 MMSeg4j SimpleSeg");
        list.add(run(SIMPLE_SEG));
        Evaluation.generateReport(list, "MMSeg4j分词器分词效果评估报告.txt");
        
        System.out.println("开始评估 MMSeg4j MaxWordSeg");
        list.add(run(MAX_WORD_SEG));
        Evaluation.generateReport(list, "MMSeg4j分词器分词效果评估报告.txt");
        
        return list;
    }
    private EvaluationResult run(final Seg seg) throws Exception{
        // 对文本进行分词
        String resultText = "temp/result-text-"+seg.getClass().getSimpleName()+".txt";
        float rate = segFile(testText, resultText, new Segmenter(){
            @Override
            public String seg(String text) {
                return segText(text, seg);                
            }
        });
        // 对分词结果进行评估
        EvaluationResult result = evaluate(resultText, standardText);
        result.setAnalyzer("MMSeg4j " + seg.getClass().getSimpleName());
        result.setSegSpeed(rate);
        return result;
    }
    @Override
    public Map<String, String> segMore(String text) {
        Map<String, String> map = new HashMap<>();
        map.put(SIMPLE_SEG.getClass().getSimpleName(), segText(text, SIMPLE_SEG));
        map.put(COMPLEX_SEG.getClass().getSimpleName(), segText(text, COMPLEX_SEG));
        map.put(MAX_WORD_SEG.getClass().getSimpleName(), segText(text, MAX_WORD_SEG));
        return map;
    }
    private String segText(String text, Seg seg) {
        StringBuilder result = new StringBuilder();
        MMSeg mmSeg = new MMSeg(new StringReader(text), seg);        
        try {
            Word word = null;
            while((word=mmSeg.next())!=null) {			
                result.append(word.getString()).append(" ");
            }
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
        return result.toString();
    }
    public static void main(String[] args) throws Exception{
        new MMSeg4jEvaluation().run();
    }
}