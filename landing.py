import streamlit as st
from bg_remove import background_img_remove

st.header('photoreal')
st.subheader('an attempt at photo-realistic image composition into a scene')

pages={
    "BG&FG":[st.Page("bg_remove.py",title="background remover"), 
             st.Page("shadow.py",title="shadow detection"),
             st.Page("light_direction.py", title='light direction'),
             st.Page("color_blending.py",title='color blending'),
             st.Page('output.py',title='final o/p'),
             st.Page('tech.py',title='tech stack')]
}

pg=st.navigation(pages)
pg.run()
