import streamlit as st
import requests

# Set up the API URL
api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example API URL

st.title("API Caller and JSON Response Display")

# Button to fetch data from API
if st.button("Fetch Data from API"):
    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the response was successful
        if response.status_code == 200:
            json_data = response.json()  # Parse JSON response
            st.subheader("Sample JSON Response")
            st.json(json_data)  # Display JSON data in a pretty format
        else:
            st.error("Failed to fetch data from API. Please try again.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
