# 基于NLP的垂直领域智能问答系统研究与实现
### 开发技术
- mysql 数据库
- python 3.6  (requirement文件中有包含的包)
- java 8
- flask web框架 + bootstrap css 框架
- memcached 缓存



## 实现内容
- 对分词器性能的比较
- 实现了4种分词器模型
- 针对电商领域的智能问答
- 针对专业领域的垂直搜索


## 内容删除
因为内容太大，对处理过的文本文件进行删除
### jieba分词/cut_data
#### 内容
- jieba分词/cut_data/abstruct_word_by_format 对摘要的提取和分割
- jieba分词/cut_data/text_word_by_format和专业文献paper内容的语句分割和词语分割


- tf_idf/model
model为针对四种分词器和三种数据模型的 12个tf-idf model
可以通过 util函数中的train_model函数来进行输出模型，训练源数据为
分词的结果
















