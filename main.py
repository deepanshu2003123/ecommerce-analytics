import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Product:
    def __init__(self, product_id, name, category, price, rating, discount):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating
        self.discount = discount

class Customer:
    def __init__(self, customer_id, name, email, city):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.city = city

class Order:
    def __init__(self, order_id, customer_id, product_id, quantity, date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.date = date

products = []
customers = []
orders = []

with open("data/products.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = Product(
            row["product_id"],
            row["name"],
            row["category"],
            float(row["price"]),
            float(row["rating"]),
            float(row["discount"])
        )
        products.append(product)

with open("data/customers.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        customer = Customer(
            row["customer_id"],
            row["name"],
            row["email"],
            row["city"]
        )
        customers.append(customer)

with open("data/orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        order = Order(
            row["order_id"],
            row["customer_id"],
            row["product_id"],
            int(row["quantity"]),
            row["date"]
        )
        orders.append(order)

def find_product(name):
    for product in products:
        if product.name.lower() == name.lower():
            return product
    return None

def total_units_sold(product_id):
    total = 0
    for order in orders:
        if order.product_id == product_id:
            total += order.quantity
    return total

def total_revenue(product_id, price):
    revenue = 0
    for order in orders:
        if order.product_id == product_id:
            revenue += order.quantity * price
    return revenue

def is_top_selling(product_id):
    units = total_units_sold(product_id)
    if units >= 5:
        return "⭐ Top Selling Product"
    else:
        return "Regular Product"

def discounted_price(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

def get_product_price(product_id):
    for product in products:
        if product.product_id == product_id:
            return product.price
    return 0

def get_product_category(product_id):
    for product in products:
        if product.product_id == product_id:
            return product.category
    return ""

def top_customers():
    customer_spending = {}
    for order in orders:
        if order.customer_id in customer_spending:
            customer_spending[order.customer_id] += order.quantity * get_product_price(order.product_id)
        else:
            customer_spending[order.customer_id] = order.quantity * get_product_price(order.product_id)
    return customer_spending

def revenue_per_category():
    category_revenue = {}
    for order in orders:
        price = get_product_price(order.product_id)
        category = get_product_category(order.product_id)
        if category in category_revenue:
            category_revenue[category] += order.quantity * price
        else:
            category_revenue[category] = order.quantity * price
    return category_revenue