from . import api
from flask import request
from flask import Response, session, jsonify
from urllib import parse
from jieba分词.Config import sege_dict
from app.main.utils import request_to_server


@api.route('/get_result/')
def get_result():
    print(request.url)
    sd = request.json
    print(sd)
    return Response('hello world')

# 从url中提取内容
def parse_url(url):
    res = parse.urlparse(url)
    msg = res.query
    data_list = msg.split('&')
    print(data_list)
    select_data = data_list[0].split('=')[1]
    sentence_data = data_list[1].split('=')[1]
    page_id = data_list[2].split('=')[1]
    return select_data,sentence_data,page_id


@api.route('/api/jd/')
def index():
    select_data,sentence_data,page_id=parse_url(url=request.url)
    keyword = None
    if session.get('keyword'):
        if session.get('select_data') == select_data and session.get('sentence_data') == sentence_data:
            keyword = session.get('keyword')
    if not keyword:
        keyword = request_to_server(select_data, sentence_data)
        session['keyword'] = keyword
        session['select_data'] = select_data
        session['sentence_data'] = sentence_data
    table = sege_dict[select_data]
    pagin = table.query.filter(table.content == keyword).limit(10)
    print(pagin)
    pagination = pagin.paginate \
        (page=int(page_id), per_page=5, error_out=False)
    print(pagination)
    result = pagination.items

    print(type(result[0].sentence.content))

    return_content = [each.sentence.content for each in result]
    print(return_content)

    return jsonify({
        'result':return_content,
    })