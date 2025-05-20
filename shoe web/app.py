import streamlit as st
from shoe_store import ShoeStore
from shoe import shoe

store = ShoeStore()
store.add_shoe(shoe(1, "Nike Air Max", 100, 10, "https://example.com/nike-air-max.jpg"))
store.add_shoe(shoe(2,  "Adidas Superstar", 80, 20, "https://example.com/adidassuperstar.jpg"))

st.title("Shoe Store")

st.header("Shoes")
for shoe in store.get_shoes():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(shoe.imge_url, width=100)
    with col2:
        st.write(shoe)

st.header("Add Shoe")
with st.form("add_shoe"):
    id = st.number_input("ID")
    name = st.text_input("Name")
    price = st.number_input("price")
    quantity = st.number_input("Quantity")
    image_url = st.text_input("Image URL")
    submitted = st.form_submit_button("Add Shoe")
    if submitted:
        store.add_shoe(shoe(id, name, price, quantity, image_url))
        st.success("Shoe Added Successfully!")

st. header("Search Shoe")
with st.form("search_shoe"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Search")
    if submitted:
        shoe = store.search_shoe(name)
        if shoe:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(shoe.image_url, width=100)
                with col2:
                    st.write(shoe)
        else:
            st.error("Shoe not found!")


st.header("Shoes")
for shoe in store.get_shoes():
    st.write(shoe)

st.header("Place Order")
with st.form("place_order"):
    customer_name = st.text_input("Customer Name")
    shoe_id = st.number_input("Shoe ID")
    quantity = st.number_input("Quantity")
    submitted = st.form_submit_button("Place Order")
    if submitted:
        order = store.place_order(customer_name, shoe_id, quantity)
        if order:
            st.success("Order placed successfully!")
            st.write(order)
        else:
            st.error("Shoe not found")

st.header("Make Payment")
with st.form("make_payment"):
    order_id = st.number_input("Order ID")
    payment_method = st.selectbox("Payment Method", ["Cash", "Card"])
    amount = st.number_input("Amount")
    submitted = st.form_submit_button("Make Payment")
    if submitted:
        payment = store.make_payment(order_id, payment_method, amount)
        if payment:
            st.success("Payment made successfully!")
            st.write(payment)
        else:
            st.error("Order not found")

            


