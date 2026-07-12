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
    st.text("""Fridays at Frans\n
Brew the coffee in a bucket cause we're here to stay
People they might come and go but we'll be here all day
When the sun is shining bright we might sit down outside.
But like today when rain is pouring we come in here to hide.
When nature calls the gang is summoned like in the old days
When the year did turn around and laughter led the way
How are you today my friend and what are you up to?
Let's sit down and sip a while and I will walk you through.
As the stories they unfold people's passing by
Farmer Pierreo's here again he don't like a cloudy sky
The man, the myth, the legend got his hay chopped down today
He has his lover with him so I guess he plans to stay
And Jessica and Anna they are still out in the rain
I wounder what they talk about they don't seems to mind the pain
When the chat is over they come laughing back inside
When questions rise about what kept them
They just smile and hide
Time it moves and our dreams grow cold
All new things that we had they all break and get old
Time it moves but our dreams spin 'round
Thats when people and places like this can be found
As the time is passing by I sense a small relief
The rain has stopped and the dark clouds is lifted by the breeze
Hard decisions, serious chats they don't belong in here
On days like theese there are no time for solving our worlds fears
So Nick and Johan raise their cups and starts a funny dance
We are here to enjoy our self these Fridays at Frans
Wisdom comes and wisdom goes but many times it stays
And sometimes it still lingers on after many days
Time it moves...""", text_alignment="center")

if button2:
    st.text

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
