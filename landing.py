import streamlit as st
from bg_remove import background_img_remove

st.header('photoreal')
st.subheader('an attempt at photo-realistic image composition into a scene')

st.divider()

img=st.file_uploader(label='upload an image to remvoe background',type=["jpg", "jpeg", "png"],help='helps remove background from images')

if img:
    st.write('image uploaded. image is being processed.........')
    img_bg_removed_op=background_img_remove(img)
    st.image(img_bg_removed_op)
    st.download_button("Download the background removed image here",img_bg_removed_op,file_name='bg_removed_img.png',help='click on the button to see the downloaded file')
