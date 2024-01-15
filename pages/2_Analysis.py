import streamlit as st
import pandas as pd
import plotly.express as py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Data Analysis",
    page_icon=":mag_right:",
)

# %matplotlib inline

sns.set_style('darkgrid')

st.header("Data Anlysis")
st.subheader("This page is Use to perform the Data Analysis on the Dataset")

## Reading CSV file into a dataframe
csv_url = "https://raw.githubusercontent.com/Aman-web2000/Loan-Defaulter-/main/Training%20Data.csv"
df = pd.read_csv(csv_url, index_col=0)

categorical_col = [col for col in df.columns if df[col].dtype=='O']
numerical_col = [col for col in df.columns if df[col].dtype!='O']

st.write("Click on the below button for getting the Statistics for the data")
if st.button("Describe Data"):
    st.write("Statistics for Numerical Data")
    st.dataframe(df.describe())
    st.write("Statistics for Categorical Data")
    st.dataframe(df.describe(include='O'))

def univariate_analysis():
    colu = st.selectbox('Select column', df.columns)
    st.write(colu)
    if colu in categorical_col:
        fig=px.bar(df, x=colu, title=f"{colu} Plot") 
    else:
        fig = px.histogram(df, x=colu, title=f"{colu} Distribution")
    
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
def bivariate_analysis():
    col1,col2 =st.columns(2)
    with col1:
        colu1 = st.selectbox('Select column', df.columns)
    with col2:
        colu2 = st.selectbox('Select column', df.columns[:-1])
                
    coll1, coll2 = st.columns(2)

    with coll1:
        st.header("Choose the column type")
        cat1 = st.radio("Column data type",['Categorical', 'Numerical'])
    with coll2:
        st.header("Choose the column type")
        cat2 = st.radio("Column data type",['categorical', 'numerical'])
        
    if cat1.lower() == 'categorical':
        if cat1.lower() == cat2.lower():
            st.selectbox("Choose a Plot", ['bar'])
        else:
            st.selectbox("Choose a Plot type", [])
    else:
        if cat1.lower()==cat2.lower():
            fig = px.scatter(x=df[col1], y=df[col2])
        else:
            print()
    
            
    st.plotly_chart(fig, theme='streamlit')


def main():
    analysis_type = st.radio("Choose the Analysis type:",['Univariate (Single Variable)', 'Bi-variate (Double Variable)'])

    print(type(categorical_col))
    
    if analysis_type.lower().split(" ")[0]=='univariate':
        univariate_analysis()
    elif analysis_type.lower().split(" ")[0]=='bi-variate':
        col1,col2 =st.columns(2)
        with col1:
            colu1 = st.selectbox('Select column', df.columns)
        with col2:
            colu2 = st.selectbox('Select column', df.columns[:-1])
                        
        if (colu1 in categorical_col) & (colu2 in categorical_col):
            fig = px.bar(df, colu1, colu2, title=f"{colu1} vs {colu2} plot", labels={'x':colu1, 'y':colu2})
        elif (colu1 in categorical_col) & (colu2 in numerical_col):
            fig= px.bar(df, x=colu1, y=colu2, title=f"{colu1} vs {colu2} plot", labels={'x':colu1, 'y':colu2})
        elif (colu2 in categorical_col) & (colu1 in numerical_col):
            fig= px.bar(df, x=colu2, y=colu1, title=f"{colu1} vs {colu2} plot", labels={'x':colu2, 'y':colu1})
        else :
            fig= px.scatter(x=df[colu1], y=df[colu2], title=f"{colu2} vs {colu1} plot", labels={'x':colu1, 'y':colu2})
            
        st.plotly_chart(fig, theme='streamlit')
                    
        
        
if __name__=='__main__':
    main()
