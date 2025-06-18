import streamlit as st

st.subheader("alt brain track")

st.write("1.clean foreground image: bg removed")

st.write("2. Analyzing the lighting and color tone of the person’s image. Checking if the lighting is warm or cool, and estimate the direction it’s coming from based on shadow detection.")

st.write("3. Choosing a background scene and modifying it to match the lighting conditions of the person.")
st.write("   - Adjusting brightness and contrast.")
st.write("   - Applying color filters to match temperature (warm/cool).")


st.write("4. **Blend the two together**:")
st.write("   - Using alpha blending or feathering around edges.")
st.write("   - Adding a soft drop shadow under the person based on the light direction to ground them realistically in the scene.")
