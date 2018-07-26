import re
from jieba import analyse
import jieba.posseg as psg
import jieba
from jieba分词.Config import WORD_PRIORITY
from tqdm import tqdm


def main():
    val = input("输入：")
    # 关键词
    seg_list = analyse.extract_tags(val, allowPOS=('n', 'ns', 'a', 'Ag'))
    print("/".join(seg_list))

    # 写入文件的数据，文件名 文件类对象


def read_file(filename):
    opener = open(filename, 'r')
    lines = opener.readlines()
    return lines


# 返回一个文件类对象
def add_read_file(filename):
    opener = open(filename, 'a')
    lines = opener.readlines()
    return lines

    # 将 sentence 写入文件


def write_sentence_in_file(sentence, filename='result.txt', opener=None):
    if not opener:
        opener = open(filename, 'a')
    opener.write(sentence + '\n')


def is_same():
    lines_1 = read_file('JD.txt')
    lines_2 = read_file('result.txt')
    print(len(lines_1))
    print(len(lines_2))
    print(len(lines_1) == len(lines_2))


def split_word_andWrite():
    re_1 = re.compile("[\s+\.\!\：;~/_,$%^*(+\"\'?]+|[+——！，。？、~@#￥%……&*（）a-zA-Z]+")
    re_2 = re.compile("\d{3,50}")
    # str='想做/ 兼_职/学生_/ 的 、加21,我Q：  2315. 8 0. ！！？？  8 6 。0.  2。 3 111 '
    lines = read_file('JD.txt')

    for line in tqdm(lines):
        result = re.sub(re_1, '', line)
        result_2 = re.sub(re_2, '', result)
        if result_2:
            write_sentence_in_file(result_2, filename='result_2.txt')


# 去掉文件 后面的/t内容

def remove_tag():
    with open('sentence_JD.txt', 'r', encoding='utf-8')as opener:
        lines = opener.readlines()
        s = 0
        for line in lines:
            line = line.split('\t')[0]
            write_sentence_in_file(line, 'JD.txt')
            print(s)
    # 输入sentence 返回分割好的值


def write_word_in_file(sentence):
    pass


def play_1():
    pass


def read_sentence_and_cutword(sentence):
    jieba.posseg.POSTokenizer = jieba
    tl = jieba.cut_for_search(sentence, HMM=True)
    # tl=psg.cut(sentence,HMM=True)
    # tl = analyse.extract_tags(sentence,)

    # tl = analyse.extract_tags(sentence, allowPOS=('n', 'ns', 'a', 'Ag','v'))
    # line_list = [(w,f) for w, f in tl]
    line_list = [w for w in tl]
    # write_result = ' '.join(line_list)
    return set(line_list)


def get_key_word(sentence):
    '''
    :param sentence:
    :return:one word
    '''

    tl = psg.cut(sentence)
    result = [(i1, i2) for i1, i2 in tl]
    print(result)
    max = 0
    max_word = None
    for i in result:
        if WORD_PRIORITY.get(i[1]) and WORD_PRIORITY[i[1]] > max:
            max = WORD_PRIORITY.get(i[1])
            max_word = i[0]
    return max_word


def find_better_word():


    pass


def write_all_word_in_txt():
    word_opener = open('cut_words_result.txt', 'a')
    with open('JD_after_wash.txt', 'r')as opener:
        lines = opener.readlines()
        line_num = 1
        for sentence in tqdm(lines):
            # set 类型
            result = read_sentence_and_cutword(sentence)
            result_sentence = ' '.join(result)
            word_opener.write(result_sentence + '\n')
            line_num += 1


def remove():
    opener = open('txt/segJD4.txt', 'r')
    result = opener.readlines()
    print(len(result))


if __name__ == '__main__':
    # strs = '去北京大学玩'
    # write_all_word_in_txt()
    remove()
    # print(get_key_word(sentence='相机'))
    # play_1()
    # result = read_sentence_and_cutword(strs)
    # print(result)
    # is_same()
    # split_word_andWrite()
