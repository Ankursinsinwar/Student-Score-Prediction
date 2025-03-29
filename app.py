import streamlit as st
import pickle
import numpy as np

with open('student_score.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Student Exam Score Predictor')

hours_studied = st.number_input('Hours Studied', min_value=0, max_value=10, value=5)
Practical_test = st.number_input('Number of Practice Tests Taken', min_value=0, max_value=10, value=5)
attendance_rate = st.number_input('Attendance Rate (%)', min_value=0, max_value=100, value=50)
sleep_hours = st.number_input('Sleep Hours', min_value=0, max_value=10, value=8)

if st.button('Predict Exam Score'):
    features = np.array([[hours_studied, Practical_test, attendance_rate, sleep_hours]])
    predicted_score = model.predict(features)
    st.write(f'Predicted Exam Score: {predicted_score[0]/100:.2f}')
