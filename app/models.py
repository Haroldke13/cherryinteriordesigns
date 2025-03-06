





from . import db
from flask_login import UserMixin
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    profile_picture = db.Column(db.String(300), default='static/profile_pics/default.png')

    cart_items = db.relationship('Cart', backref='customer', lazy=True)
    orders = db.relationship('Order', backref='customer', lazy=True)  # Use a unique backref name

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError('Password is not a readable Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def __str__(self):
        return '<Customer %r>' % self.id


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    payment_id = db.Column(db.String(100), nullable=True)
    customer_link = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    billing_detail_id = db.Column(db.Integer, db.ForeignKey('billing_detail.id'), nullable=False)



    def __str__(self):
        return f'<Order {self.id}>'


class BillingDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), default='Kenya', nullable=False)
    address_1 = db.Column(db.String(255), nullable=False)
    address_2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<BillingDetail {self.first_name} {self.last_name}>'
    
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    flash_sale = db.Column(db.Boolean, default=True)
    product_description = db.Column(db.String(10000), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Use a unique attribute (cart_items) as the relationship collection name:
    cart_items = db.relationship('Cart', backref=db.backref('product', lazy=True))
    orders = db.relationship('Order', backref=db.backref('product', lazy=True))

    def __str__(self):
        return '<Product %r>' % self.product_name
    
    



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_link = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    color = db.Column(db.String(50))
    size = db.Column(db.String(50))
    dimensions = db.Column(db.String(100))
    weight = db.Column(db.String(50))

    def __str__(self):
        return '<Cart %r>' % self.id
    


    
class Content(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(2000), nullable=False)
        display = db.Column(db.Text, nullable=False)  # Removed length limit for Text field
        thumbnail = db.Column(db.String(10000), nullable=False)
        excerpt = db.Column(db.Text, nullable=False)  # Removed length limit for Text field
        date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

        def __repr__(self):
            return f'<Content {self.title}>'

class Contact(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(100), nullable=False)
            email = db.Column(db.String(100), nullable=False)
            subject = db.Column(db.String(200), nullable=False)
            message = db.Column(db.Text, nullable=False)
            date_sent = db.Column(db.DateTime, default=datetime.now(timezone.utc))

            def __repr__(self):
                return f'<Contact {self.name}>'
            
            
from datetime import datetime

class SalesLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)  # e.g., "add_to_cart", "payment"
    timestamp = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    account_name = db.Column(db.String(150), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return f"<SalesLog {self.event_type} for customer {self.customer_id}>"