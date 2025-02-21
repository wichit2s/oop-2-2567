import streamlit as st

st.title("Interactive Widgets")
clicked = st.button('Register with Our Site')
first_name = st.text_input(" first name? ")
last_name = st.text_input(" last name? ")
dob = st.date_input('DoB')
st.color_picker('Pick a color')
st.feedback('faces')
checked = st.checkbox('Single')
file = st.file_uploader('File')
note = st.text_area(" bio? ")
if first_name:
    st.write(f'hello {first_name}')
    st.image('https://picsum.photos/400/300')
# what is bottom?