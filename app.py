import streamlit as st
from main import find_product

with st.form('input'):
    product_name = st.text_input(
        "პროდუქტის დასახელება",
        max_chars=1000
    )
    submit_button = st.form_submit_button(label='მოძებნე')

if submit_button:
    find_product(product_name)