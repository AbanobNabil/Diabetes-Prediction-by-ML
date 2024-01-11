import pickle
import streamlit as st
import pandas as pd
import requests

# Uplode Data
url = 'https://github.com/AbanobNabil/Diabetes-Prediction-by-ML/raw/main/Diabetes_prediction.sav'
response = requests.get(url)
data = pickle.loads(response.content)

st.title('Diabetes Predicting Web App')
st.info('Simple Diabetes Predictive Application')

st.sidebar.image('https://vectorified.com/images/blood-sugar-icon-23.jpg',width=200)
st.sidebar.header('Feature Selection')


Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')


df=pd.DataFrame({'Pregnancies':[Pregnancies], 'Glucose':[Glucose],'BloodPressure':[BloodPressure],
              'SkinThickness':[SkinThickness],'BMI':[BMI],'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
              'Age':[Age]},index = [0])

Confirm_button = st.sidebar.button('Confirm')
if Confirm_button :
    result = data.predict(df)
    if result == 0:
        st.sidebar.write('The patient does not suffer from diabetes')
        st.sidebar.image('https://img.freepik.com/free-photo/hand-holding-blood-glucose-meter-measuring-blood-sugar-background-is-stethoscope-chart-file_1387-943.jpg?w=1380&t=st=1704193958~exp=1704194558~hmac=883ec1e460103d7cb2e667fa65fd23adedc607b605cc37397fa48501b6182f34',width=300)
    else:
        st.sidebar.write('The patient has diabetes')
        st.sidebar.image('https://img.freepik.com/free-photo/hand-holding-blood-glucose-meter-measuring-blood-sugar-background-is-stethoscope-chart-file_1387-942.jpg?w=1380&t=st=1704194003~exp=1704194603~hmac=1c556d94b187dbce5d20955639a926c5be28445fb7f3b220dda1c8c8ae324f42',width=300)
