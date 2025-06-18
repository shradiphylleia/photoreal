import streamlit as st

st.divider()
st.header('Determining Light Direction')
st.write('Post determination of the shadow and obtaining the shadow mask from the previous tab, now we wish to determine the direction of the incoming light source')
st.write('While chromacity can help detect the mask it cannot help us detect the source and reconstruct it in the a 3d space.')

st.divider()
st.subheader('Instance shadow detection')
st.write('The above can be overcome by using instance shadow detection which refers to the discovery of shadow instances in the images along with the corresponding object which are casting the said shadow.')
st.write('Rather than using physical illumination and color models for shadow detection as in our previous approach we use CNN to learn features which can help us detect shadows and instance shadow detection not only helps detect the shadow(mask) it helps detect the associated object too.')
st.write('This would make the overall editing better as we will be aware of the light direction which can then be maintained rather than simple cut and paste')


st.subheader("Working of the LISA Architecture")

st.markdown("1. Image for analysis")

st.markdown("2. Feature Extraction (ConvNet)")
st.write(
    "- A CNN processes the image to extract useful features like edges and shapes.\n"
    "- These features go into two branches:\n"
    "  - One for detecting individual objects and shadows.\n"
    "  - Another for matching shadows to objects and predicting light direction."
)

st.markdown("3. Instance RPN (Region Proposal Network)")
st.write("Proposes regions that might contain objects or shadows.")

st.markdown("4. Association RPN")
st.write("Proposes regions that connect shadows to the objects that cast them.")

st.markdown("5. RoIAlign and Prediction Heads")
st.write(
    "**Instance Branch:**\n"
    "- Box Head: Predicts boxes around objects.\n"
    "- Mask Head: Predicts outlines of objects/shadows.\n\n"
    "**Association Branch:**\n"
    "- Box Head: Predicts boxes around object-shadow pairs.\n"
    "- Light Direction Head: Predicts the direction the light is coming from."
)

st.markdown("6. Predictions")
st.write(
    "- Bounding boxes for objects and shadows.\n"
    "- Masks for detailed outlines.\n"
    "- Object-shadow associations.\n"
    "- Estimated light direction."
)

st.markdown("7. Training with Labels")
st.write(
    "- During training, the system compares predictions with labeled data (boxes, masks, associations, light direction).\n"
    "- It learns by minimizing errors (losses) over time."
)
