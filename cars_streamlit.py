from pathlib import Path
import pandas as pd
import streamlit as st
import numpy as np
import pymongo

cars_df = pd.read_csv('./data/data.csv')

# get cars dataset
client = pymongo.MongoClient('mongodb+srv://Soyda:Azerty12!@techiasandbox.idmzy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', 27017)
db = client.CarsData
cars_db = db.carsdb

st.title('Cars dataset')

st.write(cars_df)

cars_filtered = st.container()

def select_change(df,col,row):
    with cars_filtered :
        mask_to_display = df[col] == row
        st.dataframe(data=df[mask_to_display])

st.sidebar.subheader('Cars')

constructor = st.sidebar.selectbox('Search by contructor', cars_db.distinct('Make'))

model = st.sidebar.selectbox('Search by model', cars_db.distinct('Model', {'Make': constructor}))

car_to_print = cars_db.find({ "$and" : [{"Make": constructor}, {"Model": model}]}, {"_id":0, "Make":1, "Model":1, "Vehicle Style": 1, "Year": 1, "Engine HP": 1, "Engine Cylinders": 1, "Highway L/100km": 1, "City L/100km": 1 })

for car in car_to_print:
    st.write(f"La {car['Make']} {car['Model']} {car['Vehicle Style']} de {car['Year']} a {car['Engine HP']} chevaux et {car['Engine Cylinders']} cylindres. Sa consommation sur autoroute est de {car['Highway L/100km']} L au 100 km et de {car['City L/100km']} L au 100 km en ville.")
    
with st.sidebar.form(key='my_form'):
    st.write("Here you can add a new car to the list !")
    make_input = st.text_input(label="Enter the car's brand")
    model_input = st.text_input(label="Enter the car's model")
    year_input = st.text_input(label="Enter the car's year")
    hp_input = st.text_input(label="Enter the car's horsepower")
    cylinders_input = st.text_input(label="Enter the car's cylinders")
    submit_button = st.form_submit_button(label="Submit")


