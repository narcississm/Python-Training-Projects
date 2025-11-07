from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form['content']
        if note_content.strip():
            new_note = Note(content=note_content)
            try:
                db.session.add(new_note)
                db.session.commit()
                return redirect('/')
            except:
                return 'Not eklenirken hata oluştu.'
    else:
        notes = Note.query.order_by(Note.date_created.desc()).all()
        return render_template('index.html', notes=notes)

@app.route('/delete/<int:id>')
def delete(id):
    note_to_delete = Note.query.get_or_404(id)
    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Not silinirken hata oluştu.'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        note.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Not güncellenirken hata oluştu.'
    else:
        return render_template('update.html', note=note)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
