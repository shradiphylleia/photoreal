from rembg import remove
from PIL import Image
from io import BytesIO

import streamlit as st
 
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def background_img_remove(uploaded_img):
    image=Image.open(uploaded_img)
    fixed=remove(image)
    op=convert_image(fixed)
    return op


img=st.file_uploader(label='upload an image to remvoe background',type=["jpg", "jpeg", "png"],help='helps remove background from images')

if img:
    st.write('image uploaded. image is being processed.........')
    img_bg_removed_op=background_img_remove(img)
    st.image(img_bg_removed_op)
    st.download_button("Download the background removed image here",img_bg_removed_op,file_name='bg_removed_img.png',help='click on the button to see the downloaded file')