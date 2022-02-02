import streamlit as st
# import numpy as np
import pickle


model = pickle.load(open("random_forest_regression_model.pkl", 'rb'))
st.title("Car Price Predictor")
st.text("project - Regression, model - Random Forest Regressor")
# if st.button("View code"):

Year = st.text_input("Enter the Number of Years")
Present_Price=st.text_input("Enter the Present price of your car in lakh like (5.5)")
Kms_Driven=st.text_input("Enter the Number of Kms driven")
# Kms_Driven2=np.log(Kms_Driven)
Owner=st.selectbox('What is your owner rank?',("0", "1", "2"))
Fuel_Type_Petrol=st.selectbox('what is your fuel type',("Petrol", "Diesel"))
if Fuel_Type_Petrol == 'Petrol':
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel=0
else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1

Seller_Type_Individual=st.selectbox('What is your Seller Type',("Individual", "Agency" ))
if Seller_Type_Individual=='Individual':
    Seller_Type_Individual=1
else:
    Seller_Type_Individual=0

Transmission_Mannual=st.selectbox("what is your Car's transmission type",("Mannual","Automatic"))
if Transmission_Mannual=='Mannual':
    Transmission_Mannual=1
else:
    Transmission_Mannual=0

if st.button("Know your car price"):
    prediction=model.predict([[Present_Price,(Kms_Driven),Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output<0:
        st.header("Sorry you cannot sell your car")
    else:
        st.header(f"The Predicted Price of your Car is Rs {output} lakh")
