import streamlit as st
from predict_page import predict_page
from explore_page import explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    predict_page()
else:
    explore_page()
