
import random
from flask import Flask, render_template, request, redirect, url_for
from source.database import Database


app = Flask(__name__)
database = Database('database.db')


@app.route('/')
def index():
    return render_template('index.html', users=database.get_all_users(), title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='Over ons')

@app.route('/detail/<int:id>')
def detail(id):
    for gebruiker in database.get_all_users():
        if gebruiker['id'] == id:
            return render_template('detail.html', user=gebruiker, title='Details')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html', title='Toevoegen')
    name = request.form['name']
    age = request.form['age']
    picture = f'https://randomuser.me/api/portraits/{request.form['gender']}/{random.randint(1, 99)}.jpg'
    database.add_user((name, age, picture))
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    user = database.get_user(id)

    if request.method == 'POST':
       name = request.form['name']
       age = request.form['age']
       database.update_user(( name, age, id))
       return redirect(url_for('edit', id=id, user=user, title='Wijzigen'))

    return render_template('edit.html', id=id, user=user, title='Wijzigen')

@app.route('/remove_user/<int:id>', methods=['GET'])
def remove_user(id):
    database.delete_user(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

    