import streamlit as st

st.subheader('Coloring & Blending')

st.divider()

st.markdown("1. Color Space Conversion")
st.write("Converting both the person image and background to the same color space.")

st.markdown("2.Histogram Matching")
st.write("Matching  the color distribution of the person image to the background using histogram matching for each channel.")

st.markdown("3. Ambient Light Adjustment")
st.write("Estimating the light temperature and intensity from the background (Task 3).")

st.markdown("4. Shadow Simulation")
st.write("""
Adding realistic shadows under/behind the person based on:
- light direction (from Task 3)
- The shadow mask (from Task 2)
Using:
- Gaussian blur for soft shadows
- Shape masks for hard shadows """)

st.markdown("5. Edge Softening")
st.write("""
Using alpha blending/edge feathering to remove sharp edges around the person, blending them more naturally into the scene.
""")

