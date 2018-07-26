from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from jieba分词.main import read_file
import time

corpus = ["我 来到 北京 清华大学",  # 第一类文本切词后的结果，词之间以空格隔开
          "他 来到 了 网易 杭研 大厦",  # 第二类文本的切词结果
          "小明 硕士 毕业 与 中国 科学院",  # 第三类文本的切词结果
          "我 爱 北京 天安门"]


def clock(func):
    def clocked(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print('花费的时间是{}'.format(end_time - start_time))
        return result

    return clocked


@clock
def train_model(word_list, seg_id):
    '''
    :param word_list: list of words
    :return:
    '''
    # 将word转换为词频矩阵
    vectorize = CountVectorizer()
    # 统计每个词语的tf-idf权值
    transform = TfidfTransformer()
    # 得到某个关键词的向量
    tfidf = transform.fit_transform(vectorize.fit_transform(word_list))

    joblib.dump(tfidf, '{}_tf.model'.format(seg_id))
    joblib.dump(vectorize, '{}_vectorize.model'.format(seg_id))


@clock
def load_model(modelname, vectorize_name):
    full_model_path = '/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/tf_idf/model/{}'.format(modelname)
    full_vectorize_path = '/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/tf_idf/model/{}'.format(
        vectorize_name)
    model = joblib.load(full_model_path)
    vectorize = joblib.load(full_vectorize_path)
    return model, vectorize


@clock
# 找到一个关键词list 默认为2  通过tf-idf 算法 计算每个关键词在模型中的权重

def find_the_better_word(wordlist, model, vectorize, keyword_num=5):
    value_list = [(each, vectorize.vocabulary_.get(each)) for each in wordlist]
    print('value list is {}'.format(value_list))

    value_list = [each for each in value_list if each[1]]
    if value_list:
        value_list.sort(key=lambda x: x[1])
    key_list = [each[0] for each in value_list[:keyword_num]]
    return key_list
# 训练所有分词文件的tf-idf值
@clock
def train_all_model():
    for i in range(1, 5):
        text_name = '/Users/fanjialiang2401/Desktop/项目实训/VENV_shixun/shixun/jieba分词/txt/segJD{}.txt'.format(i)
        opener = open(text_name, 'r')
        lines = opener.readlines()
        train_model(lines, i)


@clock
def test():
    model, vectorize = load_model()
    weight = model.toarray()
    result = vectorize.vocabulary_.get('蛋糕')
    print(result)
    # print(vectorize.get_feature_names())
    # vectorize = CountVectorizer()
    # word = vectorize.get_feature_names()
    # for i in range(len(weight)):
    #     for j in range(len(word)):
    #         print(word[j],weight[i][j])


def search(words, weight, vectorsize):
    pass


if __name__ == '__main__':
    train_all_model()
    # train_file('segJD1.txt')
    # train(corpus)
    # test()
    # test_file_exist()
    # word_list = ['我', '今天', '吃了', '蛋糕', '很', '好吃'
    #              ]
    # return_result = find_the_better_word(word_list)

    # print(return_result)
    # 保存
    # 获取 词袋模型中的所有词语pr
