import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

st.title('Heart Disease Prediction System')
st.write('Enter patient details below to predict heart disease risk.')

# 4 Input fields matching your selected attributes
age = st.number_input('Age', min_value=1, max_value=120, value=50)
sex = st.selectbox('Sex (1 = Male, 0 = Female)', [0, 1])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)

if st.button('Predict'):
    input_data = np.array([[age, sex, trestbps, chol]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('Prediction: High risk of Heart Disease')
    else:
        st.success('Prediction: Low risk of Heart Disease')