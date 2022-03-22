Original Post by Chord - Friday March 4th, 2016

Big milestone with the login server. I've worked hard to decode the packets
required to get the PlanetSide client to the login screen. I can finally do
this:

Image

There was a lot of technical junk in the way that needed to be done before this
could happen. Here are some of the things that needed to be completed before
this could be done:

PlanetSide's cryptographic packets needed to be reverse engineered and the
cryptographic setup needed to be figured out. This took me nearly a year of on
and off work before PSForever A basic login server code base needed to be
created Packets related to logging in needed to be reverse engineered and
rewritten in the login server. This was painstaking as PlanetSide's packet
format is so compact it's hard to understand Plenty of other reverse engineering
to get a real understanding of what the PlanetSide code base was doing (thanks
IDA pro)

Currently as it stands, the login server is around 2300 lines of dense Scala
code. I'm feeling quite proud of the progress so far! I'm learning a lot along
the way and I haven't even gotten to the game server.

With this, here are some of the things that are my list of things to do

**Login Server**

- Fix the crypto library issue that is preventing development on Windows
  (pscrypto.dll)
- Add more functionality to the login server so that it will be able to manage
  the connection to clients (currently clients auto disconnect after some time
  due to their not being any keep alives)
- Design an effective logging scheme that will scale to a bigger server (doing
  this later will be hard)
- Create a way to store user accounts in a database and pick a DB solution
  (MySQL, PostgreSQL, CouchDB, MongoDB, etc.)

**GameLogger, GCAPy**

- Write more tools to process the GCAP files in order to figure out the packets
  necessary for logging in completely
- Find a list of packets required for connecting the planetside game server

**GameLauncher**

- Make this prettier and have a way to select between live PlanetSide servers
  and PSForever servers

**Game Server**

- Start removing common components from the LoginServer to a shared code
  repository
- Figure out how to get to the character creation screen (what packets are
  required)
- Make a high level diagram of what I believe will be involved in the game
  server

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=156)
