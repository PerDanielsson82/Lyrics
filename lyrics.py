# cd lyrics
# source venv/bin/activate
#  cd Documents/Streamlit/
#  streamlit run lyrics.py

import streamlit as st
from streamlit_player import st_player

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
    st_player("https://music.youtube.com/watch?v=fv2TtaVT9q8&si=wPA8m0A0GCKYgVa2")
    st.pdf("lyrics/Fridays at Frans.pdf")


if button2:
    st_player("https://music.youtube.com/watch?v=vEiAtr7pqCA&si=q8_HQzu2DiWSOvSs")
    st.pdf("lyrics/Devils dance.pdf")

if button3:
    st_player("https://music.youtube.com/watch?v=t0TSAopt-lY&si=6tWT2jEMqmHtrpmO")
    st.pdf("lyrics/Skydiving.pdf")

if button4:
    st_player("https://music.youtube.com/watch?v=jDiZIBp-XG0&si=W5Dbove8c8wqasw3")
    st.pdf("lyrics/In times of sadness.pdf")


st.sidebar.subheader("Summertime", text_alignment="center")
st.sidebar.image("pictures/Summertime.png", width=100, output_format="JPEG")
button5=st.sidebar.button("*Laughter in the night*")
button6=st.sidebar.button("*At the stationhouse*")

if button5:
    st_player("https://music.youtube.com/watch?v=Kfv_muHA5LU&si=b8uihi33k8oWD8nc")
    st.pdf("lyrics/Laughter in the night.pdf")
    

if button6:
    st_player("https://music.youtube.com/watch?v=xgM0CPPAgxY&si=-jAGPFrxRrCwJv8g")
    st.pdf("lyrics/At the stationhouse.pdf")

st.sidebar.subheader("Christmas", text_alignment="center")
st.sidebar.image("pictures/Christmas.png", width=100, output_format="JPEG")
button7=st.sidebar.button("*This very day*")
button8=st.sidebar.button("*Once upon a time*")

if button7:
    st_player("https://music.youtube.com/watch?v=Y_nr1V0p4o4&si=AATMnJnrr9HNzWD5")
    st.pdf("lyrics/This very day.pdf")

if button8:
    st_player("https://music.youtube.com/watch?v=PtEWx_cX7Ws&si=gFbHndtD5V_Vgw8W")
    st.pdf("lyrics/Once upon a time.pdf")
    with open("lyrics/At the stationhouse.pdf", "rb") as file:
        btn = st.download_button(label"Download pdf", data=file,
                                 file_name="At the stationhouse.pdf",
                                 on_click="ignore", mime="application/pdf")
st.write("  ")
