import executor_utils as eu
import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask web server running!'

@app.route('/build_and_run', methods=['POST'])
def build_and_run():
    data = json.loads(request.data)
    if 'code' not in data or 'lang' not in data:
        return 'You should provide both "code" and "data"'
    code = data['code']
    lang = data['lang']
    print 'API go called with code %s in %s' % (code, lang)

    # return jsonify({
    #     'build': 'OKOKOK',
    #     'run': 'ahahahahaha'
    # })
    result = eu.build_and_run(code, lang)
    return jsonify(result)

if __name__ == '__main__':
    eu.load_image()
    app.run(debug=True)