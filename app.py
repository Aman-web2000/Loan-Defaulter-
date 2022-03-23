from email.policy import default
import streamlit as st 
import pandas as pd 
import numpy as np
import pickle
from PIL import Image

pickle_in=open("LoanDefaulter.pkl",'rb')
clf=pickle.load(pickle_in)

def predict(l):
    ans=clf.predict(l)[0]
    return ans


def main():
    html_title="""
    <div style="background-color: midnightblue; padding: 10px;">
    <h1 style="text-align: center; color: aliceblue;">Loan Defaulter Classifier</h1>
    </div>
    """
    st.markdown(html_title,unsafe_allow_html=True)

    st.subheader('Predict if a person will be a loan defaulter or not')

    st.header("Enter the Details Below:")

    income=st.number_input("Enter your Income per Year",min_value=100000,max_value=9000000,step=5000)

    married=st.radio("Martial Status",['married',"single"])

    age=st.slider("Age",min_value=21,max_value=68,step=1)

    car=st.radio("Do You Own a Car",['yes','no'])

    job_exp=st.number_input("Job Experience",min_value=0,max_value=30,step=2)

    house=st.slider("Current House Years",min_value=0,max_value=40,step=2)

    l=[income,married,age,car,job_exp,house]

    input_df=pd.DataFrame(data=[[income,age,married,car,house,job_exp]],columns=['Income','Age','Married/Single','Car_Ownership','CURRENT_HOUSE_YRS','Total_Job_Experience'])

    if st.button('Predict'):
        val=predict(input_df)
        if val==1:
            html_defaulter="""
            <div style="padding: 10px;">
            <h1 style="text-align: center; color:red;">⚠️ Alert! Loan Defaulter</h1>
            </div>
            """
            st.markdown(html_defaulter,unsafe_allow_html=True)
        else:
            html_not_defaulter="""
            <div>
            <h1 style="text-align: center; color:green;">✅Safe to Give Loan</h1>
            </div>
            """
            st.markdown(html_not_defaulter,unsafe_allow_html=True)  

if __name__=="__main__":
    main()
