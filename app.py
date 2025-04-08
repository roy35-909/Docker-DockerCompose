# app.py
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/')
def home():
    counter = Counter.query.first()
    if not counter:
        counter = Counter(count=0)
        db.session.add(counter)
        db.session.commit()
    return render_template('index.html', count=counter.count)

@app.route('/increment', methods=['POST'])
def increment():
    counter = Counter.query.first()
    counter.count += 1
    db.session.commit()
    return jsonify({'count': counter.count})

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)