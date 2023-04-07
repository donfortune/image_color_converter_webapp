import streamlit as st
from PIL import Image

st.subheader("Passport Photograph Cropper")

# Option to start camera and capture image
with st.expander('Start Camera'):
    image = st.camera_input('camera')

# Option to upload image from file
uploaded_img = st.file_uploader('Select your image')

# Display the original or cropped image
if image:
    img = Image.open(image)
    st.image(img, caption='Original Image')

if uploaded_img:
    img = Image.open(uploaded_img)
    st.image(img, caption='Original Image')

    # Option to crop the uploaded image
    if st.button('Crop Image'):
        # Get the user's cropping coordinates for a passport photo
        x, y, w, h = 0.1 * img.width, 0.15 * img.height, 0.8 * img.width, 0.7 * img.width
        left = st.number_input('Left', 0, int(img.width - w), int(x), step=1)
        top = st.number_input('Top', -int(y + h), int(img.height - h), int(y), step=1)
        right = st.number_input('Right', int(left + 1), int(img.width), int(x + w), step=1)
        bottom = st.number_input('Bottom', int(top + 1), int(img.height), int(y + h), step=1)

        # Crop the image and display the result
        cropped_img = img.crop((left, top, right, bottom))
        st.image(cropped_img, caption='Cropped Image')
