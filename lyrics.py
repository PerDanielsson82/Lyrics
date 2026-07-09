
import streamlit as st

st.image("Logo.png", output_format="JPEG")    
st.title("Album Lyrics", text_alignment="center")

st.sidebar.title("Albums")
st.sidebar.subheader("Skydiving", text_alignment="center")
st.sidebar.image("Skydiving.png", width=100, output_format="JPEG")
st.sidebar.write("  ")
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
st.sidebar.image("Summertime.png", width=100, output_format="JPEG")
st.sidebar.write("  ")
button5=st.sidebar.button("*Laughter in the night*")
button6=st.sidebar.button("*At the stationhouse*")

if button5:
    st.text("""Laughter in the night\n
The sun is going down as the day begins to fade.
Time means nothing now as I sit here in the shade.
Yesterday was something else, another day and time
As the year it turned around.

People were walking by with a mind in a good state
They were dressed to kill on their way to celebrate
I heard music playing everywhere and all around
As the year it turned around

Laughter in the night. As I watched the fading light. Laughter in the night.

Nick and Johan did raise their glasses for a song
So Anna sang for them a song in a foreign toungue
And Jessica told tales ´bout royalties and hotel drinks
On the day the year it turned around

And I watched as I was sitting on the ground
When Sam and Leo they did turn the stage around. 
And then the main act sang a song ’bout biking up a hill
On the day the year did turn around. 

Laughter in the night. As I watched the fading light. Laughter in the night.""", text_alignment="center")

if button6:
    st.text(""" At the stationhouse\n
Summertime is here, And the air’s so clear 
And people’s walking by, And smile against the clear blue sky
At the stationHouse, The conversation rise
As the coffee start to flow, And the wind still slowly blows

I didn’t hear a word, The laughter was all I heard
And I realised right there, The plays to be it must be here
By the tables there, Where guys and girls all share
A little space in time, To fit into this little rhyme

Then the time is up, we split and go our separate ways
But tomorrow, we are here again
To make the laughter fill our day

Then the wheel it turns, and the sunlight burns
And the time pass by, We look against the same old sky
At the stationHouse, the conversation rise
The same old girls and boys, And I are still making all that noice""", text_alignment="center")
    
st.write(" ")
