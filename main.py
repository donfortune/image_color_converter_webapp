import streamlit as st
from PIL import Image

st.subheader("Image Color Converter")

with st.expander('Start Camera'):   #camera only starts when expanded
    image = st.camera_input('camera')  #starts the camera

if image:   #condition for camera permision
    img = Image.open(image)  #open the image with the pillow module
    grey_image = img.convert('L')  #convert the image to grey scale
    st.image(grey_image) #display the image on web page


uploaded_img = st.file_uploader('Select your image')
if st.button('Convert') and uploaded_img:
    if uploaded_img:
        pics = Image.open(uploaded_img)
        new_image = pics.convert('L')
        st.image(new_image)

