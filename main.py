import streamlit as st
import requests
import pandas as pd

def make_api_request(cname):
    headers = {'Content-Type': 'application/json'}
    url = 'http://34.30.160.67:5005/demoapi/'+cname
    response = requests.get(url, headers=headers)
    return response.json()

def testt():
    st.title("IntelleWings Shell Company Check")

    # Sidebar
    st.sidebar.header("Input")

    cname = st.sidebar.text_input("Enter Company Name or CIN")


    if st.sidebar.button("Check"):
        # Make the API request and display the response
        # st.subheader("API Response")
        try:
            response_data = make_api_request(cname)
    
            lst = []
            for resp in response_data['results']:
                lst.append(resp)
            st.table(pd.DataFrame(lst))
        except Exception as e:
            st.error(f"Error making API request: {str(e)}")

if __name__ == "__main__":
    testt()
