
import streamlit as st

    
st.title("Album lyrics", text_alignment="center")
st.markdown("Välj låt i menyn till vänster för att visa texten", text_alignment="center")

st.sidebar.title("Albums")
st.sidebar.subheader("Skydiving", text_alignment="center")

button1 = st.sidebar.button("*Fridays at Frans*")
button2 = st.sidebar.button("*Devils Dance*")
button3 = st.sidebar.button("*Skydiving*")
button4 = st.sidebar.button("*In times of sadness*")

if button1:
    st.text("""Fridays at Frans \n
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

Time it moves..""", text_alignment="center")

if button2:
    st.text("""Devils Dance \n
The legend tells about a summer day,
when the wind was warm and the sky was blue.
A melody was heard above the whispering wind,
but where it came from noone knew.
As day did fade and turn into the evening,
and eventually into night.
An unknown player came and played the melody,
(that)the wind had wispered so light.

The player played with fury and entusiasm,
and people couldn’t stop to dance.
It felt as if it got a hold of them,
so he smiled with fire in his eyes.
He started walking out into the pinetrees,
and the dancers followed on.
The fire it got wider in his eyes,
as the melody went on.

Dance, dance, dance said the music
And the people they danced
They said the Lord from above was plying
But oh how wrong they where...

The dance went on deeper in the forest,
and swirled around the lakes and trees.
The music carried on and so the dancers,
deeper into the night.
In a glade upon a nearby mountaintop,
the player sat down by a tree.
The melody still flew out from the flute,
as the devil smiled and played on.

Dance, dance...

Then when night did finally turn into the day,
and the sun began to rise.
The churchbells chimed in the valley down below,
but noone answered the call.
Up in the glade there was calm and stillness,
noone left to tell the tale.
But if you listen as the wind is floating by,
you still hear the melody he played.""", text_alignment="center")
    
if button3:
    st.text("""Skydiving \n
As we get old we stop to challenge us at all
As the time moves on we do what we always done
So one day we thought as we looked up in the sky
Lets just do it with no regrets at all

They said it would be god to go away this day
After all the rain the sun would shine today
So this day we,re going up into the air
And let the wind that blows just carry us away

Skydiving
Going down the mountain sides
Skydiving
Look at the world from a different view

We gathered on the top and the instructions they were clear
There’s nothing to worry ’bout just run and you will see
So we did just that we ran into the air
And when we left the ground it all felt so Unreal.

Skydiving...

Winds they blow and things they drift away
And with the winds the moments tend topass us by
But floating in the air we could’t do another thing
Just enjoy the moment that happened there and then

So back on the ground the moment it was gone
But we did still remember the time spent flying high
And now we know that sometimes youmust look
At the world and things from a different view

Skydiving...""", text_alignment="center")
    

if button4:
    st.text(""" In times of sadness\n
Now and then I wounder where it all began?
What did ignite the spark that turned it upside down?
Was it just a rumour or something that was true?
Was it something that we could have prevent?
Somewhere on the ocean a boat is sailing on
to a destination that is still unknown
And like that boat we’re sailing on the sea of life.
Hope your boat did reach the shore.

I did once believe that day would follow night
Not that night could go on and take over the light
But like in nature when the moon eclipse the sun
Our mind and thoughts are easily corupted by the night
The boat we’re sailing on can take a different path
And go through rain and thunder and get lost in the night
And in the worst of nightmares the boat will fall apart
And we sink into the sea.

Now and then I wounder where it all began?
And did you ever wounder ”oh what have I done?”
We must live and learn but sometimes it’s so hard
But lift your head and try to breath even in the dark.
But in times of sadness it’s easy to belive
That this is all there is and there wount be nothing else
But try to remember that the moon will go away
And the light will come again""", text_alignment="center")
    
st.sidebar.subheader("Summertime", text_alignment="center")

st.write("  ")
st.write("Hör gärna av er med komentarer")
