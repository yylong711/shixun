from app import db
from sqlalchemy.ext.declarative import declared_attr


class Sentence(db.Model):
    __tablename__ = 'sentence'

    __table_args__ = (
        db.Index("idx_content", "content", mysql_length=50),
    )
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(3000))

    jieba_word = db.relationship('Jieba_Word', backref='sentence', lazy='dynamic')
    ansj_word = db.relationship('Ansj_Word', backref='sentence', lazy='dynamic')
    jcseg_Word = db.relationship('Jcseg_Word', backref='sentence', lazy='dynamic')
    ikanalyzer_Word = db.relationship('IKAnalyzer_Word', backref='sentence', lazy='dynamic')

    def __repr__(self):
        return self.content


class Jieba_Word(db.Model):
    __tablename__ = 'jieba_word'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))
    # num = db.relationship('Word_num', backref='word', lazy='dynamic')
    def __repr__(self):
        return 'word %r:{},sentence is {}'.format(self.content, self.sentence)


class Ansj_Word(db.Model):
    __tablename__ = 'ansj_word'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))

    # num = db.relationship('Word_num', backref='word', lazy='dynamic')

    def __repr__(self):
        return 'word %r:' % self.sentence


class Jcseg_Word(db.Model):
    __tablename__ = 'jcseg_word'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))

    # num = db.relationship('Word_num', backref='word', lazy='dynamic')

    def __repr__(self):
        return 'word %r:' % self.sentence


class IKAnalyzer_Word(db.Model):
    __tablename__ = 'ikanalyzer_word'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))

    # num = db.relationship('Word_num', backref='word', lazy='dynamic')

    def __repr__(self):
        return 'word %r:' % self.sentence


class Geo_Abstruct_word:
    id = db.Column(db.BigInteger, primary_key=True)
    content = db.Column(db.String(50), index=True)

    @declared_attr
    def article_id(cls):
        return db.Column(db.BigInteger,db.ForeignKey('geo_literature.lit_id'),index=True)

class Bio_Abstruct_word:
    id = db.Column(db.BigInteger, primary_key=True)
    content = db.Column(db.String(50), index=True)

    @declared_attr
    def article_id(cls):
        return db.Column(db.BigInteger,db.ForeignKey('bio_literature.lit_id'),index=True)




class Geo_abstruct_word_1(Geo_Abstruct_word, db.Model):
    __tablename__ = 'geo_abstruct_word_1'

    pass


class Geo_abstruct_word_2(Geo_Abstruct_word, db.Model):
    __tablename__ = 'geo_abstruct_word_2'

    pass


class Geo_abstruct_word_3(Geo_Abstruct_word, db.Model):
    __tablename__ = 'geo_abstruct_word_3'
    pass


class Geo_abstruct_word_4(Geo_Abstruct_word, db.Model):
    __tablename__ = 'geo_abstruct_word_4'
    pass


class Bio_abstruct_word_1(Bio_Abstruct_word, db.Model):
    __tablename__ = 'bio_abstruct_word_1'
    pass


class Bio_abstruct_word_2(Bio_Abstruct_word, db.Model):
    __tablename__ = 'bio_abstruct_word_2'
    pass


class Bio_abstruct_word_3(Bio_Abstruct_word, db.Model):
    __tablename__ = 'bio_abstruct_word_3'
    pass


class Bio_abstruct_word_4(Bio_Abstruct_word, db.Model):
    __tablename__ = 'bio_abstruct_word_4'
    pass


class Literature:
    lit_id = db.Column(db.BigInteger, primary_key=True)
    lit_title = db.Column(db.String(100))
    lit_author = db.Column(db.String(1000))
    lit_kw = db.Column(db.String(1000))
    lit_abstruct = db.Column(db.String(10000))
    lit_text = db.Column(db.Text)
    lit_pub_time = db.Column(db.String(1000))
    lit_publisher = db.Column(db.String(1000))
    lit_is_extract = db.Column(db.Integer)
    lit_type = db.Column(db.String(1000))
    lit_subject = db.Column(db.String(1000))


class Bio_literature(Literature, db.Model):
    __tablename__ = 'bio_literature'

    sentence=db.relationship('Bio_text_sentence',backref='paper',lazy='dynamic')
    # abstruct_word=db.relationship('Bio_Abstruct_word',backref='paper',lazy='dynamic')
    abstruct_word_1=db.relationship('Bio_abstruct_word_1',backref='paper',lazy='dynamic')
    abstruct_word_2=db.relationship('Bio_abstruct_word_2',backref='paper',lazy='dynamic')
    abstruct_word_3=db.relationship('Bio_abstruct_word_3',backref='paper',lazy='dynamic')
    abstruct_word_4=db.relationship('Bio_abstruct_word_4',backref='paper',lazy='dynamic')





class Geo_literature(Literature, db.Model):
    __tablename__ = 'geo_literature'

    sentence=db.relationship('Geo_text_sentence',backref='paper',lazy='dynamic')
    abstruct_word_1=db.relationship('Geo_abstruct_word_1',backref='paper',lazy='dynamic')
    abstruct_word_2=db.relationship('Geo_abstruct_word_2',backref='paper',lazy='dynamic')
    abstruct_word_3=db.relationship('Geo_abstruct_word_3',backref='paper',lazy='dynamic')
    abstruct_word_4=db.relationship('Geo_abstruct_word_4',backref='paper',lazy='dynamic')


# 分开的句子
class Text_sentence:
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(3000))
    # 创建索引 和外键

    # @declared_attr
    # def article_id(cls):
    #
    #     return db.Column(db.BigInteger,db.ForeignKey(), index=True)


class Bio_text_sentence(Text_sentence, db.Model):
    __tablename__ = 'bio_text_sentence'
    article_id=db.Column(db.BigInteger,db.ForeignKey('bio_literature.lit_id'),index=True)

    # 进行反向声明
    Bio_Text_word_1 = db.relationship('Bio_text_word_1', backref='sentence', lazy='dynamic')
    Bio_Text_word_2 = db.relationship('Bio_text_word_2', backref='sentence', lazy='dynamic')
    Bio_Text_word_3 = db.relationship('Bio_text_word_3', backref='sentence', lazy='dynamic')
    Bio_Text_word_4 = db.relationship('Bio_text_word_4', backref='sentence', lazy='dynamic')



class Geo_text_sentence(Text_sentence, db.Model):
    __tablename__ = 'geo_text_sentence'
    article_id=db.Column(db.BigInteger,db.ForeignKey('geo_literature.lit_id'),index=True)

    # 进行反向声明
    Geo_Text_word_1 = db.relationship('Geo_text_word_1', backref='sentence', lazy='dynamic')
    Geo_Text_word_2 = db.relationship('Geo_text_word_2', backref='sentence', lazy='dynamic')
    Geo_Text_word_3 = db.relationship('Geo_text_word_3', backref='sentence', lazy='dynamic')
    Geo_Text_word_4 = db.relationship('Geo_text_word_4', backref='sentence', lazy='dynamic')


# bio_text_word 父类

class Bio_Text_word:
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)

    @declared_attr
    def sentence_id(cls):
        return db.Column(db.Integer,db.ForeignKey('bio_text_sentence.id'),index=True)

    ## 反向声明


    # sentence_id = db.Column(db.BigInteger, db.ForeignKey('bio_text_sentence'))


class Bio_text_word_1(Bio_Text_word, db.Model):
    __tablename__ = 'bio_text_word_1'
    pass


class Bio_text_word_2(Bio_Text_word, db.Model):
    __tablename__ = 'bio_text_word_2'
    pass


class Bio_text_word_3(Bio_Text_word, db.Model):
    __tablename__ = 'bio_text_word_3'
    pass


class Bio_text_word_4(Bio_Text_word, db.Model):
    __tablename__ = 'bio_text_word_4'
    pass


class Geo_Text_word:
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), index=True)

    @declared_attr
    def sentence_id(cls):
        return db.Column(db.Integer, db.ForeignKey('geo_text_sentence.id'))
    # sentence_id = db.Column(db.BigInteger, db.ForeignKey('geo_text_sentence'))


class Geo_text_word_1(Geo_Text_word, db.Model):
    __tablename__ = 'geo_text_word_1'
    pass


class Geo_text_word_2(Geo_Text_word, db.Model):
    __tablename__ = 'geo_text_word_2'
    pass


class Geo_text_word_3(Geo_Text_word, db.Model):
    __tablename__ = 'geo_text_word_3'
    pass


class Geo_text_word_4(Geo_Text_word, db.Model):
    __tablename__ = 'geo_text_word_4'
    pass
