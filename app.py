import urltools
from flask import Flask, request
from flask.helpers import make_response
from flask.json import jsonify

from store import MemoryStore

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # encode utf-8

store = MemoryStore()


@app.route('/stories/<page_id>')
def show_tags(page_id):
    page = store.get_page(int(page_id))
    if page:
        return jsonify(page.to_json())
    return make_response('Not Found', 404)


@app.route('/stories', methods=['POST'])
def register_url():
    url_param = request.args.get('url')
    if not url_param:
        return make_response("url param is missing", 400)  # bad request

    # TODO: advanced input validation
    # https://validators.readthedocs.io/en/latest/#module-validators.url
    # https://github.com/django/django/blob/master/django/core/validators.py#L74

    clean_url = urltools.normalize(url_param)

    # create page
    page = store.create_page(clean_url)
    if page:
        return make_response(str(page.id), 201)  # Created

    return jsonify({'status': 'Url already exist'})
