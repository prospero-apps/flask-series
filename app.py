from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    app_name = 'Super App'
    age_limit = 13
    numbers = [3, 5, 7, 2, 9]
    return render_template('index.html', app_name=app_name, age_limit=age_limit, numbers=numbers)

@app.route('/contact')
def contact():
    email = 'super.app@gmail.com'
    phone = '111 2222 3333'
    return render_template('contact.html', email=email, phone=phone)

@app.route('/fun_stuff')
def fun_stuff():
    word = 'hello'
    return render_template('fun_stuff.html', word=word)

@app.route('/go_home')
def go_home():
    return redirect(url_for('index'))

@app.template_filter('every_other_letter')
def every_other_letter(word):
    return word[::2]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
