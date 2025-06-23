import streamlit as st
import requests
import json

st.title("My First AI App")

# Text input for the user's prompt
prompt = st.text_input("Ask the AI anything:")

# Button to send the request
if st.button("Send"):
    if prompt:
        # Make API call to local Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )
        
        # Display the response
        if response.status_code == 200:
            result = response.json()
            st.write("**AI Response:**")
            st.write(result["response"])
        else:
            st.error("Error connecting to AI")
    else:
        st.warning("Please enter a prompt")