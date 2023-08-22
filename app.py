import pickle
import streamlit as st
sys.path.insert(1, "requirements.txt")
from streamlit_option_menu import option_menu

# Importing saved models
diabetes_model = pickle.load(open("C:/Users/Mai Bhubhu/Desktop/certification/SIDHARDHAN/projects/diabetes.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/Mai Bhubhu/Desktop/certification/SIDHARDHAN/projects/heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/Mai Bhubhu/Desktop/certification/SIDHARDHAN/projects/parkinsons.sav", 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu("Multi-Disease prediction system",
                           ["Diabetes Prediction",
                            "Heart Disease",                       
                            "About"],
                           icons=['activity', 'balloon-heart-fill', 'arrow-through-heart', 'file-person-fill'],
                           default_index=0)

# Diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('ML diabetes prediction')
    
    # Columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood pressure value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of a person')
   
    # Code for prediction
    diab_diagnosis = ''
    
    # Create a button for prediction
    if st.button('Diabetes Test Result'):
        input_data = [
            [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
             float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
        ]
        diab_prediction = diabetes_model.predict(input_data)
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Diabetes detected'
        else:
            diab_diagnosis = 'Diabetes not detected'
    
    st.success(diab_diagnosis)

if selected == 'Heart Disease':
    st.title('ML Heart Disease prediction')
    
    # Columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of a person')
    with col2:
        sex = st.text_input('Gender of a person')
    with col3:
        chest_pain_type = st.text_input('Does a person have chest pains')
    with col1:
        resting_blood_pressure = st.text_input('Blood pressure value')
    with col2:
        cholestoral = st.text_input('Cholesterol level')
    with col3:
        fasting_blood_sugar = st.text_input('Fasting blood sugar level')
    with col1:
        rest_ecg = st.text_input('Resting electrocardiographic results')
    with col2:
        max_heart_rate = st.text_input('Maximum heart rate achieved')
    with col3:
        exercise_induced_angina = st.text_input('Exercise-induced angina')
    with col1:
        old_peak = st.text_input('old peak value')
    with col2:
        st_slope = st.text_input('ST depression induced by exercise relative to rest')
    with col3:
        num_major_vessels = st.text_input('Number of major vessels colored by fluoroscopy')
    with col1:
        thalassemia = st.text_input('Thalassemia')

    # Code for prediction
    heart_diagnosis = ''
    
    # Create a button for prediction
    if st.button('Heart Disease Test Result'):
        input_data = [
            [float(age), float(sex), float(chest_pain_type), float(resting_blood_pressure),
             float(cholestoral), float(fasting_blood_sugar), float(rest_ecg), float(max_heart_rate),
             float(exercise_induced_angina),float(old_peak), float(st_slope), float(num_major_vessels), float(thalassemia)]
        ]
        heart_prediction = heart_disease_model.predict(input_data)
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'Heart disease detected'
        else:
            heart_diagnosis = 'Heart disease not detected'
    
    st.success(heart_diagnosis)

if selected == "About":
    st.title("About author")
    
    st.write("Name: Bennett Mhlanga")
    st.write("Biography:")
    st.write("Bennett Mhlanga is a dedicated computer science student at the University of Zimbabwe, with a strong interest in data science and data analytics. He is passionate about leveraging data-driven approaches to solve complex problems and make informed decisions.")
    
    st.write("Education:")
    st.write("Bennett is currently pursuing his studies in computer science at the University of Zimbabwe. Through his coursework and practical projects, he is gaining a solid foundation in data science, machine learning, deep learning and data analytics.")
    
    st.write("Certifications:")
    st.write("Bennett has obtained Microsoft certifications in data science and data analytics, showcasing his proficiency in these domains. Additionally, he has pursued other relevant certifications to further enhance his knowledge and skills.")
    
    st.write("Interests:")
    st.write("Bennett's primary interests lie in data science and data analytics within the context of computer science. He enjoys exploring and analyzing complex datasets, developing machine learning models, and applying machine learning techniques to extract meaningful insights.")
    
    st.write("Contact:")
    st.write("You can reach Bennett Mhlanga via email at bennett.mhlanga@students.uz.ac.zw. or bennettmhlanga959@gmail.com")
