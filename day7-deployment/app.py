import streamlit as st
import pandas as pd
import pickle
import os

# path model (lebih aman)
model_path = os.path.join(os.path.dirname(__file__), '..', 'day5-modeling', 'model.pkl')

# load model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

st.title("Bitcoin Price Prediction 💰")
st.write("Input data untuk prediksi harga Bitcoin")

# input user
lag1 = st.number_input("Harga kemarin", value=30000.0)
lag2 = st.number_input("Harga 2 hari lalu", value=29500.0)
lag3 = st.number_input("Harga 3 hari lalu", value=29000.0)
ma7 = st.number_input("MA 7 hari", value=30000.0)
ma30 = st.number_input("MA 30 hari", value=28000.0)
volatility = st.number_input("Volatility", value=1000.0)

# prediksi
if st.button("Predict"):
    data = [[lag1, lag2, lag3, ma7, ma30, volatility]]
    prediction = model.predict(data)

    st.success(f"Predicted Bitcoin Price: ${prediction[0]:,.2f}")