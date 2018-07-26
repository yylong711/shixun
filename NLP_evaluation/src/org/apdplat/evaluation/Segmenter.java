

package org.apdplat.evaluation;

/**
 * 对文本进行分词的接口
 */
public interface Segmenter {
    /**
     * 对文本进行分词，词之间以空格分隔
     * @param text 文本
     * @return 分词后的文本
     */
    public String seg(String text);
}
