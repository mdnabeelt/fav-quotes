from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:nabeel786@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://cgduthyvjgjdrn:a39131ea15a34c61ae6a127f7cf18b8d1b96e6dbfd8cdd3fe855fa567c01b51c@ec2-52-6-77-239.compute-1.amazonaws.com:5432/dpccoe8k9dpu2'
app.config['SQLALCHEMY_TRACK_MODIFIACTIONS']=False

db=SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods = ['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
