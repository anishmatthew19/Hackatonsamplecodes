import streamlit as st
import requests
from st_aggrid import AgGrid, GridOptionsBuilder

# Function to make API request
def get_api_response(user_input):
    # Replace 'YOUR_API_ENDPOINT' with the actual API URL
    api_url = "https://api.example.com/your-endpoint"
    #api_url = "https://jsonplaceholder.typicode.com/todos/1"
    headers = {"Content-Type": "application/json"}
    payload = {"input": user_input}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an error for bad status
        return response.json()  # Return JSON response if successful
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None

# Streamlit App UI
st.title("API Input and Response Display with Ag-Grid")

# Input text box for user
user_input = st.text_input("Enter your text:")

# Submit button
if st.button("Submit"):
    if user_input:
        # Fetch response from API
        api_response = get_api_response(user_input)

        if api_response:
            # Display JSON response in Ag-Grid
            st.subheader("API Response")
            grid_options = GridOptionsBuilder.from_dataframe(pd.DataFrame(api_response))
            grid_options.configure_pagination(enabled=True)
            grid_options.configure_column("Column_name", editable=True) # Example config
            grid_response = AgGrid(pd.DataFrame(api_response), gridOptions=grid_options.build())
    else:
        st.warning("Please enter some text before submitting.")
