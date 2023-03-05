
import pymysql
from flask import (Flask, render_template, request, redirect, session, jsonify)


app = Flask(__name__, template_folder='template')
app.secret_key = 'ItShouldBeAnythingButSecret'

dataConection = ['localhost', '']

#Get the connection to the database in mysql  host='localhost', user='root', password='', db='reminders'
def conection():
    return pymysql.connect(host='localhost', user='root', password='', db='reminders')


#Login into de app
@app.route('/login', methods=['POST', 'GET'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        smsUsername = ''
        smsPasswor = ''
        if not username:
            smsUsername = 'missing username!'
        if not password:
            smsPasswor = 'missing password!'

        db = conection()
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * from users WHERE user_name = %s and password=%s", (username, password))
            userLogin = cursor.fetchall()
            db.close()

        if len(userLogin) > 0:
            session['user'] = username
            session['id'] = userLogin[0][0]
            return redirect('/')

        return render_template('login.html', smsUsername=smsUsername, smsPasswor=smsPasswor)

    return render_template('login.html', smsUsername='', smsPasswor='')

#get a reminder by id user
@app.route('/')
def index():
    if ('user' in session):
        db = conection()
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * from reminders WHERE id_user = %s ORDER BY date", (session['id']))
            reminders = cursor.fetchall()
            db.close()
        return render_template("index.html", reminders=reminders)

    return redirect("/login")


#delete a user seccion
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


#allows the user to create a new account, it is validated that the user's name does not
#exist in the application and that the password and confirmation are the same
@app.route('/register', methods=['POST', 'GET'])
def register():

    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if not username or not password or not confirm:
            return redirect('/register')

        if password != confirm:
            return redirect('/register')

        db = conection()
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * from users WHERE user_name = %s", (username))
            user = cursor.fetchall()
        if len(user) > 0:
            return redirect('/register')

        with db.cursor() as cursor:
            cursor.execute("INSERT INTO users(user_name, password) VALUES (%s, %s)",
                           (username, password))
            db.commit()
            db.close()
        return redirect('/login')

    return render_template('register.html')


#create a new reminder
@app.route('/add', methods=['POST', 'GET'])
def add():
    if (request.method == 'POST'):
        title = request.form.get('title')
        description = request.form.get('description')
        date = request.form.get('date')

        if not title or not description or not date:
            return ('/add')

        db = conection()
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO reminders(title, description, date, id_user) VALUES(%s, %s, %s, %s)",
                           (title, description, date,  session['id']))
            db.commit()
            db.close()

        return redirect('/')

    return render_template('add.html')


#delete reminder by id
@app.route('/delete/<id>')
def delete(id):

    print(id)
    db = conection()
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM reminders WHERE id = %s", (id))
        cursor.fetchall()
        db.commit()
        db.close()

    return redirect('/')


@app.route('/update/<id>',  methods=['POST', 'GET'])
def update(id):

    if (request.method == 'POST'):
        title = request.form.get('title')
        description = request.form.get('description')
        date = request.form.get('date')
        db = conection()
        with db.cursor() as cursor:
            cursor.execute("UPDATE reminders set title = %s, description = %s, date =%s WHERE id = %s",
                           (title, description, date, id))
            db.commit()
            db.close()
        return redirect('/')
    else:
        print(id)
        db = conection()
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * from reminders WHERE id = %s ", (id))
            reminder = cursor.fetchall()
            db.close()
        return render_template('edit.html', reminder=reminder)


if __name__ == '__main__':
    app.run(debug=True)
