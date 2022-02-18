from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/users')
def read_all():
    users = User.get_all_users()
    return render_template('read_all.html', users = users)

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/process', methods=['POST'])
def create():
    user = User.create_user(request.form)

    return redirect(f"/users/{user}")

@app.route('/users/<int:user_id>')
def show(user_id):
    data = {
        'user_id' : user_id
    }
    user = User.get_one_user(data)
    
    return render_template('read_one.html', user = user)

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    data = {
        'user_id' : user_id
    }
    user = User.get_one_user(data)
    
    return render_template('edit.html', user = user)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/users')

@app.route('/users/update', methods=['POST'])
def update_user():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(request.form)
    User.update_user(request.form)
    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(request.form['id'])
    return redirect(f"/users/{request.form['id']}")

if __name__ == '__main__':
    app.run(debug=True)
