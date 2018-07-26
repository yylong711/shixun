# _*_coding:utf-8_*_
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, BigInteger,String,Integer,Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import func
from tqdm import tqdm
from collections import Counter
import jieba.analyse
import time
from sklearn.externals import joblib
import os
import  re

# 创建实例，并连接test库
# engine = create_engine("mysql+pymysql://root:@localhost/stdb?charset=utf8",
#                        encoding='utf-8', echo=False)
engine = create_engine('mysql://root:newpass@localhost:3306/shixun?charset=utf8mb4')


metadata = MetaData()

class Abstruct_word(object):
    def __init__(self, id,content,article_id):
        self.id = id
        self.content=content
        self.article_id=article_id

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
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('article_id', BigInteger)
                       )
geo_abstruct_word_3 = Table('geo_abstruct_word_3', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('article_id', BigInteger)
                       )
geo_abstruct_word_2 = Table('geo_abstruct_word_2', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('article_id', BigInteger)
                       )
geo_abstruct_word_1 = Table('geo_abstruct_word_1', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('article_id', BigInteger)
                       )


class Literature(object):
    def __init__(self, lit_id,lit_title,lit_author,lit_kw,lit_abstruct,lit_text,
                 lit_pub_time,lit_publisher,lit_is_extract,lit_type,lit_subject):
        self.lit_id = lit_id
        self.lit_title=lit_title
        self.lit_author=lit_author
        self.lit_kw=lit_kw
        self.lit_abstruct=lit_abstruct
        self.lit_text=lit_text
        self.lit_pub_time=lit_pub_time
        self.lit_publisher=lit_publisher
        self.lit_is_extract=lit_is_extract
        self.lit_type=lit_type
        self.lit_subject=lit_subject

class Geo_literature(Literature):
    pass
class Bio_literature(Literature):
    pass

geo_literature = Table('geo_literature', metadata,
                       Column('lit_id', BigInteger , primary_key=True),
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
                       Column('lit_id', BigInteger , primary_key=True),
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
    def __init__(self, id,content,sentence_id):
        self.id = id
        self.content=content
        self.sentence_id=sentence_id

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
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
geo_text_word_2 = Table('geo_text_word_2', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
geo_text_word_3 = Table('geo_text_word_3', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
geo_text_word_4 = Table('geo_text_word_4', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
bio_text_word_1 = Table('bio_text_word_1', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
bio_text_word_2 = Table('bio_text_word_2', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
bio_text_word_3 = Table('bio_text_word_3', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )
bio_text_word_4 = Table('bio_text_word_4', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(50)),
                       Column('sentence_id', BigInteger)
                       )

class Text_sentence(object):
    def __init__(self, id,content,article_id):
        self.id = id
        self.content=content
        self.article_id=article_id

class Geo_text_sentence(Text_sentence):
    pass
class Bio_text_sentence(Text_sentence):
    pass
geo_text_sentence = Table('geo_text_sentence', metadata,
                       Column('id', BigInteger , primary_key=True),
                       Column('content', String(3000)),
                       Column('article_id', BigInteger)
                       )
bio_text_sentence = Table('bio_text_sentence', metadata,
                       Column('id', BigInteger , primary_key=True),
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


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopword.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr



# def store_sentence_into_db(from_file_name,to_file_name):
    # '''
    # 将txt文件中的文献拆分成句子，存入数据库,并把句子存入txt中
    # :param from_file_name: 文件名
    # :param to_file_name: 文件名
    # :return:
    # '''
    # with open(from_file_name,'r',encoding='utf-8')as read_from,open(to_file_name,'a',encoding='utf-8')as write_to:
    #     lines=read_from.readlines()
    #     global sentence_id
    #     for line in tqdm(lines):# 每一行对应一篇文献，一篇文献有多个字段，字段包括作者，摘要等
    #         line_list=line.split('   ')# 在将数据存入txt的时候同一个文献的每个字段用空格隔开
    #         write_sentence=''
    #         for l in line_list:# l 表示一个字段
    #             sentence_list=l.split('。')# 对于一个字段，根据。将字段分成句子
    #             for sen in sentence_list:
    #                 if sen!='' and len(sen)<=3000:
    #                     sen=sen.strip()
    #                     session.add(Text_sentence(sentence_id, sen))# 存句子
    #                     write_sentence+=str(sentence_id)+'\t'+sen+'\n'
    #                     sentence_id+=1
    #         session.commit()
    #         write_to.write(write_sentence)


def write_text_sentence_in_db(file_dir,field_text_sentence_class):
    '''
    将text的句子写入数据库
    :param file_dir:text句子文件所在的目录
    :param field_text_sentence_class:存储text句子的数据库表对应的类名
    :return:
    '''
    sum_n=0
    sentence_id=1
    for root,dirs,files in os.walk(file_dir):
        for file in tqdm(files):
            article_id=file.split('.')[0].split('_')[3]
            with open(file_dir+file,'r',encoding='utf-8')as opener:
                lines=opener.readlines()
                for line in lines:
                    line=line.strip()
                    if line!='' and line!='\n':
                        session.add(field_text_sentence_class(sentence_id,line,article_id))
                    sentence_id+=1
                session.commit()
    pass

def files_text_to_sentence(from_file_dir,to_file_dir):
    '''
    将一系列的文件中的text拆分成句子存入txt
    :param from_file_dir: text的文件所在的目录
    :param to_file_dir: 句子所在的目录
    :return:
    '''
    for root, dirs, files in os.walk(from_file_dir):
        for file in tqdm(files):
            with open(root+file,'r',encoding='utf-8') as from_file,open(to_file_dir+file,'w',encoding='utf-8')as to_file:
                sd = re.compile(r'\[+\d{1,2}\]')
                line = from_file.readline()
                sentences=''
                sentence_list=line.split('。')
                for sen in sentence_list:
                    s_list=sd.split(sen)
                    for s in s_list:
                        if s != '' and len(s) <= 3000:
                            sentences += s.strip()+'\n'
                to_file.write(sentences)


def store_word_into_file(sentence_file_name,word_file_name):
    '''
    将txt文件中的句子分成词语，存入txt
    :param sentence_file_name: 句子的文件名
    :param word_file_name: 词语的文件名
    :return:
    '''
    global word_id
    with open(sentence_file_name,'r',encoding='utf-8')as sen_file,open(word_file_name,'a',encoding='utf-8')as word_file:
        lines=sen_file.readlines()
        stopwords = stopwordslist('stopword.txt')  # 这里加载停用词的路径
        for line in tqdm(lines):
            sentence_list=line.split('\t')
            sentence_id=int(sentence_list[0])
            sen=sentence_list[1]
            seg_list = jieba.cut(sen.strip(), cut_all=False)  # 将句子分词
            word_list=''
            for seg in seg_list:
                # if(session.query(Word).filter(Word.content==str(seg)).first()==None):# 查找数据库中是否已经存在该词语
                seg=re.sub('[’ ‘:：《》∠×°～“”·、！!"#$%&\'。.()*+，,-./;<=>?@[\\]^_`{|}~]+', '', seg)
                if len(seg)<=50 and seg!='' and seg not in stopwords:
                    word_list+=str(word_id)+'\t'+seg+'\t'+str(sentence_id)+'\n'
                    word_id += 1
            word_file.write(word_list)

def write_word_into_db(word_file_dir,class_name):
    '''
    将词语存入数据库
    :param word_file_name:词语所在文件的目录
    :param class_name:存入的表对应的类
    :return:
    '''
    for root,dirs,files in os.walk(word_file_dir):
        for file in tqdm(files):
            with open(word_file_dir+file,'r',encoding='utf-8')as opener:
                words=opener.readlines()
                for word in words:
                    word_list=word.split('\t')
                    session.add(class_name(int(word_list[0]), word_list[1], int(word_list[2])-44400))
                session.commit()


def write_abstruct_word_into_txt(file_dir,to_file_dir):
    '''
    将文献摘要的词语存入txt
    :param file_dir: 文献摘要词语所在的目录
    :param to_file_dir: 目标目录
    :return:
    '''
    word_id=1
    for root, dirs, files in os.walk(file_dir):
        for file in tqdm(files):
            article_id=re.findall("\d+",file)[0]
            words=''
            with open(file_dir+file,'r',encoding='utf-8')as opener,open(to_file_dir+file,'w',encoding='utf-8')as opener2:
                lines=opener.readlines()
                for index,word in enumerate(lines):
                    if index !=4:
                        word_list=word.split(' ')
                        for word in word_list:
                            if len(word)<=50 and word!='' and word!='\n':
                                words+=str(word_id)+'\t'+word+'\t'+article_id+'\n'
                                word_id+=1
                opener2.write(words)


def write_text_word_into_txt(file_dir,to_file_dir):
    '''
    将text的词语存入txt文件中
    :param file_dir:text词语文件所在的目录
    :param to_file_dir:目标目录
    :return:
    '''
    word_id=1
    sentence_id=1
    stopwords = stopwordslist('stopword.txt')  # 这里加载停用词的路径
    for root, dirs, files in os.walk(file_dir):
        for file in tqdm(files):
            words = ''
            with open(file_dir + file, 'r', encoding='utf-8')as opener, open(to_file_dir + file, 'w',
                                                                             encoding='utf-8')as opener2:
                lines = opener.readlines()
                for index, word in enumerate(lines):
                    word_list = word.split(' ')
                    for word in word_list:
                        if len(word) <= 50 and word != '' and word != '\n' and word not in stopwords:
                            words += str(word_id) + '\t' + word + '\t' + str(sentence_id) + '\n'
                            word_id += 1
                    sentence_id+=1
                opener2.write(words)

def change_file_name():
    pass

if __name__ == '__main__':

    # store_sentence_into_db('geo_literature.txt','geo_literature_sentence.txt')# 读句子，存数据库，存到txt文件
    # store_sentence_into_db('bio_literature.txt','bio_literature_sentence.txt')
    # store_word_into_file('geo_literature_sentence.txt','geo_literature_word.txt')# 读句子，拆成词语，存txt
    # store_word_into_file('bio_literature_sentence.txt','bio_literature_word.txt')
    # files_text_to_sentence('cut_data/geo_text/','cut_data/geo_bio/geo_text_sentence/')# 将全文拆成句子
    # files_text_to_sentence('cut_data/bio_text/','cut_data/geo_bio/bio_text_sentence/')
    # write_text_sentence_in_db('cut_data/geo_bio/geo_text_sentence/',Geo_text_sentence)# text句子写数据库
    # write_text_sentence_in_db('cut_data/geo_bio/bio_text_sentence/',Bio_text_sentence)

    # write_abstruct_word_into_txt('cut_data/literature/geo_4/',
    #                              'cut_data/abstruct_word_by_format/geo_4/')# 将文献的摘要词语按格式存入txt
    # write_abstruct_word_into_txt('cut_data/literature/bio_4/',
    #                              'cut_data/abstruct_word_by_format/bio_4/')
    # write_word_into_db('cut_data/abstruct_word_by_format/geo_4/',Geo_abstruct_word_4)# 读摘要词语，存数据库
    # write_word_into_db('cut_data/abstruct_word_by_format/bio_4/',Bio_abstruct_word_4)
    # write_word_into_db('cut_data/abstruct_word_by_format/geo_3/', Geo_abstruct_word_3)
    # write_word_into_db('cut_data/abstruct_word_by_format/bio_3/', Bio_abstruct_word_3)
    # write_word_into_db('cut_data/abstruct_word_by_format/geo_2/', Geo_abstruct_word_2)
    # write_word_into_db('cut_data/abstruct_word_by_format/bio_2/', Bio_abstruct_word_2)
    # write_word_into_db('cut_data/abstruct_word_by_format/geo_1/', Geo_abstruct_word_1)
    # write_word_into_db('cut_data/abstruct_word_by_format/bio_1/', Bio_abstruct_word_1)
    # write_text_word_into_txt('cut_data/text_word/seg_geo_sentence1/',
    #                          'cut_data/text_word_by_format/seg_geo_sentence1/')# 将text的词语按格式存到txt
    # write_text_word_into_txt('cut_data/text_word/seg_bio_sentence3/',
    #                          'cut_data/text_word_by_format/seg_bio_sentence3/')
    write_word_into_db('cut_data/text_word_by_format/seg_geo_sentence1/',Geo_text_word_1)# 读text词语，存数据库
    # write_word_into_db('cut_data/text_word_by_format/seg_bio_sentence1/',Bio_text_word_1)
    # write_word_into_db('cut_data/text_word_by_format/seg_geo_sentence2/', Geo_text_word_2)
    # write_word_into_db('cut_data/text_word_by_format/seg_bio_sentence2/', Bio_text_word_2)
    # write_word_into_db('cut_data/text_word_by_format/seg_geo_sentence3/', Geo_text_word_3)
    # write_word_into_db('cut_data/text_word_by_format/seg_bio_sentence3/', Bio_text_word_3)
    # write_word_into_db('cut_data/text_word_by_format/seg_geo_sentence4/', Geo_text_word_4)
    # write_word_into_db('cut_data/text_word_by_format/seg_bio_sentence4/', Bio_text_word_4)

    # 关闭session:
    session.close()










