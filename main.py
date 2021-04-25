import pandas as pd
import streamlit as st
from streamlit import subheader, sidebar, bar_chart, dataframe, write

write("""
# Diabetes Detection
Detect if someone has diabetes using Machine Learning and Python
""")

df = pd.read_csv('C:/Users/Rishabh/PycharmProjects/pythonProject/diabetes.csv')


subheader('Data Information')

dataframe(df)

write(df.describe())

chart = bar_chart(df)

X = df.iloc[:, 0:8].values
Y = df.iloc[:, -1].values

def get_user_input():
    pregnancies = sidebar.slider('pregnancies', 0, 17, 3)
    glucose = sidebar.slider('glucose', 0, 199, 117)
    blood_pressure = sidebar.slider('blood_pressure', 0, 122, 72)
    skin_thickness = sidebar.slider('skin_thickness', 0, 99, 23)
    insulin = sidebar.slider('insulin', 0.0, 846.0, 30.5)
    BMI = sidebar.slider('BMI', 0.0, 67.1, 32.0)
    Diabetes_Pedigree_Function = sidebar.slider('Diabetes_Pedigree_Function', 0.078, 2.42, 0.3725)
    age = sidebar.slider('age', 23, 81, 29)

    user_data = {'pregnancies': pregnancies,
                 'glucose': glucose,
                 'blood_pressure': blood_pressure,
                 'skin_thickness': skin_thickness,
                 'insulin': insulin,
                 'BMI': BMI,
                 'Diabetes_Pedigree_Function': Diabetes_Pedigree_Function,
                 'age': age}
    features = pd.DataFrame(user_data, index=[0])
    return features


user_input = get_user_input()

subheader('User Input: ')
write(user_input)
