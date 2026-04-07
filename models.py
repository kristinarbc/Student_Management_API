from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(100), nullable=False)
    prezime = db.Column(db.String(100), nullable=False)
    indeks = db.Column(db.String(20), unique=True, nullable=False)
    ocena = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "indeks": self.indeks,
            "ocena": self.ocena
        }