import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Aries P. Wibowo')

st.info('App Developer and Tech Enthusiast who love coffee. It does not always take sophisticated technology to make life better.')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@createwitharies ', 'Create With Aries YouTube channel', icon_size)
st_button('instagram', 'https://instagram.com/riespratama', 'My Personal Instagram', icon_size)
st_button('medium', 'https://riespratama.com', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/riespratama/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/aries-wibowo/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', '#', 'Sign up for my Newsletter', icon_size)
st_button('cup', '#', 'Buy me a Coffee', icon_size)
