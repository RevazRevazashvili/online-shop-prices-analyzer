import streamlit as st
import re
from main import find_product
pattern = re.compile(r'[a-zA-Zა-ჰ0-9]+')
with st.form('input'):
    product_name = st.text_input(
        "პროდუქტის დასახელება",
        max_chars=1000
    )
    submit_button = st.form_submit_button(label='მოძებნე')

if submit_button:
    product_name = ' '.join(pattern.findall(product_name))
    products = find_product(product_name)
    if products.shape[0] == 0:
        st.write(f":red[პროდუქტი ვერ მოიძებნა]")
    else:
        st.dataframe(products)