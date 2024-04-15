# This page is used to demo the current state of Streamlit-analytics2
# It is deployed at https://steamlit-analytics2.streamlit.app/
# A major feature here is testing st.secret deployment and providng a window
# into the current state of streamlit-analytics2


"""This demo is run through Streamlit Sharing."""

import streamlit as st
import streamlit_analytics2 as streamlit_analytics

with streamlit_analytics.track():
    st.title("👀 Demo app for streamlit-analytics2")

    # Get the software versions
    streamlit_version = st.__version__
    streamlit_analytics_version = streamlit_analytics.__version__

    # Print the versions
    st.write(f"Streamlit version: {streamlit_version}")
    st.write(f"Python version: {streamlit_analytics_version}")

    name = st.text_input("Write your name")
    fav = st.selectbox("Select your favorite", ["cat", "dog", "flower"])
    clicked = st.button("Click me")
    if clicked:
        # Ensure fav is a string; provide a default value or modify as needed
        fav_str = (
            fav.replace("flower", "sunflower") if fav is not None else "favorite thing"
        )
        st.write(f"Hello {name}, here's a {fav_str} for you: :{fav_str}:")

    st.write("...add `?analytics=on` to the URL to see the analytics dashboard 👀")
