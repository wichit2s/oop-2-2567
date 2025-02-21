# st.session_state
from random import choice

import streamlit as st
if 'counter' not in st.session_state:
    st.session_state.counter = 1
    st.session_state.clicked = False
    st.session_state.name = ''
clearb = st.button('Clear counter')
addb = st.button('Increase counter')
subtractb = st.button('Decrease counter')
if clearb: st.session_state.counter = 1
if addb: st.session_state.counter += 1
if subtractb: st.session_state.counter -= 1

clicked = st.button("click meee?")
if clicked:
    st.session_state.clicked = True
    name = st.text_input('Your name? ', key="name")
if st.session_state.name:
    st.text(f"Hello {st.session_state.name} How are you today?")


st.title("Session State")
st.header(f'counter = {st.session_state.counter}')
n = st.session_state.counter
data = {
    'Name': [choice(['Anna', 'Betsy', 'Cathy']) for i in range(n)],
    'GPA': [choice([3.9, 4.0, 3.3]) for i in range(n) ],
    'Country': [choice(['Russia', 'Ukraine', 'USA']) for i in range(n)],
}
st.table(data)
