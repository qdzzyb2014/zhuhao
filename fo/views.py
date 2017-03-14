from flask import render_template, Blueprint
from flask import flash
from .forms import RegisterForm
from .models import Registration


blueprint = Blueprint('fo', __name__, url_prefix='/',)


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        r = Registration.create(
            name=form.name.data,
            company=form.company_name.data,
            job_title=form.position.data,
            contact_way=form.mobile.data,
            main_industry=form.main_industry.data
        )
        flash('{},恭喜您,报名成功'.format(r.name), 'message')
    return render_template('index.html', form=form)
