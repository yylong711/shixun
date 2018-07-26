import numpy as np


def jaccard_similarity(s1, s2):# 对比一对句子需要大概0.05毫秒

    s = s1.strip() + s2.strip()
    s = list(set(s))
    v1 = []
    v2 = []
    for i in s:
        v1.append(int(i in s1))
        v2.append(int(i in s2))
        pass
    vectors = [v1, v2]
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数

    return 1.0 * numerator / denominator


# def print_all_in_txt(s):
#     with open('JD.txt','r',encoding='utf-8')as opener:
#         lines=opener.readlines()
#         for line in tqdm(lines):
#             if(jaccard_similarity(s,line)>=0.6):
#                 print(line)
#                 pass


def de_repetition(sentence_list):
    '''
    :param sentence_list: (sentence,1 or -1)
    :return: sentences list: sentence_content
    '''
    non_repeat_sen=[]
    for sentence,tag in sentence_list:
        canadd=1
        for sen,t in non_repeat_sen:
            if jaccard_similarity(sen,sentence)*tag*t>=0.5:# 相似度为1，则两个句子完全相同，为0，则完全不同
                canadd=0
                break
        if canadd:
            non_repeat_sen.append((sentence,tag))
    return [sen for sen,t in non_repeat_sen]


if __name__ == '__main__':
    # print(jaccard_similarity('快递京东','京东快递'))
    # print(jaccard_similarity('好','好好好好好好好和好好好好好好'))
    # print(jaccard_similarity('威化饼干真好吃','威化饼干好吃'))
    # print(jaccard_similarity('这个口味不怎么好吃','很好吃一直买这个吃'))
    # print_all_in_txt('威化饼干真好吃')

    sentence_list=[('京东快递',1),('快递京东',1),('好',1),('不好',-1),('好好好好好',1),
                   ('好好和好好好',1),
                   # 注意这里，这个分不出来，因为这里的多个好字只相当与一个好字，
                   # 这个句子相当与'好和'，与'好'的相似度为0.5，而我设的去重的相似度为0.7
                   # 最好不要将去重的相似度设为0.5，这样会把很多不怎么相似的句子去除
                   ('威化饼干真好吃',1),('威化饼干真不好吃',-1),('这个口味不怎么好吃',-1),('很好吃一直买这个吃',1)]
    sentence=de_repetition(sentence_list)

    print('\n'.join(sentence))
    pass









