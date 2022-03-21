**Original Post by Chord - Thursday November 19th, 2015**

So much for weekly updates...sorry about that! I'm still all for the project.

**PlanetSide Event** I hope everyone had a good time at the probably last PS
event ever. The turn out was low, but certainly the highest I've seen in a
while. I got some good play time and captures as well. The hackers were not
completely destroying the game, except for Saturday when someone pulled people.
Could have been worse.

**Login Server Progress** I have more than enough packets for the login server
to make the server on my own. The game server is where all of the packets will
come in handy. I have decided to go with Scala+Akka for the main codebase and
C++11 or Python when necessary. Originally I was thinking of doing the server in
C++ like every other game server out there, but C++ has real problems with
concurrency (exactly what game servers need to run fast) and any single crash
brings the whole server down. Scala with Akka is based on the Java Virtual
Machine, but is more than fast enough to do the job. Also I'm one guy. C++ is
hard to get stuff done in quick. If this project is going to succeed, I need to
not start from scratch.

My goal is to have a minimal working login server by the end of the year. I
really want the most minimal working server, even it it means there won't be
multiplayer to start (i.e. you login but you are alone). That way you guys have
something to play with instead of just waiting around for me.

**Capture Files** By the end of next week I will have a quick and dirty capture
file upload form for you guys to start submitting captures.

**Wiki** I'm not focusing on making the wiki better for now as getting a server
is more important.

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=26)

<!--[Category:PSForever Updates](Category:PSForever_Updates.md)-->
