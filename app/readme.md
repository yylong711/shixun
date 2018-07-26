### 缓存

- sentence 句子缓存
- keyword  关键字缓存
- select_data 选择的分词器缓存
- 为了翻页功能的pagin缓存

###POST
处理post请求: 传入select_data和post_data
判断 缓存中有没有这两个，如果有且相等的话，session中的keyword
就是想要的值，否则重新连接java服务器请求查询结果
### GET
实现分页功能，如果请求时get判断缓存中是否存在keyword,如果存在的话
，向数据库中进行请求，如何判断向哪个数据库呢?在session中找
select_data的值，如果没有的话，说明session已经过期，或者其他的原因，请重新请求
否则通过session中的select_data和keyword和页号来对数据库进行请求


如果句子内容是已经查询过的话，就把句子内容给记录下来
把分词器的信息记录下来，把keyword的内容记录下来。

关键词直接从key_word中找吧。
把pagin的信息记录下来。。。
对pagin 进行缓存时报错，orm对象禁止作为value值 


## 耗时
两个耗时的点
- get keyword
- 去数据库中查询


#### 任务
将地质类文献和 生物类文献的查询和优化完成
将前端显示页面完成，弄成博客类型的
完成api

