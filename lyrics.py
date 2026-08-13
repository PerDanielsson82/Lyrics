
import streamlit as st
from streamlit_player import st_player

st.image("pictures/Logo.png", output_format="JPEG")    
st.title("Album Lyrics", text_alignment="center")

st.sidebar.title("Albums")
st.sidebar.subheader("Skydiving (2026) ", text_alignment="center")
st.sidebar.image("pictures/Skydiving.png", width=100, output_format="JPEG")
st.sidebar.write("  ")
button1 = st.sidebar.button("*Fridays at Frans*")
button2 = st.sidebar.button("*Devils Dance*")
button3 = st.sidebar.button("*Skydiving*")
button4 = st.sidebar.button("*In times of sadness*")

if button1:
    st_player("https://music.youtube.com/watch?v=fv2TtaVT9q8&si=wPA8m0A0GCKYgVa2")
    st.pdf("lyrics/Fridays at Frans.pdf")
    with open("lyrics/Fridays at Frans.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Fridays at Frans.pdf",
                                 on_click="ignore", mime="application/pdf")


if button2:
    st_player("https://music.youtube.com/watch?v=vEiAtr7pqCA&si=q8_HQzu2DiWSOvSs")
    st.pdf("lyrics/Devils dance.pdf")
    with open("lyrics/Devils dance.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Devils dance.pdf",
                                 on_click="ignore", mime="application/pdf")

if button3:
    st_player("https://music.youtube.com/watch?v=t0TSAopt-lY&si=6tWT2jEMqmHtrpmO")
    st.pdf("lyrics/Skydiving.pdf")
    with open("lyrics/Skydiving.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Skydiving.pdf",
                                 on_click="ignore", mime="application/pdf")

if button4:
    st_player("https://music.youtube.com/watch?v=jDiZIBp-XG0&si=W5Dbove8c8wqasw3")
    st.pdf("lyrics/In times of sadness.pdf")
    with open("lyrics/In times of sadness.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="In times of sadness.pdf",
                                 on_click="ignore", mime="application/pdf")


st.sidebar.subheader("Summertime (2024) ", text_alignment="center")
st.sidebar.image("pictures/Summertime.png", width=100, output_format="JPEG")
button5=st.sidebar.button("*Laughter in the night*")
button6=st.sidebar.button("*At the stationhouse*")

if button5:
    st_player("https://music.youtube.com/watch?v=Kfv_muHA5LU&si=b8uihi33k8oWD8nc")
    st.pdf("lyrics/Laughter in the night.pdf")
    with open("lyrics/Laughter in the night.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Laughter in the night.pdf",
                                 on_click="ignore", mime="application/pdf")
    

if button6:
    st_player("https://music.youtube.com/watch?v=xgM0CPPAgxY&si=-jAGPFrxRrCwJv8g")
    st.pdf("lyrics/At the stationhouse.pdf")
    with open("lyrics/At the stationhouse.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="At the stationhouse.pdf",
                                 on_click="ignore", mime="application/pdf")

st.sidebar.subheader("Christmas (2024) ", text_alignment="center")
st.sidebar.image("pictures/Christmas.png", width=100, output_format="JPEG")
button7=st.sidebar.button("*This very day*")
button8=st.sidebar.button("*Once upon a time*")

if button7:
    st_player("https://music.youtube.com/watch?v=Y_nr1V0p4o4&si=AATMnJnrr9HNzWD5")
    st.pdf("lyrics/This very day.pdf")
    with open("lyrics/This very day.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="This very day.pdf",
                                 on_click="ignore", mime="application/pdf")

if button8:
    st_player("https://music.youtube.com/watch?v=PtEWx_cX7Ws&si=gFbHndtD5V_Vgw8W")
    st.pdf("lyrics/Once upon a time.pdf")
    with open("lyrics/Once upon a time.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Once upon a time.pdf",
                                 on_click="ignore", mime="application/pdf")

st.sidebar.subheader("Different World (2024) ", text_alignment="center")
st.sidebar.image("pictures/Different world.png", width=100, output_format="JPEG")
button9=st.sidebar.button("*Sail away*")
button10=st.sidebar.button("*K.C*")
button11=st.sidebar.button("*Different world*")
button12=st.sidebar.button("*My world*")

if button9:
    st_player("https://music.youtube.com/watch?v=HIVns2XP0xc&si=PRA-m_uRqSjFNGsK")
    st.pdf("lyrics/Sail away.pdf")
    with open("lyrics/Sail away.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Sail away.pdf",
                                 on_click="ignore", mime="application/pdf")

if button10:
    st_player("https://music.youtube.com/watch?v=RDfzQ5Zgc4I&si=-2N2SkDj42ww8ZBc")
    st.pdf("lyrics/KC.pdf")
    with open("lyrics/KC.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="KC.pdf",
                                 on_click="ignore", mime="application/pdf")

if button11:
    st_player("https://music.youtube.com/watch?v=Yvdtx27Ku4M&si=df6UqsvImuONvvjm")
    st.pdf("lyrics/Different world.pdf")
    with open("lyrics/Different world.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="Different world.pdf",
                                 on_click="ignore", mime="application/pdf")

if button12:
    st_player("https://music.youtube.com/watch?v=BRUyzRN5kbo&si=jz5xODIw21_oeWvl")
    st.pdf("lyrics/My World.pdf")
    with open("lyrics/My World.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="My World.pdf",
                                 on_click="ignore", mime="application/pdf")

st.sidebar.subheader("Two sides (2020) ", text_alignment="center")
st.sidebar.image("pictures/Two sides.png", width=100, output_format="JPEG")
button13=st.sidebar.button("*The world's gone mad*")
button14=st.sidebar.button("*The way home*")
button15=st.sidebar.button("*I ain't going nowhere*")


if button13:
    st_player("https://music.youtube.com/watch?v=t9P0Wuyg9r4&si=gsunUmNG8rxxr0oT")
    st.pdf("lyrics/The world's gone mad.pdf")
    with open("lyrics/The world's gone mad.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="The world's gone mad.pdf",
                                 on_click="ignore", mime="application/pdf")

if button14:
    st_player("https://music.youtube.com/watch?v=F1q-PLGjnYA&si=685mtfgHprSErJjB")
    st.pdf("lyrics/The way home.pdf")
    with open("lyrics/The way home.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="The way home.pdf",
                                 on_click="ignore", mime="application/pdf")

if button15:
    st_player("https://music.youtube.com/watch?v=OQoyJRdxZTA&si=tJ9a5g-ghpksTEdT")
    st.pdf("lyrics/I ain't going nowhere.pdf")
    with open("lyrics/I ain't going nowhere.pdf", "rb") as file:
        btn = st.download_button(label="Download pdf", data=file,
                                 file_name="I ain't going nowhere.pdf",
                                 on_click="ignore", mime="application/pdf")


st.write("  ")
