from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/help')
def help():
    return '<h2>Help - learn how to use this page!</h2>'

@app.route('/show/<id>')
def show_id(id):
    return f'The selected id is {id}. Recommended format: p_{id}.'

@app.route('/introduce/<name>/<city>/<age>')
def introduce(name, city, age):
    return f'This is {name} from {city}, aged {age}.'

@app.route('/sum/<num1>/<num2>')
def add_numbers(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/sumcast/<num1>/<num2>')
def add_numbers_cast(num1, num2):
    return f'{num1} + {num2} = {int(num1) + int(num2)}'

@app.route('/sumtype/<int:num1>/<int:num2>')
def add_numbers_type(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/concatenate')
def concatenate():
    word1 = request.args['word1']
    word2 = request.args['word2']
    return f'{word1} {word2}'

@app.route('/concatenate_checked')
def concatenate_checked():
    if 'word1' in request.args and 'word2' in request.args:
        word1 = request.args['word1']
        word2 = request.args['word2']
        return f'{word1} {word2}'
    else:
        return 'One or more URL parameters are missing.'
    
@app.route('/concatenate_with_get')
def concatenate_with_get():
    word1 = request.args.get('word1', '')
    word2 = request.args.get('word2', '')
    return f'{word1} {word2}'

@app.route('/help_post', methods=['POST'])
def help_post():
    return 'Handled requests: POST'

@app.route('/help_get', methods=['GET'])
def help_get():
    return 'Handled requests: GET'

@app.route('/help_get_post', methods=['GET', 'POST'])
def help_get_post():
    return 'Handled requests: GET, POST'

@app.route('/help_get_post_put_delete', methods=['GET', 'POST', 'PUT', 'DELETE'])
def help_all_four():
    return 'Handled requests: GET, POST, PUT, DELETE'

@app.route('/help_diff', methods=['GET', 'POST', 'PUT', 'DELETE'])
def help_diff():
    if request.method == 'GET':
        return 'This is a GET request.'
    elif request.method == 'POST':
        return 'This is a POST request.'
    elif request.method == 'PUT':
        return 'This is a PUT request.'
    elif request.method == 'DELETE':
        return 'This is a DELETE request.'
    
@app.route('/help_default_status_code', methods=['GET'])
def help_default_status_code():
    return 'Default status code'

@app.route('/help_202', methods=['GET'])
def help_202():
    return 'Status code: 202', 202

@app.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response.')
    response.status_code = 201
    response.headers['content-type'] = 'text/plain'
    response.content_length = 500
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
