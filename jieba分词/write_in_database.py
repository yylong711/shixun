import sqlalchemy
from tqdm import tqdm
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from app.models import *
from jieba分词.main import read_sentence_and_cutword, read_file

engine = create_engine('mysql://root:newpass@localhost:3306/shixun?charset=utf8mb4')

Session = sessionmaker(bind=engine)

# sentence_one = Sentence(tag='JD', content='港荣蒸蛋糕，真的很好吃')
session = Session()


def add_sentence(sentence_id, sentence_content):
    # if not session.query(Sentence).filter_by(content=sentence_content).first():
    sentence = Sentence(id=sentence_id, content=sentence_content)
    # sentence.word=
    session.add(sentence)
    # session.commit()


def write_word_in_database(word_file):
    lines = read_file(word_file)
    i = 1
    line_s = 1
    for line in tqdm(lines):
        words = line.split(' ')
        for word in words:
            if len(word) < 50:
                word_db = Jieba_Word(id=i, content=word, sentence_id=line_s)
                session.add(word_db)
                i += 1
        line_s += 1
        if i % 1000 == 0:
            session.commit()


def write_sentence_in_database(sentence_file):
    filename_1 = sentence_file
    lines_sentence = read_file(filename_1)
    # lines_word = read_file(word_file)

    # write sentence
    index = 1
    try:
        for sentence_line in tqdm(lines_sentence):
            sentence = Sentence(id=index, content=sentence_line)
            session.add(sentence)
            index += 1
            if index % 1000 == 0:
                session.commit()
    except Exception as e:
        print('出错了{}'.format(e.args))
        print("index ")

    # i = 1
    # for word_line in tqdm(lines_2):
    #     # #     sentence_id=add_sentence(sentence_line)
    #     words = word_line.split(' ')
    #     for word in words:
    #         if word:
    #             write_word_in_db(word, i)
    #     i += 1


# 从分好词的txt文件读取 数据然后写入数据库
def write_words_in_db():
    with open('cut_words_result.txt', 'r') as opener:
        lines = opener.readlines()
        for line in tqdm(lines):
            msg = line.split(' ')
            if len(msg) == 2 and msg[0]:
                write_word_in_db(msg[0], int(msg[1]))

    session.commit()


def write_word_in_db(word_content, sentence_id):
    # 如果能从数据库中找到
    Is_exist = session.query(Word_num).filter_by(words_content=word_content).first()
    if Is_exist:
        Is_exist.num += 1
    else:
        word = Jieba_Word(content=word_content, sentence_id=sentence_id)
        word_num = Word_num(words_content=word_content)
        session.add(word)
        session.add(word_num)
    # session.commit()


def play_select(word_content):
    result = session.query().filter(Word_num.words_content == word_content)
    print(result)


def write():
    pass


if __name__ == '__main__':
    # write_sentence_in_database('txt/JD.txt')

    # play_select(word_content='asdsadasd')
    # write_sentence_in_database('txt/segJD2.txt')
    write_word_in_database('txt/segJD4.txt')
    session.commit()
    # write_words_in_db()
