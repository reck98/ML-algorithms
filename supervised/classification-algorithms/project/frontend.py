import streamlit as st
import numpy as np
import pickle

# Load your trained model (make sure you saved it earlier)
model = pickle.load(
    open(
        "/run/media/reck98/Others/Development/ML_NLP_DL/Ml-algorithms/supervised/classification-algorithms/project/modelFinal.pkl",
        "rb",
    )
)

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

# ------------------ INPUT FIELDS ------------------

Age = st.slider("Age", -3.0, 3.0, 0.0)
RestingBP = st.slider("RestingBP", -3.0, 4.0, 0.0)
Cholesterol = st.slider("Cholesterol", -3.0, 7.0, 0.0)
FastingBS = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
MaxHR = st.slider("Max Heart Rate", -3.0, 3.0, 0.0)
Oldpeak = st.slider("Oldpeak", -3.0, 6.0, 0.0)

Sex_M = st.selectbox("Sex (Male=1, Female=0)", [0, 1])

ChestPainType_ATA = st.checkbox("Chest Pain ATA")
ChestPainType_NAP = st.checkbox("Chest Pain NAP")
ChestPainType_TA = st.checkbox("Chest Pain TA")

RestingECG_Normal = st.checkbox("ECG Normal")
RestingECG_ST = st.checkbox("ECG ST")

ExerciseAngina_Y = st.selectbox("Exercise Angina", [0, 1])

ST_Slope_Flat = st.checkbox("ST Slope Flat")
ST_Slope_Up = st.checkbox("ST Slope Up")

# ------------------ PREPARE INPUT ------------------

input_data = np.array(
    [
        [
            Age,
            RestingBP,
            Cholesterol,
            FastingBS,
            MaxHR,
            Oldpeak,
            Sex_M,
            int(ChestPainType_ATA),
            int(ChestPainType_NAP),
            int(ChestPainType_TA),
            int(RestingECG_Normal),
            int(RestingECG_ST),
            ExerciseAngina_Y,
            int(ST_Slope_Flat),
            int(ST_Slope_Up),
        ]
    ]
)

# ------------------ PREDICTION ------------------

if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
