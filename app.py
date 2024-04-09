# Gig-Backend/app.py

from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialization of app
app = Flask(__name__)
BASEDIR = os.path.join(os.path.dirname(__file__))

CORS(app)

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    pickup_location = db.Column(db.String(255), nullable=False)
    delivery_location = db.Column(db.String(255), nullable=False)
    delivery_time = db.Column(db.String(255), nullable=False)
    delivery_date = db.Column(db.String(255), nullable=False)

    def __init__(self, description, contact, pickup_location, delivery_location, delivery_time, delivery_date):
        self.description = description
        self.contact = contact
        self.pickup_location = pickup_location
        self.delivery_location = delivery_location
        self.delivery_time = delivery_time
        self.delivery_date = delivery_date

# Order schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'contact', 'pickup_location', 'delivery_location', 'delivery_time', 'delivery_date')

Order_Schema = OrderSchema()
Orders_Schema = OrderSchema(many=True)

with app.app_context():
    db.create_all()

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password)  # Hash the password
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):  # Check password using check_password_hash
        return jsonify({'message': 'Invalid email or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

# Create a new order
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(
        description=data['description'],
        contact=data['contact'],
        pickup_location=data['pickup_location'],
        delivery_location=data['delivery_location'],
        delivery_time=data['delivery_time'],
        delivery_date=data['delivery_date']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(Order_Schema.dump(order)), 201

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(Orders_Schema.dump(orders)), 200

# View orders
@app.route('/view_orders', methods=['GET'])
def view_orders():
    return redirect(url_for('get_orders'))

# Get a specific order
@app.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify(Order_Schema.dump(order)), 200

# Update an order
@app.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    data = request.get_json()
    order.description = data['description']
    order.contact = data['contact']
    order.pickup_location = data['pickup_location']
    order.delivery_location = data['delivery_location']
    order.delivery_time = data['delivery_time']
    order.delivery_date = data['delivery_date']
    db.session.commit()
    return jsonify(Order_Schema.dump(order)), 200

# Delete an order
@app.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
