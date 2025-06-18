import streamlit as st

st.subheader('Final image')
st.divider()

st.write('Foreground')
st.image('./images/foregorund.png')
st.divider()

st.write('Background')
st.image('./images/bg.png')
st.divider()

st.write('Background removal: rembg')
st.image('./images/bg_removed_img.png')
st.divider()

st.write('Detection of shadow mask')
st.image('./images/mask.png')
st.divider()

st.write('Light direction')
st.image('./images/lightd.png')
st.divider()

st.write('final: bg+fg')
st.image('./images/final.jpg')
