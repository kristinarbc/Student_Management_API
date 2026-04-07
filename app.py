from flask import Flask, jsonify, request
from models import db, Student

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studenti.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Kreira bazu pri pokretanju
with app.app_context():
    db.create_all()

# -----------------------------------------------
# 1. GET — svi studenti
# -----------------------------------------------
@app.route("/studenti", methods=["GET"])
def get_studenti():
    studenti = Student.query.all()
    return jsonify([s.to_dict() for s in studenti])

# -----------------------------------------------
# 2. GET sa parametrom — jedan student po ID-ju
# -----------------------------------------------
@app.route("/studenti/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

# -----------------------------------------------
# 3. POST — dodaj novog studenta
# -----------------------------------------------
@app.route("/studenti", methods=["POST"])
def dodaj_studenta():
    podaci = request.get_json()
    novi = Student(
        ime=podaci["ime"],
        prezime=podaci["prezime"],
        indeks=podaci["indeks"],
        ocena=podaci.get("ocena")
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify(novi.to_dict()), 201

# -----------------------------------------------
# 4. PUT — izmeni studenta
# -----------------------------------------------
@app.route("/studenti/<int:id>", methods=["PUT"])
def izmeni_studenta(id):
    student = Student.query.get_or_404(id)
    podaci = request.get_json()
    student.ime = podaci.get("ime", student.ime)
    student.prezime = podaci.get("prezime", student.prezime)
    student.ocena = podaci.get("ocena", student.ocena)
    db.session.commit()
    return jsonify(student.to_dict())

# -----------------------------------------------
# 5. DELETE — obrisi studenta
# -----------------------------------------------
@app.route("/studenti/<int:id>", methods=["DELETE"])
def obrisi_studenta(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"poruka": "Student obrisan"})

if __name__ == "__main__":
    app.run(debug=True)