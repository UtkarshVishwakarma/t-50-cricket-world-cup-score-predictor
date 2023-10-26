import streamlit as st
import pickle
import pandas as pd

teams = ['India',
 'Pakistan',
 'New Zealand',
 'Sri Lanka',
 'Australia',
 'South Africa',
 'Bangladesh',
 'England',
 'Netherlands',
 'Afghanistan']

model = pickle.load(open('model.pkl', 'rb'))

st.title("World Cup Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batsman = st.selectbox("Select The Current Batsman", teams)

with col2:
    bowler = st.selectbox("Select The Current Bowler", teams)

col3, col4, col5 = st.columns(3)

with col3:
    runs = st.number_input("Enter Current Score")

with col4:
    wicket_taken = st.number_input("Enter Wicket Taken")

with col5:
    balls = st.number_input("Enter Balls Played")

last_five = st.number_input("Enter The Score of last five overs")

if st.button("Predict"):
    if batsman != bowler:
        try:
            crr = (runs * 6) / balls
            balls_left = 120 - balls
            wicket_left = 10 - wicket_taken

            data = [[batsman, bowler, runs, crr, wicket_left, balls_left, last_five]]
            df = pd.DataFrame(data)

            prediction = model.predict(data)

            st.header(f'Predicted Total Runs Scored - {int(prediction[0])}')

        except:
            st.header("Provided Info Not Valid")