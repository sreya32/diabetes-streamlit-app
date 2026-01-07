if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure,
                             SkinThickness, Insulin, BMI, DPF, Age]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Diabetic")
    else:
        st.success("Not Diabetic")
