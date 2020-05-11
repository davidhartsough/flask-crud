from flask import Flask, render_template, request, jsonify, redirect

from db import close_db
from things import get_all_things, get_thing, create_thing, update_thing, delete_thing

app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    close_db()


@app.route("/")
def index():
    # list all the things :: READ
    return render_template('list.html', things=get_all_things())


@app.route("/thing/<int:id>")
def detail(id):
    # detail of one thing :: READ
    if id is None:
        return redirect("/")
    thing = get_thing(id)
    if thing is None:
        return redirect("/")
    return render_template('detail.html', thing=thing)


@app.route("/new")
def new():
    # form for making a new thing :: CREATE
    return render_template('new.html')


@app.route('/create', methods=['POST'])
def create():
    # make a new thing :: CREATE
    title = request.form['title']
    stuff_list = request.form.getlist('stuff')
    stuff_string = ",".join(stuff_list)
    num = int(request.form['num'])
    create_thing(title, stuff_string, num)
    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
    # form for editing a thing :: UPDATE
    if id is None:
        return redirect("/")
    thing = get_thing(id)
    if thing is None:
        return redirect("/")
    return render_template('edit.html', thing=thing)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    # edit a thing :: UPDATE
    if id is None:
        return redirect("/")
    title = request.form['title']
    stuff_list = request.form.getlist('stuff')
    stuff_string = ",".join(stuff_list)
    num = int(request.form['num'])
    update_thing(id, title, stuff_string, num)
    return redirect("/")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # remove a thing :: DELETE
    if id is None:
        return redirect("/")
    delete_thing(id)
    return redirect("/")


@app.route("/api/things")
def api_get_things():
    # list of all the things :: READ
    return jsonify(things=get_all_things())


@app.route("/api/thing/<int:id>")
def api_get_thing(id):
    # detail of one thing :: READ
    return jsonify(thing=get_thing(id))


if __name__ == "__main__":
    app.run(debug=True)
