**Original Post by Chord - Friday February 19th, 2016**

Hello again PSF. Busy times on my end, but I got to spend some time hacking
around with the PlanetSide client tonight.

**Friday Night Hacking**

Core combat isn't enabled on the server side, but the PlanetSide client doesn't
care! I messed around with map loading state changes and I was able to fake load
some cave maps, while being networked on a real continent. To other people it
would look quite strange as I would be flying around ignoring any collision
detection. Somethings I learned about the game from tonight:

- All physics and collision detection is clientside. If this were to be removed,
  then walls, doors, or the floor wouldn't stop you
- Water damage is server-side
- Nearly all of the interesting GM commands are patched out of the client. Like
  the code has literally been compiled out. This is quite sad as I suspect the
  server probably has more than a fair share of strange bugs regarding these
  commands.
- There are multiple embedded command processors within planetside that allows
  for high level actions to to take place. For example, the command for loading
  a map is 'psc_loadmap'. This goes for the creation of all game objects as
  well. Logging the calls to these command processors should help figure out how
  the game is running
- The /paintball command is locked behind a special bit on the client, but once
  enabled it allows the creation of floating text anywhere in the world. It's
  simply a debug tool and nothing else.
- The cave maps are located in the PlanetSide/expansion1 folder and are prefixed
  as ugd. Example: ugd01
- When loading in to a cave map while actually running on a bigger continent,
  the cave map is always towards the bottom left corner of the overworld map.
  This is where PlanetSide's (0, 0) coordinate lies.
- There is a /spectator command in the client, but unfortunately it is patched
  out

Here are some screenshots: Image Image Image Image Image Image Image

**Website News** My site is now fully backed up with a disaster recovery plan in
place. I can now sleep easy. PSF will never die, NCGauss. Sorry for all of the
horrible spam that has cropped up recently. There is a dedicated and passionate
group of people who want this project to burn. We should expect more things like
this in the future. Active couter-measures are in place and I keep quite a close
eye on server health.

**Login Server Coding** Not much has gotten done in this area unfortunately.
This is quite important, but the momentum has been lost. Spring break is coming
up for me soon and I hope to get some serious coding in then. At least what I
have done so far is open source. I need all of the help I can get in this area.
Code doesn't write itself.

**Packet Captures** We are nearly at 10 million total packets captured! Holy
crap, great work team!

**PlanetSide Forever Discord** If you didn't know, PSF has its own Discord
server, courtesy of Naeadil. This has probably limited the number of posts on
the forums, but it's certainly a lot easier to chat than to write up a lengthy
post. Glad this is helping keep the community together. If you are not in it
already, ask me or Naeadil for an invite.

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=142)
