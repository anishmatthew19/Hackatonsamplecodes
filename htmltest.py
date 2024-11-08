import streamlit as st
import requests
import json

# Set page title
st.title("API Response Viewer")

# Input API URL
api_url = st.text_input("Enter the API URL", "https://jsonplaceholder.typicode.com/todos/1")

if st.button("Call API"):
    try:
        # Call the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            json_data = response.json()

            # Display JSON response as formatted text
            st.subheader("JSON Response")
            st.json(json_data)

            # Render JSON response as HTML
            st.subheader("JSON Response in HTML Format")
            html_content = f"<pre>{json.dumps(json_data, indent=2)}</pre>"
            st.markdown(html_content, unsafe_allow_html=True)

        else:
            st.error(f"Error: Received status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
