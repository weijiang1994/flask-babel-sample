"""
coding:utf-8
file: index.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2022/2/26 23:44
@desc:
"""
from flask import Blueprint, render_template, make_response, redirect, request, url_for
from flask_babel import gettext
idx_bp = Blueprint('index', __name__)


@idx_bp.route('/')
@idx_bp.route('/index')
def index():
    content = gettext('This is a flask-babel sample application')
    return render_template('index.html', content=content)


@idx_bp.route('/set-locale/<language>')
def set_locale(language):
    resp = redirect(request.referrer)
    if language:
        resp.set_cookie('locale', language, max_age=30 * 24 * 60 * 60)
    return resp
