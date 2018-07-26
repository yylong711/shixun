from . import main
from flask import render_template, request, session, redirect, url_for, flash
from .forms import InputForm, PaperForm
from app.models import *
import pickle
from emotion_analyze.jaccard import de_repetition
from manage import cache
from jieba分词.Config import sege_dict
from .utils import get_result,  ListPagination, sentence_classfiy


# 使用session来减少时间 将sentence_data和select_data 储存在session中
@main.route('/', methods=['GET', 'POST'])
def index():
    form = PaperForm()
    page = request.args.get('page', 1, type=int)
    if form.validate_on_submit():
        # str msg
        sentence_data = form.sentence.data
        # str 1，2，3，4
        select_data = form.select.data
        # str 1 ,2 ,3
        type_data = form.type_select.data
        # abstruct or all 1, 0
        find_data = form.find_select.data
        # set paper_type
        paper_type = sege_dict.get(type_data)
        session['type'] = type_data
        session['find_data'] = find_data
        pagin = get_result(select_data=select_data, sentence_data=sentence_data,
                           type=type_data, is_abstruct=find_data)
        # 存在缓存中的必须是orm对象。。 也就是说get方法的排序也要往后稍稍
        # jd 对京东数据 进行排序处理后存入 pagin
        # if type_data and type_data == '1':
        #     # 范围匹配 去重
        #     if find_data=='1':
        #         sentence_result = [item.sentence.content for item in pagin]
        #         tag_sentence_list = sentence_classfiy(sentence_result)
        #         pagin = de_repetition(tag_sentence_list)
        #     else:
        #         pass
        # pagin = [item.sentence.content for item in pagin]
        # 排序 for pagin 对象 进行返回数据的处理 然后再加入memcached缓存中 时间5分钟
        cache.set('pagin_list', pickle.dumps(pagin), timeout=10 * 60)
    ## get 请求
    else:
        if session.get('key_list'):
            flash('关键词为:{}'.format(session.get('key_list')))
        type_data = session.get('type')
        paper_type = sege_dict.get(type_data)
        if page and type_data:
            pagin = cache.get('pagin_list')
            if pagin:
                pagin = pickle.loads(pagin)
                #
                for each in pagin:
                    db.session.add(each)
            else:
                return render_template('index.html', form=form)
        else:
            return render_template('index.html', form=form)
    # public methods
    # 专业类文献
    if type_data and type_data != '1':
        pagination = ListPagination(pagin, page=page, per_page=5)
        # papers = [item.paper for item in sentence_result]
        sentence_result = pagination.items
        # find_the_better_result(papers,select_data,type_data)
        # print(sentence_result)
        return render_template('index.html', form=form,
                               pagination=pagination, paper_type=paper_type, papers=sentence_result,
                               )
    else:
        # 对sentence进行情感分析后构建pagination  那个在session中还要存一个字段
        #  来表示是全局匹配还是范围匹配
        find_data = session.get('find_data')
        if find_data == '1':
            sentence_result = [item.content for item in pagin]
            tag_sentence_list = sentence_classfiy(sentence_result)
            pagin = de_repetition(tag_sentence_list)
        else:
            #
            pagin = [each for each in pagin]

        pagination = ListPagination(pagin, page=page, per_page=5)
        sentence_result = pagination.items

        form.sentence.data=session.get('sentence_data')
        return render_template('index.html', form=form, sentence_result=sentence_result,
                               pagination=pagination
                               )


@main.route('/show')
def show():
    return render_template('show.html')


@main.route('/reset')
def reset():
    if session.get('key_list'):
        session.pop('key_list')
    if session.get('table_num'):
        session.pop('table_num')
    if session.get('type'):
        session.pop('type')
    print(session.items())
    return redirect(url_for('.index'))


@main.route('/play')
def play():
    return render_template('play.html')


@main.route('/article_content/<string:paper>/<int:id>')
# bio geo
def article_content(paper, id):
    article = None
    # bio类型paper
    if paper == 'bio':
        article = Bio_literature.query.get_or_404(id)
    elif paper == 'geo':
        article = Geo_literature.query.get_or_404(id)
    return render_template('paper_content.html', paper=article)


@main.route('/record')
def record():
    return render_template('_record.html')
    pass
