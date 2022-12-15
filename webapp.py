import numpy as np
import pickle
import streamlit as st

# Create function for prediciton
# Load the model
loaded_model = pickle.load(open("model.pkl",'rb'))

@st.cache
def churn_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Customer NOT likely to churn'
    else:
        return 'Customer MOST likely to churn'

def main():
    # giving a title
    st.title('Bank Customer Churn Prediction')
    
    # getting the input data from the user
    CreditScore = st.text_input('Credit Score')

    Age = st.text_input('Age')

    Tenure = st.text_input('Tenure')

    Balance = st.text_input('Balance')

    NumOfProducts = st.selectbox('Number of Products', [1, 2, 3, 4])

    HasCrCard = st.selectbox('Have A Credit Card?', ['Yes','No'])
    if HasCrCard == 'Yes':
        HasCrCard = 1
    else:
        HasCrCard = 0

    IsActive = st.selectbox('Is Active Member', ['Yes','No'])
    if IsActive == 'Yes':
        IsActive = 1
    else:
        IsActive = 0

    EstimatedSalary = st.text_input('Estimated Salary')

    Gender_Male = st.selectbox('Gender', ['Male','Female'])
    if Gender_Male == 'Male':
        Gender_Male = 1
    else:
        Gender_Male = 0
    st.text("If Geography is France, Select the following as 'No'")
    Geography_Germany = st.selectbox('Is Geography Germany?', ['Yes','No'])
    if Geography_Germany == 'Yes':
        Geography_Germany = 1
    else:
        Geography_Germany = 0
    Geography_Spain = st.selectbox('Is Geography Spain?', ['Yes','No'])
    if Geography_Spain == 'Yes':
        Geography_Spain = 1
    else:
        Geography_Spain = 0
    
    # code for Prediction
    my_prediction = ''
    
    # creating a button for Prediction
    if st.button('Predict'):
        my_prediction = churn_prediction([CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActive, EstimatedSalary, Gender_Male, Geography_Germany, Geography_Spain])

    st.success(my_prediction)
    
if __name__ == '__main__':
    main()
