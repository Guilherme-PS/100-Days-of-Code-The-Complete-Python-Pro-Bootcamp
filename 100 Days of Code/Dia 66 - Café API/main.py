from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rd

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")

# Retorna um café aleatório.
@app.route("/random", methods=["GET", "POST"])
def random():
    random_cafe = rd.choice(Cafe.query.all())

    return jsonify(id=random_cafe.id,
                   name=random_cafe.name,
                   urls={"img_url": random_cafe.img_url,
                         "map_url": random_cafe.map_url},
                   location=random_cafe.location,
                   amenities={"has_sockets": bool(random_cafe.has_sockets),
                              "has_toilet": bool(random_cafe.has_toilet),
                              "has_wifi": bool(random_cafe.has_wifi),
                              "can_take_calls": bool(random_cafe.can_take_calls)},
                   seats=random_cafe.seats,
                   coffee_price=random_cafe.coffee_price)

# Retorna todos os cafés.
@app.route("/all", methods=["GET", "POST"])
def all():
    query = Cafe.query.all()

    all_cafe= []

    for item in query:
        item = dict(item.__dict__)
        del item["_sa_instance_state"]

        all_cafe.append(item)

    return jsonify(cafes=all_cafe)

# Retorna cafés por localização.
@app.route("/search", methods=["GET", "POST"])
def search():
    loc = request.args.get("loc")
    query = Cafe.query.filter_by(location=loc).all()

    if query:
        all_cafe= []

        for item in query:
            item = dict(item.__dict__)
            del item["_sa_instance_state"]

            all_cafe.append(item)

        return jsonify(cafes=all_cafe)

    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

# Adiciona um café.
@app.route("/add", methods=["GET", "POST"])
def add():
    db.session.add(Cafe(name=request.form.get("name"),
                        img_url=request.form.get("img_url"),
                        map_url=request.form.get("map_url"),
                        location=request.form.get("location"),
                        has_sockets=bool(request.form.get("sockets")),
                        has_toilet=bool(request.form.get("toilet")),
                        has_wifi=bool(request.form.get("wifi")),
                        can_take_calls=bool(request.form.get("calls")),
                        seats=request.form.get("seats"),
                        coffee_price=request.form.get("price")))

    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})

# Atualiza um café pelo ID.
@app.route("/update/<int:id_cafe>", methods=["GET", "PATCH"])
def update(id_cafe):
    query = db.session.get(Cafe, id_cafe)

    if query:
        query.coffee_price = request.args.get("new-price")
        db.session.commit()

        return jsonify(response={"success": "Successfully updated the price."}), 200

    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# Remove um café pelo ID.
@app.route("/report/<int:id_cafe>", methods=["GET", "DELETE"])
def delete(id_cafe):
    if request.args.get("api-key") == "TopSecretAPIKey":
        query = db.session.get(Cafe, id_cafe)

        if query:
            db.session.delete(query)

            db.session.commit()

            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api-key."), 404


if __name__ == '__main__':
    app.run(debug=True)
