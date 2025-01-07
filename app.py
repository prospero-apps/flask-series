from flask import (Flask, 
                   render_template, 
                   redirect, 
                   url_for, 
                   request, 
                   send_file, 
                   session, 
                   make_response)
import pandas as pd
import os

app = Flask(__name__, template_folder='templates', 
            static_folder='static',
            static_url_path='/')

app.secret_key = 'MY SECRET KEY'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', message='Nice to see you.')

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

@app.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'GET':
        return render_template('personal_info.html')
    elif request.method == 'POST':
        if 'username' in request.form.keys():
            username = request.form['username']
        if 'password' in request.form.keys():
            password = request.form['password']

        if username == 'prospero' and password == 'coder':
            return "You're logged in."
        else:
            return "Wrong username or password!"
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return 'Nothing to display.', 400
    
    file = request.files['file']
    filename = file.filename

    if filename == '':
        return 'No file selected!', 400
    
    if file.content_type.startswith('image/'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return render_template('photo.html', image_url=f"/uploads/{filename}")
    elif file.content_type == 'text/csv':
        df = pd.read_csv(file)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)        
        return df.to_html()
    
    return 'Unsupported file format!', 400

@app.route('/uploads/<filename>')
def serve_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(filepath, mimetype='image/*')

@app.route('/set_personal_data')
def set_personal_data():
    session['first_name'] = 'Jamie'
    session['last_name'] = 'McFee'
    return render_template('index.html', message='Your personal data has been set.')

@app.route('/get_personal_data')
def get_personal_data():
    if 'first_name' in session and 'last_name' in session:
        first_name = session['first_name']
        last_name = session['last_name']
        return render_template('index.html', 
                               message=f'first name: {first_name}, last name: {last_name}')
    else:
        return render_template('index.html', 
                               message='No session found.')
    
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session cleared.')

@app.route('/set_cookie')
def set_cookie():    
    response = make_response(render_template('index.html', message='Cookie set.'))
    response.set_cookie('name', 'my_cookie')
    return response

@app.route('/get_cookie')
def get_cookie():  
    cookie_value = request.cookies['name']
    return render_template('index.html', message=f'Cookie value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():  
    response = make_response(render_template('index.html', message='Cookie removed.'))
    response.set_cookie('name', expires=0)
    return response

@app.template_filter('every_other_letter')
def every_other_letter(word):
    return word[::2]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
