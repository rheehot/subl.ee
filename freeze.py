# -*- coding: utf-8 -*-
import os

from flask_frozen import Freezer
import yaml

from sublee import app, DEFAULT_THEME, THEMES


@app.route('/404.html')
def not_found():
    client = app.test_client()
    response = client.get('/404')
    return response.data


if os.path.exists('../gh-pages'):
    app.config['FREEZER_DESTINATION'] = '../gh-pages'
    app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'runker', 'CNAME']
freezer = Freezer(app, with_static_files=False)


@freezer.register_generator
def css():
    with open(THEMES) as f:
        themes = yaml.load(f)
    for theme in themes.viewkeys():
        if theme == DEFAULT_THEME:
            continue
        yield {'theme': theme}


if __name__ == '__main__':
    freezer.freeze()
