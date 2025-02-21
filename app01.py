from random import choice

import streamlit as st

# print('Hello Streamlit')
st.title('Hello Streamlit')
st.header('latex')
st.latex('f(x) = e^{log{y}x^9}')
st.header('Code')
st.code('''import streamlit as st
print("hello streamlit")
st.header("for your Header")
''')
st.image('https://picsum.photos/800/600')
st.header('Header 2')
st.text('My fav photo')

st.header('Markdown')
st.markdown('''
# Equation

$f(x) = e^{log{y}x^9}$

    import streamlit as st
    print("hello streamlit")
    
# Image

![image](https://picsum.photos/id/111/800/600)
''')

n = 1000
data = {
    'Name': [choice(['Anna', 'Betsy', 'Cathy']) for i in range(n)],
    'GPA': [choice([3.9, 4.0, 3.3]) for i in range(n) ],
    'Country': [choice(['Russia', 'Ukraine', 'USA']) for i in range(n)],
}
st.table(data)
