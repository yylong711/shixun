# _*_coding:utf-8_*_
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, BigInteger, String, Integer, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import func
from tqdm import tqdm
from collections import Counter
import jieba.analyse
import time
from sklearn.externals import joblib

# 创建实例，并连接test库
# engine = create_engine("mysql+pymysql://root:@localhost/stdb?charset=utf8",
#                        encoding='utf-8', echo=False)
engine = create_engine('mysql://root:newpass@localhost:3306/shixun?charset=utf8mb4')

metadata = MetaData()


class Abstruct_word(object):
    def __init__(self, id, content, article_id):
        self.id = id
        self.content = content
        self.article_id = article_id


class Geo_abstruct_word_4(Abstruct_word):
    pass


class Geo_abstruct_word_3(Abstruct_word):
    pass


class Geo_abstruct_word_2(Abstruct_word):
    pass


class Geo_abstruct_word_1(Abstruct_word):
    pass


class Bio_abstruct_word_4(Abstruct_word):
    pass


class Bio_abstruct_word_3(Abstruct_word):
    pass


class Bio_abstruct_word_2(Abstruct_word):
    pass


class Bio_abstruct_word_1(Abstruct_word):
    pass


bio_abstruct_word_4 = Table('bio_abstruct_word_4', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
bio_abstruct_word_3 = Table('bio_abstruct_word_3', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
bio_abstruct_word_2 = Table('bio_abstruct_word_2', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
bio_abstruct_word_1 = Table('bio_abstruct_word_1', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )

geo_abstruct_word_4 = Table('geo_abstruct_word_4', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
geo_abstruct_word_3 = Table('geo_abstruct_word_3', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
geo_abstruct_word_2 = Table('geo_abstruct_word_2', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )
geo_abstruct_word_1 = Table('geo_abstruct_word_1', metadata,
                            Column('id', BigInteger, primary_key=True),
                            Column('content', String(50)),
                            Column('article_id', BigInteger)
                            )


class Literature(object):
    def __init__(self, lit_id, lit_title, lit_author, lit_kw, lit_abstruct, lit_text,
                 lit_pub_time, lit_publisher, lit_is_extract, lit_type, lit_subject):
        self.lit_id = lit_id
        self.lit_title = lit_title
        self.lit_author = lit_author
        self.lit_kw = lit_kw
        self.lit_abstruct = lit_abstruct
        self.lit_text = lit_text
        self.lit_pub_time = lit_pub_time
        self.lit_publisher = lit_publisher
        self.lit_is_extract = lit_is_extract
        self.lit_type = lit_type
        self.lit_subject = lit_subject


class Geo_literature(Literature):
    pass


class Bio_literature(Literature):
    pass


geo_literature = Table('geo_literature', metadata,
                       Column('lit_id', BigInteger, primary_key=True),
                       Column('lit_title', String(100)),
                       Column('lit_author', String(1000)),
                       Column('lit_kw', String(1000)),
                       Column('lit_abstruct', String(10000)),
                       Column('lit_text', Text),
                       Column('lit_pub_time', String(1000)),
                       Column('lit_publisher', String(1000)),
                       Column('lit_is_extract', Integer),
                       Column('lit_type', String(1000)),
                       Column('lit_subject', String(1000))
                       )

bio_literature = Table('bio_literature', metadata,
                       Column('lit_id', BigInteger, primary_key=True),
                       Column('lit_title', String(100)),
                       Column('lit_author', String(1000)),
                       Column('lit_kw', String(1000)),
                       Column('lit_abstruct', String(10000)),
                       Column('lit_text', Text),
                       Column('lit_pub_time', String(1000)),
                       Column('lit_publisher', String(1000)),
                       Column('lit_is_extract', Integer),
                       Column('lit_type', String(1000)),
                       Column('lit_subject', String(1000))
                       )


class Text_word(object):
    def __init__(self, id, content, sentence_id):
        self.id = id
        self.content = content
        self.sentence_id = sentence_id


class Geo_text_word_1(Text_word):
    pass


class Geo_text_word_2(Text_word):
    pass


class Geo_text_word_3(Text_word):
    pass


class Geo_text_word_4(Text_word):
    pass


class Bio_text_word_1(Text_word):
    pass


class Bio_text_word_2(Text_word):
    pass


class Bio_text_word_3(Text_word):
    pass


class Bio_text_word_4(Text_word):
    pass


geo_text_word_1 = Table('geo_text_word_1', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
geo_text_word_2 = Table('geo_text_word_2', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
geo_text_word_3 = Table('geo_text_word_3', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
geo_text_word_4 = Table('geo_text_word_4', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
bio_text_word_1 = Table('bio_text_word_1', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
bio_text_word_2 = Table('bio_text_word_2', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
bio_text_word_3 = Table('bio_text_word_3', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )
bio_text_word_4 = Table('bio_text_word_4', metadata,
                        Column('id', BigInteger, primary_key=True),
                        Column('content', String(50)),
                        Column('sentence_id', BigInteger)
                        )


class Text_sentence(object):
    def __init__(self, id, content, article_id):
        self.id = id
        self.content = content
        self.article_id = article_id


class Geo_text_sentence(Text_sentence):
    pass


class Bio_text_sentence(Text_sentence):
    pass


geo_text_sentence = Table('geo_text_sentence', metadata,
                          Column('id', BigInteger, primary_key=True),
                          Column('content', String(3000)),
                          Column('article_id', BigInteger)
                          )
bio_text_sentence = Table('bio_text_sentence', metadata,
                          Column('id', BigInteger, primary_key=True),
                          Column('content', String(3000)),
                          Column('article_id', BigInteger)
                          )

mapper(Geo_abstruct_word_4, geo_abstruct_word_4)
mapper(Geo_abstruct_word_3, geo_abstruct_word_3)
mapper(Geo_abstruct_word_2, geo_abstruct_word_2)
mapper(Geo_abstruct_word_1, geo_abstruct_word_1)
mapper(Bio_abstruct_word_4, bio_abstruct_word_4)
mapper(Bio_abstruct_word_3, bio_abstruct_word_3)
mapper(Bio_abstruct_word_2, bio_abstruct_word_2)
mapper(Bio_abstruct_word_1, bio_abstruct_word_1)
mapper(Geo_literature, geo_literature)
mapper(Bio_literature, bio_literature)
mapper(Geo_text_word_4, geo_text_word_4)
mapper(Geo_text_word_3, geo_text_word_3)
mapper(Geo_text_word_2, geo_text_word_2)
mapper(Geo_text_word_1, geo_text_word_1)
mapper(Bio_text_word_4, bio_text_word_4)
mapper(Bio_text_word_3, bio_text_word_3)
mapper(Bio_text_word_2, bio_text_word_2)
mapper(Bio_text_word_1, bio_text_word_1)
mapper(Geo_text_sentence, geo_text_sentence)
mapper(Bio_text_sentence, bio_text_sentence)

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
session = Session_class()  # 生成session实例


def run_time(func):
    def print_run_time(*args, **kwargs):
        t1 = time.perf_counter()
        ret = func(*args, **kwargs)
        t2 = time.perf_counter()
        print('{}运行的时间为：{}'.format(func.__name__, t2 - t1))
        return ret

    return print_run_time


@run_time
def find_in_db(session, DB_table_class_name, words, num):
    '''
    在一个数据表中查找词语，返回最匹配的文献或句子id，返回的结果不多于num个(如果结果多于num，则返回num个，否则返回全部)
    :param session:数据库会话
    :param DB_table_class_name: 数据表类
    :param words: 所要查找的一组词语,类型为list
    :param num: 返回的结果不多于num
    :return: 返回最符合关键词的文献或句子的id,个数不多于num，类型为list
    '''
    t1 = time.time()
    # 先将所有等于关键词的条目（文献或句子id）都找出来，如果其中有文献或句子包含多个关键词，那么结果中就会有重复
    word_list = []
    # 根据数据库表类来判断是查找摘要还是全文句子
    if issubclass(DB_table_class_name, Text_word):  # 传入的参数类型是否是Text_word的子类
        for word in words:
            # 首先查找与关键词完全相同的条目
            word_list += session.query(DB_table_class_name.sentence_id).filter(
                DB_table_class_name.content == word).all()
    elif issubclass(DB_table_class_name, Abstruct_word):  # 是否是Abstruct_word的子类
        for word in words:
            word_list += session.query(DB_table_class_name.article_id).filter(DB_table_class_name.content == word).all()
    print('数据库查询花费时间： ' + str(time.time() - t1))
    word_list = [word[0] for word in word_list]
    # 根据重复的条目的重复次数排序
    c = Counter(word_list).most_common(num)  # 这个函数返回值类型为[(),]
    ids = [i[0] for i in c]
    # 如果有num个结果，返回前num个，类型为list
    return ids


@run_time
def get_data_by_id(session, DB_table_class_name, ids):
    '''
    根据给出的文献或者句子的id，查找文献的text或者句子，并返回句子所对应的文献的id
    :param session: 数据库会话
    :param DB_table_class_name: 数据表类
    :param ids: 文献id，类型list
    :return: 返回文献的text或句子，句子对应的文献的id，类型为list
    '''
    texts = []
    article_ids = []
    for i in ids:
        if issubclass(DB_table_class_name, Text_sentence):
            temp = session.query(DB_table_class_name.content,
                                 DB_table_class_name.article_id).filter(DB_table_class_name.id == i).first()
            texts.append(temp[0])
            article_ids.append(temp[1])
        elif issubclass(DB_table_class_name, Literature):
            texts.append(
                session.query(DB_table_class_name.lit_abstruct).filter(DB_table_class_name.lit_id == i).first()[0])
    if issubclass(DB_table_class_name, Literature):
        article_ids = ids
    return texts, article_ids


@run_time
def field_search(session, words, num, field_literature_class, field_abstruct_class, Text_word_class,
                 Text_sentence_class):
    '''
    在相应领域中查找词语,返回结果与对应的article_id
    :param session: 数据库会话
    :param words: 词语
    :param num: 返回结果个数
    :param field_literature_class: 文献全部内容所在的表类
    :param field_abstruct_class: 摘要词语所在的表类
    :param Text_word_class: 全文词语所在的表类
    :param Text_sentence_class: 全文句子所在的表类
    :return: 返回找到的结果与article_id，类型为list
    '''
    # 先在摘要中找
    aricle_ids = find_in_db(session, field_abstruct_class, words, num)
    print('摘要中找到的结果: ', end='')
    print(aricle_ids)
    texts, aricle_ids = get_data_by_id(session, field_literature_class, aricle_ids)
    abstruct_len = len(aricle_ids)
    # 如果找到的结果数目小于num，再在text中找
    if abstruct_len < num:
        text_ids = find_in_db(session, Text_word_class, words, num)  # 这里也找num个，结果与摘要的结果可能有重复
        temp_text, temp_article_id = get_data_by_id(session, Text_sentence_class, text_ids)
        print('全文中找到的结果：', end='')
        print(temp_article_id)
        for i, j in zip(temp_text, temp_article_id):  # 将全文的结果添加到摘要结果中
            if j not in aricle_ids:
                aricle_ids.append(j)
                texts.append(i)
    return texts[0:num], aricle_ids[0:num]


@run_time
#
def sort_by_word_tfidf(words, article_ids, texts, weight, vectorize):
    '''
    根据tfidf模型对文献的id进行排序
    通过将句子分割为词语计算累计的tf-idf值来进行排序
    :param words: 用户输入的句子所拆分出来的词语
    :param article_ids: 一组文献的id
    :param texts: 文献id对应的文献
    :param weight: 所使用的model中的weight
    :param vectorize: 所使用的vectorize
    :return: 返回排好序的文献id
    '''
    tfidfs = []
    for article_id in article_ids:  # 对于每一篇文献
        tfidf = 0
        for word in words:  # 计算所有词语在这篇文献的tfidf值的和
            j = vectorize.vocabulary_.get(word)
            if j is not None:
                tfidf += weight[article_id][j]
        tfidfs.append(tfidf)
    # print('-'.join([str(i) for i in article_ids]))
    # print('-'.join([str(i) for i in tfidfs]))
    # 根据tfidf的值对文献id进行排序，tfidf值大的排在前面
    t_a = [(tfidf, article_id, text) for tfidf, article_id, text in zip(tfidfs, article_ids, texts)]
    t_a.sort(reverse=True)
    sort_article_ids = [article_id for tfidf, article_id, text in t_a]
    sort_texts = [text for tfidf, article_id, text in t_a]
    return sort_texts, sort_article_ids


@run_time
# 输入一句话，返回num 结果个文献id
def search_by_type_of_seg_and_field(session, words, num, type_of_tokenizer, type_of_field, weight, vectorize):
    '''
    根据分词器类型与领域的类型查找
    :param session: 数据库的会话
    :param words: 所要查找的词组
    :param num: 返回结果的个数
    :param type_of_tokenizer: 分词器的类型
    :param type_of_field: 领域的类型
    :param weight: 所使用的model中的weight
    :param vectorize: 所使用的vectorize
    :return: 返回结果与对应的文献的id
    '''
    res = []
    article_ids = []
    if type_of_tokenizer == 1:
        if type_of_field == 1:
            res, article_ids = field_search(session, words, num, Geo_literature, Geo_abstruct_word_1, Geo_text_word_1,
                                            Geo_text_sentence)
        elif type_of_field == 2:
            res, article_ids = field_search(session, words, num, Bio_literature, Bio_abstruct_word_1, Bio_text_word_1,
                                            Bio_text_sentence)
    elif type_of_tokenizer == 2:
        if type_of_field == 1:
            res, article_ids = field_search(session, words, num, Geo_literature, Geo_abstruct_word_2, Geo_text_word_2,
                                            Geo_text_sentence)
        elif type_of_field == 2:
            res, article_ids = field_search(session, words, num, Bio_literature, Bio_abstruct_word_2, Bio_text_word_2,
                                            Bio_text_sentence)
    elif type_of_tokenizer == 3:
        if type_of_field == 1:
            res, article_ids = field_search(session, words, num, Geo_literature, Geo_abstruct_word_3, Geo_text_word_3,
                                            Geo_text_sentence)
        elif type_of_field == 2:
            res, article_ids = field_search(session, words, num, Bio_literature, Bio_abstruct_word_3, Bio_text_word_3,
                                            Bio_text_sentence)
    elif type_of_tokenizer == 4:
        if type_of_field == 1:
            res, article_ids = field_search(session, words, num, Geo_literature, Geo_abstruct_word_4, Geo_text_word_4,
                                            Geo_text_sentence)
        elif type_of_field == 2:
            res, article_ids = field_search(session, words, num, Bio_literature, Bio_abstruct_word_4, Bio_text_word_4,
                                            Bio_text_sentence)

        # 通过tf-idf来排序
    res, article_ids = sort_by_word_tfidf(words, article_ids, res, weight, vectorize)

    return res, article_ids


# def update_pri_key(session,table_name):
#     '''
#     修改原文文献的id为从1开始
#     :param session:
#     :param table_name:
#     :return:
#     '''
#     ids=session.query(func.count(table_name.lit_id)).scalar()
#     for i in tqdm(range(ids)):
#         one_id=session.query(table_name.lit_id).filter(table_name.lit_id>10000).first()[0]
#         session.query(table_name).filter(table_name.lit_id==one_id).update({table_name.lit_id:i+1})
#         if i%20==0:
#             session.commit()
#     session.commit()


def main():
    t1 = time.perf_counter()
    model, vectorize = load_model('geo_4_tf.model', 'geo_4_vectorize.model')
    weight = model.toarray()
    num = 10
    sentence = '工程布置以及相应的成果质量评述进行了详细的阐述以期为行业同仁提供一些借鉴经验。'  # 这是文献id 4摘要里的一句话
    # 分词
    words = jieba.lcut(sentence, cut_all=False)
    # print('-'.join(words))
    t2 = time.perf_counter()
    res, ids = search_by_type_of_seg_and_field(session, words, num, 1, 1, weight, vectorize)  # 这里的words最好是个list
    # print('\n'.join(res))
    t3 = time.perf_counter()
    # for r,i in zip(res,ids):
    #     print(str(i)+'\t'+r)
    print('查询总时间： ' + str(t3 - t2))
    print('总时间： ' + str(time.perf_counter() - t1))
    session.close()


if __name__ == '__main__':
    main()