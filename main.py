from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user_id = form_data.get('user-id')
        user_pwd = form_data.get('user-pwd')
        if db.is_login(user_id, user_pwd): # is_login 연결
            return 'Success'
        return 'Fail'
    return render_template('login.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        form_data = request.form
        return 'Success'
    return render_template('join.html')

@app.route('/likes', methods=['GET', 'POST'])
def like():
    if request.method == 'POST':
        db.likes(1)
        return 'Success'
    # TODO : DB -> 
    # SELECT COUNT(user_id) from Likes;
    likes = 0
    return render_template('likes.html', likes=likes)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)