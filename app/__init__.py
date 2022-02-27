"""
coding:utf-8
file: __init__.py.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2022/2/26 23:29
@desc:
"""
from flask import Flask, request
from app.extensions import babel
from app.views.index import idx_bp
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app():
    app = Flask(__name__)
    app.config['BABEL_DEFAULT_LOCALE'] = 'zh'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = basedir + '/translations'
    app.register_blueprint(idx_bp)
    register_extensions(app)

    @babel.localeselector
    def get_local():
        cookie = request.cookies.get('locale')
        if cookie in ['zh', 'en']:
            return cookie
        return request.accept_languages.best_match(app.config.get('BABEL_DEFAULT_LOCALE'))

    return app


def register_extensions(app):
    babel.init_app(app)
