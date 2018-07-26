from wtforms import StringField, RadioField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    sentence = StringField('', validators=[DataRequired()], render_kw={
        "placeholder": "请输入语句或关键词"
    })
    select = RadioField('请选择分词器',
                        choices=[('1', 'Ansj分词器'), ('2', 'IKAnalyzer_Seg分词器'), ('3', 'Jcseg_Seg分词器'), ('4', '结巴分词器'), ],
                        validators=[DataRequired()]
                        )
    submit = SubmitField('提交')


class PaperForm(FlaskForm):
    sentence = StringField('请输入语句或者关键词', validators=[DataRequired()])
    select = SelectField('请选择分词器', choices=[('1', 'Ansj分词器'), ('2', 'IKAnalyzer_Seg分词器'), ('3', 'Jcseg_Seg分词器'),
                                            ('4', '结巴分词器'), ], validators=[DataRequired()])
    find_select = SelectField('请选择查找模式', choices=[('0', '全文匹配'), ('1', '范围匹配'), ('2', '精确匹配(推荐)')],
                              validators=[DataRequired()])
    type_select = SelectField('请选择查找类型', choices=[('1', '京东'), ('2', '生物类文献'), ('3', '地质类文献')],
                              validators=[DataRequired()])
    submit = SubmitField('搜索')
