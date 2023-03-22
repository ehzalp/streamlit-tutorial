import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="my webpage", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding =load_lottieurl("https://lottie.host/63422d1a-ffb4-4cf5-a95a-2b569daddac4/rCMs2Wq0P9.json")
img_contact_from = Image.open("images\canva-photo-editor-8-7.png")
with st.container():
    st.subheader("hi ım humeyra :wave:")
    st.write("Iam passionate  nothing")


with st.container():
     st.write("------")
     left_column, right_column= st.columns(2)
     with left_column:
        st.header("what ı do")
        st.write("""
        bla bla bla
        
        
        bla bla bla """)
     with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    

with st.container():
    st.write("-------")
    image_column, text_column = st.columns((1,2))
    with image_column: st.image(img_contact_from)
    with text_column:
        st.subheader("Integrate lottie animations ınside streamlit app")
        st.write(
        """
      bla bla bla 

        """
        )
        st.markdown("[watch wideo....](https://www.youtube.com/watch?v=VqgUkExPvLY)")
