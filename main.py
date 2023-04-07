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
if uploaded_img:
    img = Image.open(uploaded_img)
    st.image(img, caption='Original Image')
    if st.button('Crop Image'):
        # Get the user's cropping coordinates for a passport photo
        x, y, w, h = 0.1 * img.width, 0.15 * img.height, 0.8 * img.width, 0.7 * img.width
        left = st.number_input('Left', 0, img.width - w, int(x), step=1)
        top = st.number_input('Top', 0, img.height - h, int(y), step=1)
        right = st.number_input('Right', left + 1, img.width, int(x + w), step=1)
        #bottom = st.number_input('Bottom', top + 1, img.height, int(y + h), step=1, max_value=int(img.height))
        bottom = st.number_input('Bottom', top + 1, img.height, int(y + h), step=1, max_value=img.height)

        # Crop the image and display the result
        cropped_img = img.crop((left, top, right, bottom))
        st.image(cropped_img, caption='Cropped Image')
if image:
    img = Image.open(image)
    st.image(img, caption='Original Image')


