from flask import session
from jieba分词.Config import sege_dict
from .client import Client
from tf_idf.utils import find_the_better_word
from sklearn.externals import joblib
from flask_sqlalchemy import BaseQuery
from flask import flash

from emotion_analyze.train import SentimentClassifier

# 通过 编号和 sentence内容 和查询类型 得到pagin对象
def get_result(select_data, sentence_data, type, is_abstruct):
    '''
    :param select_data:int 1 2 3 4
    :param sentence_data:
    :param type 1jd 2bio  3geo
    :param is_abstruct 1 ,0, 2 适用于paper类型的关键词查找数据库为

    :return: ordered pagin result
    查询结果的缓存放一放
    '''
    #  1 代表 范围匹配 当不为1时数据库*2
    if is_abstruct != '1':
        table_num = type + select_data * 2
    else:
        table_num = type + select_data
    # print('select_data is'.format(select_data))
    key_list = None
    type_name = sege_dict.get(type)
    model_name = '{}_{}_tf.model'.format(type_name, select_data)
    vectorize_name = '{}_{}_vectorize.model'.format(type_name, select_data)
    # load the special model
    model, vectorize = load_model(model_name, vectorize_name)
    # get key word from session
    if session.get('table_num') == select_data and session.get('sentence_data') == sentence_data:
        if session.get('key_list'):
            key_list = session.get('key_list')
            print('从缓存中取得keylist{}'.format(key_list))
    else:
        print('请求的到的key_list')
        word_list = request_to_server(select_data, sentence_data)
        # find key_list by ftf-
        key_list = find_the_better_word(word_list, model, vectorize)
        session['key_list'] = key_list
        flash('关键词为:{}'.format(key_list))
        print('关键词为:{}'.format(key_list))

        session['table_num'] = table_num
        session['sentence_data'] = sentence_data

    # 根据选择的分词器找到对应的数据库
    table = sege_dict.get(table_num)
    # jd类数据
    if type == '1':
        pagin_data = find_result_in_db(key_list, table, model, vectorize, is_sort=0)
    else:
        # is_sort  1 代表着杰拉德系数的排序
        pagin_data = find_result_in_db(key_list, table, model, vectorize, is_sort=1, type=type, is_abstruct=is_abstruct)

    return pagin_data


def load_model(model_name, vectorize_name):
    full_model_path = '/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/tf_idf/model/{}'.format(model_name)
    full_vectorize_path = '/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/tf_idf/model/{}'.format(
        vectorize_name)
    model = joblib.load(full_model_path)
    vectorize = joblib.load(full_vectorize_path)
    # print('model and vectorize{}'.format(model,vectorize))
    return model, vectorize


# 增加对结果的排序功能 根据tf-idf
# 既需要is_sort 和is_type的原因是  对于范围匹配和 全文匹配 需要tf-idf 全文匹配同时需要2方法
def find_result_in_db(keylist, table, model, vectorsize, is_sort=1, type='1', is_abstruct='1'):
    results = []
    for key in keylist:
        result = table.query.filter(table.content == key).limit(50).all()
        # print(type(result))
        results.extend(result)
    # is_sort 代表是文献类数据
    if is_sort == 1:
        if is_abstruct == '1':
            paper_set = [each.paper for each in results]
            sorted_paper = sort_by_word_tfidf(keylist, paper_set, model, vectorsize)
            print(sorted_paper)

            # 全文匹配
        elif is_abstruct == '0':
            paper_set = [each.sentence.paper for each in results]
            sorted_paper = sort_by_word_tfidf(keylist, paper_set, model, vectorsize)
        # key匹配
        else:
            paper_set = [each.sentence.paper for each in results]
            sorted_paper = sort_by_keyword(keylist, paper_set, type=type)
    # is_sort not 1 代表不为1 不做处理
    else:
        new_list = []
        for each in results:
            if each.sentence not in new_list:
                new_list.append(each.sentence)
        sorted_paper = new_list
    return sorted_paper[:30]

# 去除重复的List 在不改变顺序情况下
def de_repetition(results):
    new_list = []
    for each in results:
        if each not in new_list:
            new_list.append(each)
    return new_list
def find_type(key_list, type):
    if type == '2':
        opener = open('/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/app/main/csv/bio.csv', 'r')
    elif type == '3':
        opener = open('/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/app/main/csv/geo.csv', 'r')
    else:
        return
    lines = opener.readlines()
    article_list = []
    for line in lines:
        all_msg = line.split('\t')
        msg = all_msg[1]
        msg_list = msg.split(' ')
        atc_list = all_msg[2]
        for key in key_list:
            if key in msg_list:
                article_list.append(atc_list)
                break
    return article_list


# 对于文献类的数据 根据key_list 查找来对结果进行排序和推荐
def sort_by_keyword(key_list, paper_set, type):
    kwy_word_list = find_type(key_list, type)

    paper_set = de_repetition(paper_set)

    after_list = []
    sorted_list = []
    while paper_set:
        paper = paper_set.pop()
        if paper.lit_id in kwy_word_list:
            sorted_list.append(paper)
            print('这个方法是有用的')
        else:
            after_list.append(paper)

    sorted_list.extend(after_list)

    print(sorted_list)

    return sorted_list
# 通过请求来获取keyword
def request_to_server(select_data, sentence_data):
    client = Client('localhost', 1234)
    client.send_message('{} {}'.format(select_data, sentence_data))
    received = client.receive()
    print('this is the receive value{}'.format(received))
    word_list = received.decode('utf-8').split(' ')

    return word_list


## 对筛选出来的句子加上tag标签
def sentence_classfiy(sentence_list):
    '''
    :param word_list:
    :return: -1,1 means pos or neg
    '''
    return_list = []
    sen_clas = SentimentClassifier()
    for each in sentence_list:
        each_tag = sen_clas.predict(each)
        return_list.append((each, each_tag))
    return return_list


# def search_by_type_of_seg_and_field(words, field, tokensizer, is_abstruct, weight=None, vectorize=None):
#     '''
#     根据分词器类型与领域的类型查找
#     :param words: list
#     :param field: 1jd  2bio 3geo
#     :param type_of_tokenizer: int
#     :param is_abstruct from abstruct
#     :param weight:
#     :param vectorize:
#     :return: list[article],list[article_id]
#     '''
#     #     article_sentence = []
#     #     article_id = []
#     #
#     # 根据摘要来匹配
#     if is_abstruct == '1':
#         table_name = field + tokensizer
#     else:
#         table_name = field + tokensizer * 2
#     table = sege_dict.get(table_name)
#     print("table is {}".format(table))
#     pagin = find_in_text(words, table=table)
#     if not pagin:
#         print('there is not pagin')
#     else:
#         print(pagin)
#     return pagin


# 权重首先加载好
def sort_by_word_tfidf(key_list, paper_set, model, vectorize):
    '''
    根据tfidf模型对文献的id进行排序
    通过key_word 来计算在这篇文章中的向量，然后进行排序
    ## 用户输入的语句
    :param words: 用户输入的句子所拆分出来的词语
    :param article_ids: 一组文献的id
    :param texts: 文献id对应的文献
    :param weight: 所使用的model中的weight
    :param vectorize: 所使用的vectorize
    :return: 返回排好序的文献
    '''
    # 计算分词list 在这篇文献中的tfidf值的和
    # model 中每行为 一篇文章的所有词语的向量
    paper_set = de_repetition(paper_set)
    tfidfs = []
    weight = model.toarray()
    paper_id = [paper.lit_id for paper in paper_set]
    for each_id in paper_id:
        tfidf = 0
        for word in key_list:
            j = vectorize.vocabulary_.get(word)
            if j is not None:
                tfidf += weight[each_id][j]
        tfidfs.append(tfidf)
    # print('-'.join([str(i) for i in article_ids]))
    # print('-'.join([str(i) for i in tfidfs]))
    # 根据tfidf的值对文献id进行排序，tfidf值大的排在前面
    t_a = [(tfidf, paper) for tfidf, paper in zip(tfidfs, paper_set)]
    t_a.sort(reverse=True, key=lambda x: x[0])
    sorted_paper = [each[1] for each in t_a]
    # sort_article_ids = [article_id for tfidf, article_id, text in t_a]
    # sort_texts = [text for tfidf, article_id, text in t_a]
    print('this is tf-idf sorted paper{}'.format(t_a))
    return sorted_paper


#             res, article_ids = field_search( words, num, Bio_literature, Bio_abstruct_word_4, Bio_text_word_4,
#                                             Bio_text_sentence)
#
#         # 通过tf-idf来排序
#     res, article_ids = sort_by_word_tfidf(words, article_ids, res, weight, vectorize)
#
#     return res, article_ids


#
# def field_search( words, num, field_literature_class, field_abstruct_class, Text_word_class,
#                  Text_sentence_class):
#     '''
#     在相应领域中查找词语,返回结果与对应的article_id
#     :param session:
#     :param words: list
#     :param num: int
#     :param field_literature_class: table
#     :param field_abstruct_class: table
#     :param Text_word_class: table
#     :param Text_sentence_class: table
#     :return: 返回找到的结果与article_id，类型为list
#     '''
#     # 先在摘要中找
#     aricle_ids = find_in_db(session, field_abstruct_class, words, num)
#     print('摘要中找到的结果: ', end='')
#     print(aricle_ids)
#     texts, aricle_ids = get_data_by_id(session, field_literature_class, aricle_ids)
#     abstruct_len = len(aricle_ids)
#     # 如果找到的结果数目小于num，再在text中找
#     if abstruct_len < num:
#         text_ids = find_in_db(session, Text_word_class, words, num)  # 这里也找num个，结果与摘要的结果可能有重复
#         temp_text, temp_article_id = get_data_by_id(session, Text_sentence_class, text_ids)
#         print('全文中找到的结果：', end='')
#         print(temp_article_id)
#         for i, j in zip(temp_text, temp_article_id):  # 将全文的结果添加到摘要结果中
#             if j not in aricle_ids:
#                 aricle_ids.append(j)
#                 texts.append(i)
#     return texts[0:num], aricle_ids[0:num]

def find_in_text(keyword, table):
    pagin = table.query.filter(table.content == keyword) \
        .order_by(table.id.desc())

    return pagin


# 通过摘要查找 在 abstruct_word通过一个关键词
def find_in_subStruct(keyword, table):
    pagin = table.query.filter(table.content == keyword) \
        .order_by(table.id.desc())

    return pagin


#
#
#
# def find_in_db(DB_table_class_name, words, num):
#     '''
#     在一个数据表中查找词语，返回最匹配的文献或句子id，返回的结果不多于num个(如果结果多于num，则返回num个，否则返回全部)
#     :param DB_table_class_name: table
#     :param words: list
#     :param num: int
#     :return: list[num]
#     '''
#     # 先将所有等于关键词的条目（文献或句子id）都找出来，如果其中有文献或句子包含多个关键词，那么结果中就会有重复
#     word_list = []
#     # 根据数据库表类来判断是查找摘要还是全文句子
#     if issubclass(DB_table_class_name, Text_word):  # 传入的参数类型是否是Text_word的子类
#         for word in words:
#             # 首先查找与关键词完全相同的条目
#             word_list += session.query(DB_table_class_name.sentence_id).filter(
#                 DB_table_class_name.content == word).all()
#     elif issubclass(DB_table_class_name, Abstruct_word):  # 是否是Abstruct_word的子类
#         for word in words:
#             word_list += session.query(DB_table_class_name.article_id).filter(DB_table_class_name.content == word).all()
#     print('数据库查询花费时间： ' + str(time.time() - t1))
#     word_list = [word[0] for word in word_list]
#     # 根据重复的条目的重复次数排序
#     c = Counter(word_list).most_common(num)  # 这个函数返回值类型为[(),]
#     ids = [i[0] for i in c]
#     # 如果有num个结果，返回前num个，类型为list
#     return ids


# 将list 转换为pagination 对象
import math
from flask import abort


class ListPagination:

    def __init__(self, iterable, page=1, per_page=20):

        if page < 1:
            abort(404)

        self.iterable = iterable
        self.page = page
        self.per_page = per_page

        self.total = len(iterable)

        start_index = (page - 1) * per_page
        end_index = page * per_page

        self.items = iterable[start_index:end_index]

        if not self.items and page != 1:
            abort(404)

    @property
    def pages(self):
        """The total number of pages"""
        return int(math.ceil(self.total / float(self.per_page)))

    def prev(self):
        assert self.iterable is not None, ('an object is required for this method to work')
        iterable = self.iterable
        return self.__class__(iterable, self.page - 1, self.per_page)

    @property
    def prev_num(self):
        """Number of the previous page."""
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    def next(self):
        assert self.iterable is not None, ('an object is required for this method to work')
        iterable = self.iterable
        return self.__class__(iterable, self.page + 1, self.per_page)

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    @property
    def next_num(self):
        """Number of the next page"""
        return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        """Iterates over the page numbers in the pagination.  The four
        parameters control the thresholds how many numbers should be produced
        from the sides.  Skipped page numbers are represented as `None`.
        """
        last = 0
        for num in range(1, self.pages + 1):
            if (
                    num <= left_edge or
                    num > self.pages - right_edge or
                    (num >= self.page - left_current and
                     num <= self.page + right_current)
            ):
                if last + 1 != num:
                    yield None
                yield num
                last = num
        if last != self.pages:
            yield None
