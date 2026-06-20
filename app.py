import streamlit as st
from main import products, customers, orders
from main import find_product, total_units_sold, total_revenue
from main import is_top_selling, discounted_price, get_product_price
from main import get_product_category, top_customers, revenue_per_category

st.set_page_config(page_title="Ecommerce Analytics", layout="wide")
st.title("🛒 Ecommerce Product Analytics System")
st.write("---")

# Search Section
st.subheader("🔍 Search Product")

# Show available products
with st.expander("📋 Click here to see all available products"):
    for i, product in enumerate(products):
        st.write(str(i+1) + ".", product.name, "—", product.category)

search_name = st.text_input("Enter Product Name:")

if search_name:
    product = find_product(search_name)
    if product:
        st.success("Product Found!")
        st.write("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📦 Product Details")
            st.write("**Product ID:**", product.product_id)
            st.write("**Name:**", product.name)
            st.write("**Category:**", product.category)
            st.write("**Original Price:** Rs.", int(product.price))
            st.write("**Discount:**", int(product.discount), "%")
            st.write("**Discounted Price:** Rs.", int(discounted_price(product.price, product.discount)))
            st.write("**Rating:**", product.rating, "⭐")

        with col2:
            st.subheader("📊 Sales Analytics")
            units = total_units_sold(product.product_id)
            revenue = total_revenue(product.product_id, product.price)
            status = is_top_selling(product.product_id)
            st.write("**Total Units Sold:**", units)
            st.write("**Total Revenue:** Rs.", int(revenue))
            st.write("**Status:**", status)

    else:
        st.error("Product not found! Please check the name.")

st.write("---")

# Dashboard Section
st.subheader("📈 Overall Dashboard")

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Total Products", len(products))

with col4:
    st.metric("Total Customers", len(customers))

with col5:
    st.metric("Total Orders", len(orders))

st.write("---")

# Revenue Per Category Section
st.subheader("💰 Revenue Per Category")
category_revenue = revenue_per_category()
for category in category_revenue:
    st.write("**" + category + ":** Rs.", int(category_revenue[category]))

st.write("---")

# Top Customers Section
st.subheader("👑 Top Customers")
customer_spending = top_customers()
sorted_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
for i, (customer_id, spending) in enumerate(sorted_customers[:5]):
    for customer in customers:
        if customer.customer_id == customer_id:
            st.write(str(i+1) + ".", customer.name, "→ Rs.", int(spending))