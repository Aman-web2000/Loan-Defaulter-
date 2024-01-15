import streamlit as st


def main():
    st.set_page_config(
    page_title="Home",
    page_icon=":page_facing_up:",
)

    st.sidebar.success("Select the Tab")

    st.title("🚀 Loan Defaulter Classifier App 🚀")
    st.markdown("Welcome to the Loan Defaulter Classifier App! This app is designed to help you analyze loan-related data "
                "and predict whether a person is likely to be a loan defaulter or not.")
    
    st.header("About Me")
    st.write("Hi, I'm Aman Chauhan, the creator of this app. With a passion for machine learning, "
             "I developed this tool to streamline the loan application process and assist in identifying potential defaulters. "
             "Feel free to explore the various features and functionalities offered by this app!")

    st.header("Why was this app created?")
    st.write("The Loan Defaulter Classifier App was created to address the challenges faced in the lending industry. "
             "By leveraging machine learning, this app aims to provide quick and accurate predictions on whether a loan applicant "
             "is likely to default, enabling financial institutions to make more informed lending decisions.")

    st.header("How to Use the App?")
    st.subheader("1. Home Page")
    st.write("Explore the home page to learn more about the app and its creator. You'll find information about the purpose "
             "of the app and its key features.")
    
    st.subheader("2. Classifier Page")
    st.write("Navigate to the Classifier page to input relevant details for a loan applicant. The app will analyze the data "
             "and provide a prediction on whether the individual is likely to be a loan defaulter or not.")
    
    st.subheader("3. Data Analysis Page")
    st.write("Visit the Data Analysis page to visualize and explore the patterns in the loan-related dataset. The app provides "
             "interactive charts to help you gain insights into the data.")

    st.success("Feel free to use the app and make informed decisions in the lending process!")

# Uncomment the line below to run the home_page function when the script is executed
# home_page()

if __name__=='__main__':
    main()