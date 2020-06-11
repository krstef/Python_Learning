from flask import Flask, jsonify, request, Response, json
#from views import bookstore_views
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # calls constructor for creating global Flask application object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ekrstef/Work/repos/Python_Learning/Flask/BookStoreApp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# a pp.register_blueprint(bookstore_views.simple_view) TODO -> create blueprints when done

books = [
    {
        'name': "Code Complete: A Practical Handbook of Software Construction",
        'price': 25,
        'book_id': 8000
    },
    {
        'name': "Clean Code",
        'price': 30,
        'book_id': 8001
    }
]
BOOK_OBJ_KEYS = ["name", "price", "book_id"]
BOOK_PRICE_KEY = "price"


# ***************** Helper methods ***************** #
def valid_book_object(book_obj: dict) -> bool:
    # TODO replace whole function with comprehension
    status_flag = True
    for key in book_obj.items():
        if key[0] not in ["name", "price", "book_id"]:
            status_flag = False
    return status_flag


def valid_book_price(book_obj: dict) -> bool:
    status_flag = False
    for key in book_obj.items():
        if key[0] == BOOK_PRICE_KEY:
            status_flag = True
    return status_flag

# ***************** GET request ***************** #
@app.route("/")
def main_view():
    return "Hi baby"


@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id):
    return_book = {}
    for book in books:
        if book["book_id"] == book_id:
            return_book = {'name': book["name"], 'price': book["price"]}
    return jsonify(return_book)

# ***************** POST request ***************** #
@app.route('/books', methods=['POST'])
def add_book():
    req = request.get_json()
    response = Response("", 201, mimetype='application/json')
    # mimetype says client what kind of response we're sending -> we're sending json
    if valid_book_object(req):
        books.append(req)
        response.headers['Location'] = "/books/" + "someHashedValue"
        return response
    else:
        response.status_code = 404  # 400 == BAD REQUEST
        return response

# ***************** PUT/PATCH requests ***************** #
@app.route("/books/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    req = request.get_json()
    response = Response("", status=204)
    # Add some logic for checking valid input
    item_exist = False
    for book in books:
        if book_id == book["book_id"]:
            item_exist = True
            book.update(req)  # update only existing book
    # according to PUT definition -> if data does not exist, it should be appended
    if not item_exist:
        new_book = {"name": req["name"], "price": req["price"], "book_id": book_id}
        books.append(new_book)
    return response


@app.route("/books/<int:book_id>", methods=['PATCH'])
def update_book_price(book_id):
    req = request.get_json()
    item_exist = False
    for book in books:
        if book_id == book["book_id"]:
            item_exist = True
            book.update(req)  # update only existing book
    if not item_exist:
        return Response("", status=400)  # Bad request -> invalid request message
    else:
        return Response("", status=204)  #

# ***************** DELETE requests ***************** #
@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    item_deleted = False
    for book in books:
        if book_id == book["book_id"]:
            books.remove(book)
            item_deleted = True
    if item_deleted:
        return Response("", status=204)  #
    else:
        err = {"error": "Book with requested ID does not exist"}
        return Response(json.dumps(err), status=400, mimetype='application/json')


# ***************** DataBase implementation ***************** #
db = SQLAlchemy(app)


class BooksDataBase(db.Model):
    __tablename__ = books
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)


if __name__ == "__main__":
    app.run(debug=True)  # starting Flask app
