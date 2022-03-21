**Original Post by Chord - Tuesday December 29, 2015**

I dove head first in to the login server implementation this past week. I'm
spending a lot of time getting the libraries and base code right as I know it's
going to be heavily used. After my work, I now have working packet encryption,
decryption, and encryption setup: no small feat. I spent way more time in 2014
than I'd like to admit digging through the horrible ugly crypto + netcode. It
paid off though and I now have a clean working crypto library.

But the crypto packets are literally just the beginning. There are over 250 more
packet types that need reverse engineering.

Some technical tangents on the language and architecture:

- The programming language I chose (Scala) for the server is amazing and
  expressive. It makes C++ look like assembly language, yet is still very fast.
  This is good for me and you as I now have to spend a whole lot less time
  working on the low-level things and I can get straight in to developing
- Scala has one of the most amazing libraries known as Akka. Akka gives you
  something called the "actor model" in your code. This model allows for dead
  simple concurrency (many things happening at once), which means the server
  will be fast. A problem threaded servers have is scheduling work. Each actor
  can be scheduled individually which will let the server run hot
- With the actor model, full server crashes are going to be non-existent.
  Essentially each player session will be given one Actor as a base, so if
  something crashes, it's likely just to kill that user's session, not the
  entire server's

What this means for you guys is that this server is going to be awesome and
modern. It will be able to scale way beyond current planetside servers today.

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=58)


