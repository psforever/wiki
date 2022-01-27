## LLU Goes Live - August 14, 2003

We are releasing a patch to the client and server on August 14, 2003
that contains the following items:

- [Facility](Facility.md) capture takes on a whole new level
  of action now that the Lattice Logic Unit is live! Details on the
  LLU are in the online manual.

<!-- -->

- The [Lasher](Lasher.md) now has [Damage
  Degradation](Damage_Degradation.md). While the projectile
  still goes the same maximum distance, it now degrades in its
  strength, as does the lash itself. Lasher damage against armor
  ([MAXes](MAX.md), vehicles) has been reduced by 30%.

<!-- -->

- The [Starfire](Starfire.md) AA MAX has had its damage
  degradation removed and its damage has been decreased about 20%.
  This reduction is only different from the live version at ranges of
  less than 50 meters. The removal of damage degradation, however,
  will be very noticable against targets at greater ranges.

<!-- -->

- The [Basilisk](Basilisk.md) and the
  [Wraith](Wraith.md) have been combined into the new 3 point
  [ATV cert](</ATV_(Certification)>). Players who already have
  Wraith or Basilisk certs will keep the ATV cert for now, but will be
  "in debt" to the certification system by one point. If those players
  choose to forget the ATV cert, they will have to have 3 available
  points to buy it again.

<!-- -->

- Dynamically calculated [Certification
  Point](Certification_Point.md) system: This is to resolve
  certain bugs where a player would forget a
  [Certification](Certification.md), but those certification
  points would not be available to them.

<!-- -->

- An exploit that would force a base to deplete its [NTU
  Silo](NTU_Silo.md) by destroying the [Matrix
  Panels](Matrix_Panel.md) has been fixed.

<!-- -->

- The Find [Waypoint](Waypoint.md) button will no longer be
  available when selecting a drop location from the
  [HART](HART.md) shuttle.

<!-- -->

- Squadmates in vehicles now have their names displayed in gold.

## July 31, 2003 - Client-side Patch

We will be releasing a client-side patch Thursday, July 31 at 3 AM
Pacific. The patch contains the following item:

- Enemies will no longer appear as moving and invulnerable corpses to
  the client.
- [Marauder](Marauder.md) and [Enforcer](Enforcer.md)
  physics and handling have been fixed.
- A zone crash associated with backpacks has been fixed.
- Newly created vehicles should no longer deconstruct on the creation
  pad.
- Dropped [ACEs](ACE.md) deconstruct properly.
- [Lightning](Lightning.md) drivers will no longer lose their
  reticule while on steep slopes.
- Improved Availability of Login Servers. In other words, if the
  Launchpad says a server is up, players will be able to connect to it
  reliably.
- Fixed a zone crash from using Warp Gates while in a vehicle with
  multiple occupants.
- The planetside_crash.log file now pulls more information to aid in
  debugging crash issues.
- An issue with new characters getting stuck in the world has been
  resolved.
- A client-side memory leak when zoning was fixed.

## July 20, 2003

We will be releasing a client-side patch July 20, 2003 at 3 AM Pacific.
The patch will contain the following:

### Bug fixes:

- Spawn tube doors are fixed, this also fixes numerous issues where
  hacked doors would not open.
- Players who have more than 100 health due to empire balance
  adjustments will have full health bars.
- Players with 1 health point will no longer appear dead on your
  client.
- Your UI settings will now persist between logins.
- You will no longer have a strange chat message appear when you are
  revived.
- Liberator and Skyguard certifications appear on myPlanetside.
- You can no longer get stuck in offline training mission 1 if you
  clear your inventory.
- /who teams results are now formatted correctly.
- /ignore player results are now formatted correctly.

### Additions:

- Medic/Engineer/Hacker icons will appear over friendly heads if they
  are holding the associated tool, i.e. Medical Applicator, BANK,
  Nano-dispenser, REK.
- Advanced medics are able see dead people who have not yet released
  their corpses on the proximity radar when they have a Medical
  Applicator equipped. Likewise, dead players who have not yet release
  their corpse can see the position of Advanced Medics who are holding
  the Medical Applicator.

### Changes:

- Faster clean up of objects based on object density. In other words,
  if there are many objects appearing, such as backpacks and destroyed
  vehicles, they will decay faster. This is intended to help client
  and server performance in large battles.
- Grief Points work on a sliding scale, where grief accumulates faster
  as a player accumulates more points in a brief period of time. The
  threshold for grief accumulation to begin moving up this sliding
  scale has been increased. This should reduce the grief generated in
  extended vehicle collisions.
- Change to nano-dispenser fire effect.
- Performance monitor can be toggled pressing Shift and the period
  key. This will allow you to view your framerate and ping times and
  packet loss.
- The Lasher's refire rate was increased, lashes more often and in a
  slightly larger space.
- The Thresher's flux cannon damage has been increased 50% against
  players and its range has been increased 50%.
- The maximum Cone of Fire on the Mini-Chaingun has been reduced. The
  Cone of Fire expansion now starts later in the burst and expands
  more slowly.
- The Skyguard's flak cannon range has been doubled.
- Marauder health increased by 1/3.
- Thresher health increased by 1/3.
- Empire logos on HART dropships are fixed and look better.
- The Lightning now sports 360-degree turrets.
- The Hotspot threshold has been decreased. Six people involved in a
  battle will generate a Hotspot. Hotspots will also last longer.
- Updated physics engine to Karma 1.3.

## Client-Side Patch - July 11, 2003

A client-side patch is being released today that should resolve many of
the crash issues related to sound that players were experiencing.

## Test Server Patch - July 10, 2003

A patch to the Test Server is currently available that should resolve
crash issues related to sound cards. Please post your feedback on the
Test Patch to the Test Server Feedback Forum.

## July 9, 2003 - Small client patch

A small patch went in today that improves framerate in certain problem
situations. We will also continue in improving framerate optimizations.
There are no other changes associated with this patch.

## July 4, 2003 - Server-side patch

The servers were brought down this morning for a brief server-side patch
that should resolve the issues experienced after the July 3 patch. We
apologize for the inconvenience these issues may have caused you.

## Liberator (7-3-03)

Client and Server-side patch (July 3, 2003 2:45PM Pacific on All
Servers)

- The 3-Person bomber known as the [Liberator](Liberator.md)
  is now available. The cost is 3 Certification points.

<!-- -->

- Certain issues with doors have been fixed.

## July 2, 2003

Introducing the PlanetSide Test Server

Today, we are introducing the much anticipated Test Server for
PlanetSide. Stop in and preview the new features, content and fixes
before they hit the live server. The [Liberator](Liberator.md)
will be making its debut on the Test Server today as well.

Here's how to get to the PlanetSide Test Server preview:

Patch Planetside normally. Copy (do not move) the entire Planetside
directory to a new location on your computer. In the PS directory, find
"PlanetSideTest.exe" Make a shortcut to the test patcher on your
desktop. Run the patcher and, if desired, hit "play" to enter the
Planetside test environment. You'll go to a server selection where three
servers will be listed. Select the "Public Test" server. At this point
you'll be able to enter "Public Test" normally.

## Client and Server-side fix (6/21/03 3:30AM Pacific on All Servers)

This is a client and server-side fix that will take approximately 1.5
hours to update all the servers.

- Fixed a crash related to the [Orbital
  Strike](Orbital_Strike.md).

<!-- -->

- The ability to purchase a [Liberator](Liberator.md)
  certification has been removed until the Liberator is available
  in-game (very soon). Note that you can still sell back the Liberator
  certification (regular cert sell-back rules apply).

<!-- -->

- Certain voice assets were swapped incorrectly between male and
  female, but are now fixed.

<!-- -->

- Hotspots should be working as intended.

<!-- -->

- Various fixes to the Skyguard are made in this patch, including its
  display on the radar and on the statistics page, as well as various
  animation and sound related fixes.

## Server-side fix (6/7/03, 3am)

- A fix was made that prevents characters from being "stuck in the
  world" and unable to log onto a specific server. This patch doesn't
  affect very many players, but they were unable to play while this
  bug existed. It's resolved now.

<!-- -->

- An extremely rare server performance issue occurred today on Markov.
  That is now resolved.

## Server-side fix (6/6/03)

The zone crash that affected Cyssor on Emerald last night has been
resolved. All servers were updated with that fix.

## Server-side fix (6/5/03, 6pm Central)

A server-side fix was made to fix the lag issues seen today. That is
resolved now and all servers are updated with that fix.

## Server-side fix (6/5/03)

A stability fix was made to the servers this morning. All updates have
occurred and the servers are back up and running.

## Small downloadable patch (5/31/03)

The reports of a lockup bug continued to accumulate, so we came in today
to make a fix. The fix is client-side only and does not require a server
cycling. Just patch and enter the game.

## Server-side Fixes (5/30/03)

- The "first-time experience" exploits are prevented. In addition to
  the fixes made yesterday (that sealed up 90+% of those exploits) we
  have also resolved an issue affecting some users where the
  first-time event wouldn't be permanently registered. That's resolved
  now and first-time experience is (properly) one-time only.

<!-- -->

- A large memory leak was located and squashed on the servers. This
  stabilizes our worlds further.

<!-- -->

- A logic error in base capture experience has been found. The system
  is now changed so that a) squads that participate in captures will
  typically gain more xp than in the previous system, and b) the
  exploitability of the system by "cap squatters" (individuals from
  squads slipping in at the last minute to rake xp without risk and
  sharing that bonus with other squadmembers who were also not at
  risk) are virtually eliminated.

<!-- -->

- Additionally, the xp awards for resecuring a base (hacking the
  console back after attackers have initially hacked it) have been
  increased substantially, so defenders that stick around and fight to
  retake a base should see increased xp awards for doing so.

NOTE: These xp changes apply equally to lone wolves as well as squads.
Both will see increases.

## Holiday Game Updates (12/21/2006)

Update Features

More Holiday Fun:

Watch out for the new objects appearing all over Auraxis during the
holiday. In certain locations you might run across a snowman,
gingerbread man, sled, or xmas tree. Exploring the world to find these
objects might just earn you a few [Merits](Merits.md):

- Holiday: Snowman - Earned by finding all 9 snowmen.
- Holiday: Gingerbread Man - Earned by finding all 10 gingerbread men.
- Holiday: Spirit of Youth - Earned by finding 7 sleds and 7 xmas
  trees (there are 9 of each).
- Players that participate in the event and earn the awards may get a
  special prize at the end of the event!

**Miscellaneous Changes:**

- [Engineering](</Engineering_(Merit)>) merits should all list
  requirements
- News Ticker has been updated with news about new merits and the xmas
  event
- [Equipment Support](Equipment_Support.md) merits should all
  list requirements
- Players that use /humbug to hide the santa hat should now be able to
  keep their usual hat flair (i.e. beret, etc)

## Game Update (01/17/2007)

Update Features

- Xmas hats, presents, lights in trees, etc. have been turned OFF
- /appeal should no longer crash the game when logged in with Quick
  Launch.

## Game Update (03/30/2007)

Undocumented update

- Cake, pies, and donut boxes replacing NC, TR, and VS backpacks
  respectively for April Fool's event

## Game Update (05/03/2007)

Undocumented bug fix

- Fixed [Darklight](Darklight.md) icon not displaying above
  both friendly and enemies names. The bug was introduced with patch
  [3.12.12](3.md.12.12).

## Anniversary 2007 Update (5/18/2007)

Happy Four Year Anniversary, PlanetSide!

For PlanetSide's Four Year Anniversary, we designed three New Pistols
(one for each empire), a Missile Launcher with Propelled Explosives, and
an experimental Flamethrower weapon. Each weapon can be obtained by
every player with the exception of the Flamethrower.

As you read the details below, you'll notice that there are a few
limiting factors on the Missile Launcher and the Flamethrower. However,
take note that we have enabled all weapons to be available to all
players from 5/18/07 to 5/25/07 regardless of the limitations. We wanted
everyone to have the chance to try out the new weapons and participate
in the mayhem of the Four Year Anniversary! Enjoy!

PISTOLS - The [Spear](Spear.md) ([NC](NC.md)) / The
[Stinger](Stinger.md) ([TR](TR.md)) / The
[Eraser](Eraser.md) ([VS](VS.md))

These Empire specific pistols are designed to be very lethal towards
Infantry units but lack a punch in the armor piercing department

- 10mm Pistols
- Very powerful versus infantry units
- Primary firing mode is an automatic single shot, capable of firing
  long distances with better than average accuracy
- Primary firing mode has a slower rate of fire
- Secondary firing mode will unload all remaining rounds in the clip
  to produce a high amount of damage
- Secondary firing mode has a side effect: your
  [stamina](stamina.md) will be completely drained, so use it
  with caution
- Secondary firing also has a large cone of fire so be close to your
  enemy units if you want to do massive damage
- Pistols deliver very low damage towards
  [vehicles](vehicle.md) and equipment

MISSILE LAUNCHER with PROPELLED EXPLOSIVE - The
[Scorpion](Scorpion.md)

The [Scorpion](Scorpion.md) uses a range-finder technology to
fire 'smart' missiles from long distances

- Built in Range Finder to lock in distances where your enemies are
  "dug-in"
- Launches 'smart' missiles to the locked in distance while carrying
  grenade type bombs, unleashing several smaller explosives in every
  direction
- Ability to zoom long distances to establish locked in range (unable
  to shoot at close targets)
- Hitting objects before the missile reaches the locked in range will
  disable the missile's arming ability
- Available without any certification cost to 2 year veterans (based
  on your character's creation date)
- If not a 2 year veteran, it may be purchased for 1 certification
  point if [Special Assault](Special_Assault.md) has already
  been learned

FLAMETHROWER - The [Dragon](Dragon.md)

The [Dragon](Dragon.md) is a powerful flamethrower that works
best at close ranges. The Dragon is an experimental weapon and may not
be accessible at all times in PlanetSide. Due to the special effects of
the flames, the Dragon may be removed from many playing conditions that
cause adverse performance issues. Although many limitations have been
put in place to limit performance issues, the Dragon will be classified
experimental until such performance issues are deemed non-existent or
believed to be minor.

- The Primary fire mode unleashes a stream of fire for short range
  tactics. The fire is slow moving that is very devastating to anyone
  caught in the way
- This stream can be released in short bursts or until your fuel is
  gone
- Secondary fire mode launches a concentrated ball of fire called a
  Sunburst that will explode after a short time or when it hits the
  ground.
- The Sunburst's explosion deals massive damage to anyone in range.
- If Sunburst is close enough to the ground, it will also scatter
  small fires around that burn anyone who tries to walk through it.
- Secondary fire mode requires fuel capacity to be at its maximum
- Fire from Primary and Secondary fire modes will not only directly
  hurt soldiers passing through armor, but it will ignites them as
  well
- The Dragon is only useable by 3 year veterans (based on your
  character's creation date) and includes a three minute purchase
  timer

## [6th Anniversary Update](6th_Anniversary_Update.md) (6/18/2009)

- Free [certification](certification.md) reset
- Increased maximum [Battle Rank](Battle_Rank.md) from 25 to
  40
- Added 6 year [Term of Service](Term_of_Service.md)
  [merit](merit.md)

## BR32 Fix (6/17/2009)

- Patch fixes issues with [Battle Rank](Battle_Rank.md) 32+
  players causing others to crash and other weird anomalies.

## Server Merge and Lasher nerf (08/25/2009)

- Players moving from [Werner](Werner.md) to
  [Gemini](Gemini.md) will receive a [Werner Distinguished
  Veteran](Distinguished_Veteran.md) [Merit](Merit.md)
- Players who receive a -W or -G appended to their names will be
  allowed a one-time use of the /rename command
- [Outfits](Outfit.md) that receive a -W or -G appended to
  their names will be allowed a one-time use of the /outfitrename
  command (leader only)
- We have increased the minimum number of characters allowed from 8 to
  24
- The [Lasher](Lasher.md)'s LASH damage has been significantly
  reduced
- The Lasher's [AP](Armor_Piercing.md) Damage has been reduced
  (while in AP mode) **(Not actually implemented in-game for unknown
  reasons)**

## Game Update (10/15/2009)

- Fixed a bug where players with the five year [Term of
  Service](Term_of_Service.md) award were unable to purchase
  [Reinforced Exo-Suit](Reinforced_Exo-Suit.md) armor in the
  [Sanctuary](Sanctuary.md) and [Amerish](Amerish.md)
  without the [certification](certification.md)
- Dramatically increased [BEP](BEP.md) and
  [CEP](CEP.md) awarded for [facility](facility.md)
  captures (later rolled back in a patch shortly afterward)

## Game Update (10/22/2009)

It's that time of year again when all the Ghouls and Goblins come out to
play however this year they've decided to change things up a bit, gone
are the flying skulls and red glowing skies which have been replaced
with the Spooktacular Bonus Experience Days. This years event will run
from October 22nd through November 2nd, and feature some really howling
experience gains. [Base](Facility.md) captures like you've never
seen before, cavern captures that will make you want you want get that
next [BFR](BFR.md) [imprint](imprint.md), and much more!
So go ahead and spend some time with us and let’s get that much needed
[Battle Experience](Battle_Experience_Points.md) and see if we
can reach [Battle Rank](Battle_Rank.md) 40... If you dare!!!

[The Chainblade Massacre](The_Chainblade_Massacre.md) will also
pop up from time to time throughout the [Spooktacular
Days](Spooktacular_Days.md) so be prepared! All players will be
able to use [Cloaking infiltration suits](Infiltration_Suit.md)
without need of the [certification](certification.md) on
[Extinction](Extinction.md) (this is our version of ghosts).

- In true Halloween tradition, players will only be allowed to use a
  Knife to kill other players.
- Players are urged to get proper [Implants](Implant.md)
  before entering the zone such as [Darklight](Darklight.md)
  in order to see all apparitions.
- The zone has limited [vehicles](vehicle.md).
- Knives’ secondary mode will now damage vehicles and equipment. This
  damage should slightly increase with [Melee
  Booster](Melee_Booster.md) implants.
- Oh, and don’t worry about damage from vehicles trying to mow you
  over. That has been changed. Nor should you worry about damage from
  an exploding vehicle. Consider yourself in a zombie state under
  these circumstances.
- If a base is drained of its resources, hang tight as they will be
  replenished almost immediately.

Now lets get prepared for some serious experience gain and have a
haunting good time!

## Game Update (11/03/2009)

Greetings Auraxians!

The [Spooktacular Days](Spooktacular_Days.md) are now over and
all systems have been restored back to normal.

Thank you and we'll see you on the Battle Field!

## Game Update (12/09/2009)

Greetings Auraxians! We are pleased to announce to everyone that
PlanetSide now supports both Windows Vista and Windows 7. While players
could work around the compatibility issues with Vista and Windows 7
before, the client should now be completely functional without having to
use compatibility mode and/or other tricks.

We appreciate your patience with this change and please make sure that
you spread the word to all your fallen Vista and Windows 7 comrades!

[category:Patches](category:Patches.md)
