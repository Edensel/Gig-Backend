# from flask_sqlalchemy import sqlalchemy
# from flask_marshmallow import Marshmallow


# db = sqlalchemy(app)
# ma = Marshmallow(app)


# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#     contact = db.Column(db.Integer (10), nullable=False)
#     pickup_location = db.Column(db.String(255), nullable=False)
#     delivery_location = db.Column(db.String(255), nullable=False)
#     delivery_time = db.Column(db.String(255), nullable=False)
#     delivery_date = db.Column(db.String(255), nullable=False)

#     def __init__(self, description, contact, pickup_location, delivery_location, delivery_time, delivery_date):
#         self.description = description
#         self.contact = contact
#         self.pickup_location = pickup_location
#         self.delivery_location = delivery_location
#         self.delivery_time = delivery_time
#         self.delivery_date = delivery_date

# class OrderSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'description', 'contact', 'pickup_location', 'delivery_location', 'delivery_time', 'delivery_date')

# Order_Schema = OrderSchema()
# Orders_Schema = OrderSchema(many=True)


