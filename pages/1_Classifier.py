import streamlit as st 
import pandas as pd 
import numpy as np
import category_encoders as ce
import pickle
from PIL import Image

st.set_page_config(
    page_title="Classifier",
    page_icon=":robot_face:",
)


def load_model(model_name):
    
    """Load the Machine Learning Model using pickle file"""
    
    if model_name=='Logistic Regression':
        pickle_in=open("A:\DS ML\Classification\Loan defaulter\LoanDefaulter_lr.pkl",'rb')
    elif model_name=='Decision Tree':
        pickle_in=open("A:\DS ML\Classification\Loan defaulter\LoanDefaulter_dt.pkl",'rb')
    elif model_name=='Random forest':
        pickle_in=open("A:\DS ML\Classification\Loan defaulter\LoanDefaulter_rfc.pkl",'rb')
    elif model_name=='XGBoost':
        pickle_in=open("A:\DS ML\Classification\Loan defaulter\LoanDefaulter_xgb.pkl",'rb')
    else:
        pickle_in=open("A:\DS ML\Classification\Loan defaulter\LoanDefaulter_knn.pkl",'rb')
               
    clf=pickle.load(pickle_in)
    
    return clf

def predict(clf, val):
    """get the input and predict the output using clf (ML model)"""
    
    result = clf.predict(val)[0]
    return result
    
def main():
    html_title="""
        <div style="background-color: midnightblue; padding: 10px;">
        <h1 style="text-align: center; color: aliceblue;">Loan Defaulter Classifier</h1>
        </div>
        """
    st.markdown(html_title,unsafe_allow_html=True)

    st.subheader("Enter the Following details:")

    income = st.number_input(":green[Enter you annual salary e.g. 950000]", min_value=0, max_value=10000000, step=10000)

    age_col, job_exp_col = st.columns(2)
    with age_col:
        age = st.slider("Enter your Age", min_value=18, max_value=60, step=2)
    with job_exp_col:
        job_exp=st.slider("Total Job Experience",min_value=0,max_value=30,step=2)
        

    married=st.radio("Martial Status",['married',"single"])

    house_col, car_col = st.columns(2)
    with house_col:
        house=st.radio('House Owernship',['rented', 'norent_noown', 'owned'])
    with car_col:
        car=st.radio('Do you own a Car',['yes', 'no'])

    profession=st.selectbox('What is your Profession',['Designer', 'Police_officer', 'Dentist', 'Physician',
        'Civil_servant', 'Technician', 'Analyst',
        'Computer_hardware_engineer', 'Chartered_Accountant', 'Surgeon',
        'Fashion_Designer', 'Librarian', 'Secretary', 'Civil_engineer',
        'Technical_writer', 'Statistician', 'Artist', 'Official',
        'Mechanical_engineer', 'Scientist', 'Lawyer', 'Software_Developer',
        'Comedian', 'Psychologist', 'Graphic_Designer', 'Economist',
        'Magistrate', 'Politician', 'Firefighter', 'Hotel_Manager',
        'Flight_attendant', 'Petroleum_Engineer', 'Architect',
        'Air_traffic_controller', 'Computer_operator', 'Army_officer',
        'Industrial_Engineer', 'Chemical_engineer', 'Microbiologist',
        'Financial_Analyst', 'Geologist', 'Consultant', 'Aviator',
        'Engineer', 'Design_Engineer', 'Drafter', 'Biomedical_Engineer',
        'Chef', 'Surveyor', 'Web_designer', 'Technology_specialist'])
    house_yrs=st.slider("Current House Years",min_value=0,max_value=40,step=2)

    city_col, state_col = st.columns(2)
    with city_col:
        city = st.selectbox("CITY ",['Bhavnagar', 'Kavali', 'Jammu', 'Ahmedabad', 'Chapra', 'Asansol',
        'Kochi', 'Korba', 'SurendranagarDudhrej', 'Kadapa', 'Kishanganj',
        'Anantapuram', 'Ratlam', 'Bettiah', 'VasaiVirar',
        'SangliMirajKupwad', 'Kolkata', 'Tinsukia', 'Muzaffarnagar',
        'Ichalkaranji', 'Raebareli', 'Delhicity', 'Chennai', 'Gurgaon',
        'KirariSulemanNagar', 'Davanagere', 'Ulhasnagar', 'Silchar',
        'Bongaigaon', 'Nagpur', 'Belgaum', 'Allahabad', 'NewDelhi',
        'Ozhukarai', 'Morena', 'Burhanpur', 'Baranagar', 'Visakhapatnam',
        'Gulbarga', 'Thane', 'Ballia', 'Hazaribagh', 'Suryapet', 'Sasaram',
        'Amaravati', 'Madurai', 'Naihati', 'Dehri', 'Bilaspur', 'Tiruppur',
        'Ambala', 'Shimla', 'Tiruchirappalli', 'Miryalaguda', 'Firozabad',
        'Proddatur', 'Moradabad', 'SriGanganagar', 'Kanpur', 'Jaunpur',
        'BhalswaJahangirPur', 'Bidar', 'Anantapur', 'NaviMumbai', 'Arrah',
        'Saharanpur', 'Katihar', 'Nadiad', 'Amritsar', 'Ahmednagar',
        'Satna', 'Vadodara', 'Vijayawada', 'Dibrugarh', 'Durgapur',
        'Bhopal', 'Raipur', 'Unnao', 'Adoni', 'Guna', 'Siliguri',
        'MiraBhayandar', 'Surat', 'Rewa', 'Raiganj', 'Jorhat', 'Katni',
        'Ajmer', 'Ujjain', 'NangloiJat', 'Kolhapur', 'Thiruvananthapuram',
        'Bhilai', 'Dindigul', 'Deoghar', 'Secunderabad', 'Mehsana',
        'Thanjavur', 'Machilipatnam', 'Dehradun', 'Hapur', 'Jamnagar',
        'KalyanDombivli', 'Jaipur', 'Jalgaon', 'Jehanabad', 'Dhanbad',
        'Durg', 'Patiala', 'Bangalore', 'Yamunanagar', 'Kakinada',
        'Mysore', 'Haldia', 'Agartala', 'Ghaziabad', 'Narasaraopet',
        'Jodhpur', 'Bally', 'Sonipat', 'Panihati', 'Solapur', 'Purnia',
        'Bharatpur', 'Mahbubnagar', 'Bijapur', 'Vijayanagaram',
        'Pallavaram', 'Jabalpur', 'Amroha', 'SouthDumdum', 'Raichur',
        'Bareilly', 'Meerut', 'Nanded', 'Vellore', 'Rajkot', 'Nagercoil',
        'Aligarh', 'Cuttack', 'Alappuzha', 'Tezpur', 'Amravati', 'Imphal',
        'Etawah', 'Bhagalpur', 'Haridwar', 'Anand', 'Erode', 'Munger',
        'Jamshedpur', 'KarawalNagar', 'Serampore', 'Nashik', 'Aurangabad',
        'Sikar', 'Buxar', 'Bhatpara', 'Mirzapur', 'Hajipur', 'Bhilwara',
        'Saharsa', 'Bidhannagar', 'Aizawl', 'Srinagar', 'Bhind',
        'Gorakhpur', 'Udaipur', 'Rajahmundry', 'Hospet', 'Chandrapur',
        'Ambattur', 'Avadi', 'Shimoga', 'Ranchi', 'Bhusawal', 'Pali',
        'Tirupati', 'Bokaro', 'Dharmavaram', 'Agra', 'RajpurSonarpur',
        'Shahjahanpur', 'Guntur', 'Gaya', 'Madanapalle', 'Howrah',
        'Panchkula', 'Kottayam', 'Fatehpur', 'Pune', 'Salem', 'Karaikudi',
        'Mumbai', 'Maheshtala', 'Barasat', 'Berhampore', 'Kota',
        'Ludhiana', 'Giridih', 'Khandwa', 'Coimbatore', 'Mangalore',
        'Bathinda', 'Begusarai', 'Satara', 'Rohtak', 'Nandyal',
        'Tirunelveli', 'Ramagundam', 'Gangtok', 'Mango', 'SultanPurMajra',
        'Kulti', 'Orai', 'Medininagar', 'Madhyamgram', 'Dhule',
        'Hyderabad', 'Noida', 'Thrissur', 'Panipat', 'Jhansi', 'Ramgarh',
        'Singrauli', 'Siwan', 'Guwahati', 'Nizamabad', 'Mathura',
        'Danapur', 'Dewas', 'Tadipatri', 'Sambhal', 'Shivpuri', 'Gwalior',
        'Gandhidham', 'Varanasi', 'PimpriChinchwad', 'BiharSharif',
        'Tumkur', 'Bulandshahr', 'Hindupur', 'Nagaon', 'Bellary',
        'Bahraich', 'Sambalpur', 'Uluberia', 'Rampur', 'Lucknow', 'Morbi',
        'Darbhanga', 'Motihari', 'HubliDharwad', 'NorthDumdum', 'Kollam',
        'Faridabad', 'Bhubaneswar', 'Gudivada', 'Bhiwandi', 'Indore',
        'Bardhaman', 'Thoothukudi', 'Jalandhar', 'Sirsa', 'Chinsurah',
        'Kumbakonam', 'Malegaon', 'Rourkela', 'Hosur', 'Udupi', 'Phusro',
        'Ambarnath', 'Chandigarhcity', 'Panvel', 'Sagar', 'Guntakal',
        'Bhiwani', 'Srikakulam', 'Jalna', 'Tiruvottiyur', 'Junagadh',
        'Kharagpur', 'Khammam', 'Parbhani', 'Muzaffarpur', 'Warangal',
        'Malda', 'Karimnagar', 'Jamalpur', 'Kozhikode', 'Phagwara',
        'Kamarhati', 'Mau', 'Chittoor', 'Akola', 'Loni', 'Patna',
        'Farrukhabad', 'Tadepalligudem', 'Karnal', 'Latur', 'Gopalpur',
        'Tenali', 'Ongole', 'KhoraGhaziabad', 'Eluru', 'Gandhinagar',
        'Alwar', 'Nellore', 'Pudukkottai', 'Berhampur', 'Bikaner',
        'Kurnool', 'Bhimavaram', 'RaurkelaIndustrialTownship',
        'Pondicherry'])
    with state_col:
        state = st.selectbox("STATE", ['Gujarat', 'AndhraPradesh', 'JammuandKashmir', 'Bihar',
        'WestBengal', 'Kerala', 'Chhattisgarh', 'MadhyaPradesh',
        'Maharashtra', 'Assam', 'UttarPradesh', 'Delhi', 'TamilNadu',
        'Haryana', 'Karnataka', 'Puducherry', 'Jharkhand', 'Telangana',
        'HimachalPradesh', 'Rajasthan', 'Punjab', 'Uttarakhand', 'Tripura',
        'Odisha', 'Manipur', 'Mizoram', 'Sikkim', 'Chandigarh'])

    input_val = pd.DataFrame(data=[[income, age, job_exp, married, house, car, profession, city, state, house_yrs]],columns=['Income','Age', 'total_experience', 'Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession', "CITY",'STATE','CURRENT_HOUSE_YRS'])

    model = st.selectbox("Select ML Model", ['Logistic Regression', 'Decision Tree', 'Random forest', 'K Nearest Neighbors', 'XGBoost'])

    if st.button('Predict'):
        clf = load_model(model)
        val=predict(clf, input_val)
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

if __name__ == '__main__':
    main()
    