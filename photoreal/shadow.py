import streamlit as st
import numpy as np
import cv2
from PIL import Image

def detect_shadows_chromacity(img, light_threshold=0.7, hue_thresh=10):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v_norm = cv2.normalize(v.astype('float32'), None, 0, 1.0, cv2.NORM_MINMAX)
    
    bright_mask = v_norm > light_threshold
    bright_pixels_hue = h[bright_mask]
    bright_pixels_v = v_norm[bright_mask]

    avg_hue = np.mean(bright_pixels_hue)
    avg_v = np.mean(bright_pixels_v)

    hue_diff = cv2.absdiff(h.astype('float32'), avg_hue)
    shadow_mask = (v_norm < avg_v) & (hue_diff < hue_thresh)

    return shadow_mask.astype('uint8') * 255



st.header('Task 2: Shadow detection(bg)& classification')
st.write('The approach is derived by taking into consideration the following research studies and blogs:')
st.write('1. Techniques and Algorithms of Shadow Detection in Images(idea of chromacity)')
st.write('2. Wang, Tianyu, et al. “Instance shadow detection.” Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.')


img=st.file_uploader(label='upload an image to for shadow mask detection',type=["jpg", "jpeg", "png"],help='add the foreground image to help detect shadows')

if img:
    detect_btn=st.button(label='Detect Shadow (Chromacity Method)')
    if detect_btn:
        input_image = Image.open(img).convert("RGB")
        np_img = np.array(input_image).astype('uint8')
        bgr_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)

        shadow_mask = detect_shadows_chromacity(bgr_img)
        shadow_rgb = cv2.cvtColor(shadow_mask, cv2.COLOR_GRAY2RGB)
        st.image(shadow_rgb, caption="Detected Shadow Mask", use_column_width=True)

