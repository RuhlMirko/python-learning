import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    snapshot = st.camera_input("Camera")

if snapshot:
    img = Image.open(snapshot)
    gray_img = img.convert('L')
    st.image(gray_img)


uploaded_img = st.file_uploader("Upload Image")

if uploaded_img:
    img = Image.open(uploaded_img)
    gray_img = img.convert('L')
    st.image(gray_img)


