from flask import Flask
from flask import *
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def catbook_profile(id):
	cat = get_cat(id)
	return render_template("cat.html",cat=cat)

@app.route('/AddCat', methods=['GET', 'POST'])
def AddCat():
	if request.method == 'GET':
		return render_template('AddCat.html')
	else:
		name = request.form['CatName']
		create_cat(name)
		return redirect(url_for('catbook_home'))
	

if __name__ == '__main__':
   app.run(debug = True)
