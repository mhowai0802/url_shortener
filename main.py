# app.py
import streamlit as st
import requests

def shorten_url(long_url):
    try:
        response = requests.post(
            "https://0avp15ms25.execute-api.us-east-1.amazonaws.com/dev/users",
            json={"original_url": long_url}
        )
        data = response.json()
        print(response)
        if response.status_code == 200:
            return data["short_url"]
    except Exception as e:
        st.error(f"Error: {str(e)}")
    return None

st.title("URL Shortener")

# Input field for the long URL
long_url = st.text_input("Enter your long URL")

# Button to trigger URL shortening
if st.button("Shorten URL"):
    if long_url:
        with st.spinner("Shortening URL..."):
            short_url = shorten_url(long_url)
            if short_url:
                st.success("URL shortened successfully!")
                st.write(f"Short URL: {short_url}")
                if st.button("Copy to clipboard"):
                    st.write(short_url)
    else:
        st.warning("Please enter a URL")