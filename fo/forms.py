from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired


MESSAGE = '这项不能为空'


class RegisterForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(MESSAGE)])
    company_name = StringField('公司名称', validators=[DataRequired(MESSAGE)])
    position = StringField('职称')
    mobile = TelField('手机号', validators=[DataRequired(MESSAGE)])
    main_industry = StringField('主营产业', validators=[DataRequired(MESSAGE)])
