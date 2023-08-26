import streamlit as st
from PIL import Image

# Streamlit camera input
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    print(camera_image)

    if camera_image:
        # Creaate PIL image instance
        img = Image.open(camera_image)

        # Convert to grayscale
        gray_img = img.convert('L')
        # Render the grayscale image to the webpage
        st.image(gray_img)