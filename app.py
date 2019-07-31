from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
   # meal = get_food(request.form['fav_food'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't already taken
    #meal = get_food(request.form['fav_food'])
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in', methods=['GET', 'POST'])
def logged_in():
    #if request.method == 'GET':
    return render_template('logged.html')
   # else:
       # meal = get_food(request.form['fav_food']) 
        #update_food(food, user)
        #print("received POST request!!!!")
        #return render_template('logged.html', fav_food= food, name=user)




@app.route('/logout')
def logout():
    login_session['logged_in'] = False
    return home()



if __name__ == '__main__':
    app.run(debug=True)
