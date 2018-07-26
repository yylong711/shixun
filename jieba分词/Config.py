from app.models import *

# 分词器序号
Ansj_Seg = 1
IKAnalyzer_Seg = 2
Jcseg_Seg = 3
Jieba_Seg = 4

sege_dict = {

    '1': 'jd',
    '2': 'bio',
    '3': 'geo',
    # jd word
    '11': Ansj_Word,
    '12': IKAnalyzer_Word,
    '13': Jcseg_Word,
    '14': IKAnalyzer_Word,

    '111': Ansj_Word,
    '122': IKAnalyzer_Word,
    '133': Jcseg_Word,
    '144': IKAnalyzer_Word,

    # bio abstruct
    '21': Bio_abstruct_word_1,
    '22': Bio_abstruct_word_2,
    '23': Bio_abstruct_word_3,
    '24': Bio_abstruct_word_4,

    # bio_text
    '211': Bio_text_word_1,
    '222': Bio_text_word_2,
    '233': Bio_text_word_3,
    '244': Bio_text_word_4,

    # geo_abstruct
    '31': Geo_abstruct_word_1,
    '32': Geo_abstruct_word_2,
    '33': Geo_abstruct_word_3,
    '34': Geo_abstruct_word_4,

    # geo text_word
    '311': Geo_text_word_1,
    '322': Geo_text_word_2,
    '333': Geo_text_word_3,
    '344': Geo_text_word_4,

}
FIND_SCHEMA = {
    '0': 'find in abstruct_word',
    '1': 'find in all word',
    '2': 'find by keyword',
}

# 词性优先级

WORD_PRIORITY = {
    'nt': 5,
    'vn': 4,
    'v': 3,
    't': 2,
    'n': 5
}

Allowed_attribute = ['nt', 'vn']
