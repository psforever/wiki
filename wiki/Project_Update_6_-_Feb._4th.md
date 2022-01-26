**Original Post by Chord - Friday February 05, 2016**

Hey PSForever.

Apologies for the recent nasty spam attack. I'll be tightening
registration and flooding limits to counter act future events. Big
thanks to Sulferix and p0intman for keeping things from falling to shit.

As for my absence, well I've been working on the server - client
communication and I'm able to get an unmodified client to talk to my
server and have the client get past the login progress. Yeah not as much
as I was hoping for either. I've been quite slammed this spring with
work and I just haven't been able to devote as many cycles as I would
like. I do need to make a point to keep you guys up to date regardless
though. Otherwise I figure most of you will probably scurry off to
another corner of the internet out of boredom.

I'm currently doing server development on my Linux machine which is
great, but obviously not ideal because PlanetSide is windows only. I've
been able to get away with this for a while as PlanetSide has great Wine
support. The best apart about having chosen Scala is that I don't have
to change any code over from Linux to Windows due to it being JVM based.
One thing I do have to change which is slowing me down right now is my
crypto library is in C++, which is platform specific. It's working for
Linux only and I would need to port it over. Not a huge deal, but just
something that is bothering me at the moment.

In order to speed up development, I have decided to open source what I
have so far on the Login Server. It is available here:
<https://github.com/psforever/PSF-LoginServer>

Until next time!

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=135)

[Category:PSForever Updates](Category:PSForever_Updates.md "wikilink")
