from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.home import Home

@app.route('/new/home')
def new_home():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_home.html',user=User.get_by_id(data))

@app.route('/create/home',methods=['POST'])
def create_home():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Home.validate_home(request.form):
        return redirect('/new/home')
    data = {
        "price": int(request.form["price"]),
        "location": request.form["location"],
        "rooms": int(request.form["rooms"]),
        "bathrooms": int(request.form["bathrooms"]),
        "squarefootage": int(request.form["squarefootage"]),
        "user_id": session["user_id"]
    }
    Home.save(data)
    return redirect('/dashboard')

@app.route('/edit/home/<int:id>')
def edit_home(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_home.html",edit=Home.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/home',methods=['POST'])
def update_home():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Home.validate_home(request.form):
        return redirect('/new/home')
    data = {
        "price": int(request.form["price"]),
        "location": request.form["location"],
        "rooms": int(request.form["rooms"]),
        "bathrooms": int(request.form["bathrooms"]),
        "squarefootage": int(request.form["squarefootage"]),
        "id": request.form['id']
    }
    Home.update(data)
    return redirect('/dashboard')

@app.route('/home/<int:id>')
def show_home(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_home.html",home=Home.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/home/<int:id>')
def destroy_home(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Home.destroy(data)
    return redirect('/dashboard')