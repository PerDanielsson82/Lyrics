# cd lyrics
# source venv/bin/activate
#  cd Documents/Streamlit/
#  streamlit run lyrics.py

import streamlit as st

st.image("pictures/Logo.png", output_format="JPEG")    
st.title("Album Lyrics", text_alignment="center")

st.sidebar.title("Albums")
st.sidebar.subheader("Skydiving", text_alignment="center")
st.sidebar.image("pictures/Skydiving.png", width=100, output_format="JPEG")
st.sidebar.write("  ")
button1 = st.sidebar.button("*Fridays at Frans*")
button2 = st.sidebar.button("*Devils Dance*")
button3 = st.sidebar.button("*Skydiving*")
button4 = st.sidebar.button("*In times of sadness*")

if button1:
    st.pdf("Fridays at Frans.pdf")

if button2:
    st.pdf("lyrics/Devils dance.pdf")

if button3:
    st.pdf("lyrics/Skydiving.pdf")

if button4:
    st.pdf("lyrics/In times of sadness.pdf")


st.sidebar.subheader("Summertime", text_alignment="center")
st.sidebar.image("pictures/Summertime.png", width=100, output_format="JPEG")
button5=st.sidebar.button("*Laughter in the night*")
button6=st.sidebar.button("*At the stationhouse*")

if button5:
    st.pdf("lyrics/Laughter in the night.pdf")
    
if button6:
    st.pdf("lyrics/At the stationhouse.pdf")



st.write("  ")
