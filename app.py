import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open('/Users/harinathreddy/Desktop/MDPS/savedmodels/diabetes_model.sav', 'rb'))

heartdisease_model = pickle.load(open('/Users/harinathreddy/Desktop/Muldisease/Models/heartdisease_model.sav', 'rb'))

parkinson_model = pickle.load(open('/Users/harinathreddy/Desktop/Muldisease/Models/parkinson_model.sav', 'rb'))


  
#navigation side bar

with st.sidebar:
    
    selected_option = option_menu('Multiple Disease Prediction System', 
                                  
                                  ['Diabetes Prediction', 'Heart disease Prediction', 
                                   'Parksinson disease Prediction'],
                                  
                                  icons = ['activity','heart','person'],
                                  
                                  default_index = 0 )


#diabetes Prediction Page
if (selected_option == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction System')
    
    #getting the input data from the user
    Pregnancies = st.text_input('Number of pregnencies')
    Glucose = st.text_input('Enter glucose level')
    BloodPressure = st.text_input('Enter BP')
    SkinThickness = st.text_input('Enter skin thickness ')
    Insulin = st.text_input('Enter insulin level')
    BMI = st.text_input('Enter BMI')
    DiabetesPedigreeFunction = st.text_input('Enter DPF')
    Age = st.text_input('Enter age')
    
    #code for prediction
    
    diabetes_diagnosis = ''
    
    #button for prediction
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis  = 'The person is diabetic'
        else:
            diabetes_diagnosis  = 'The person is not diabetic'
            
    st.success(diabetes_diagnosis)

#Heart Disease Prediction Page
if (selected_option  == 'Heart disease Prediction'):
    
    #page title
    st.title('Heart disease Prediction System')
    
    
    #getting the input data from user
    age	= st.text_input('Age')
    sex	= st.text_input('Sex')
    cp	= st.text_input('Chest Pain types')
    trestbps = st.text_input('Blood Pressure When at Rest')
    chol = st.text_input('Cholestrol in mg/dl')
    fbs = st.text_input('Blood Pressure when fasting')
    restecg	= st.text_input('Resting Electrocardiographic results')
    thalach	= st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Excercise induced Angina')
    oldpeak	= st.text_input('ST depression induced by excercise')
    slope	= st.text_input('Slope of the peak exercise ST segment')
    ca	= st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    #code for prediction
    
    heart_diagnosis = ''
    
    #button for prediction
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heartdisease_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis  = 'The person is having heart disease'
        else:
            heart_diagnosis  = 'The person does not have any heart disease'
    st.success(heart_diagnosis)



# Parkinson's disease Prediction
if (selected_option  == 'Parksinson disease Prediction'):
    
    #page title
    st.title('Parkinson Disease Prediction System ')
    
    #getting input from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')
        
    #code for prediction
    
    Parkinson_diagnosis = ''
    
    #button for prediction
    
    if st.button('Parkinson Disease Test Result'):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]
        heart_prediction = parkinson_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis  = 'The person is has Parkinson Disease'
        else:
            heart_diagnosis  = 'The person does not have Parkinson Disease'
    st.success(Parkinson_diagnosis)

    
    
    


     
