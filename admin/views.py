from flask_admin.contrib.sqla import ModelView


class UserRegisterView(ModelView):
    can_delete = True
    can_edit = True
    can_export = True

    column_list = [
        'name',
        'company',
        'job_title',
        'contact_way',
        'main_industry'
    ]

    export_types = ['xlsx']

    column_labels = {
        'name': '姓名',
        'company': '公司名称',
        'job_title': '职称',
        'contact_way': '联系方式',
        'main_industry': '主营产业'
    }
