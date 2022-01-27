Sometimes called the Overhead Map, this is a top-down view of a
[continent](Continent.md) and its
[facilities](Facilities.md). Accessed by pressing the "M" key
(default).

To zoom the map, use the Mouse Wheel, and to move it, left-click-hold,
and drag. Press 'G' to move to the [Interstellar
Map](Interstellar_Map.md).

## Basic Map View

The basic view (by default: "M") shows the continent as a whole. The
features of the basic view are as follows:

![](images/ContMapExp.jpg "ContMapExp.jpg")

### Facility Information

- **Base Name** --Every [Facility](Facilities.md) in the game
  has a unique name, typically based on mythological figures from
  history.
- **Base Type** --On either side of the facility name will be a clock
  icon (indicating [Hack-and-Hold](Hack-and-Hold.md) base
  type) or flag icons (indicating an [LLU](Lattice_Logic_Unit.md) base type).
- **Hack Status** --If the facility is under hack, crossed flags of
  the [empire](Empire.md) initiating the hack will appear to
  the left of the facility name.
- **[Facility Linked Benefit](Facility_Linked_Benefit.md)**
  --Above the base name will be various icons indicating the linked
  benefits the facility is receiving (<i> see [Facility Linked
  Benefit](Facility_Linked_Benefit.md) for more
  information</i>).
- **Module Status** --If the base is receiving a [Module
  benefit](Module_benefit.md) a yellow module icon will appear
  next to the name. It will be green if the module benefit is a
  [Cavern Lock](Cavern_Lock.md).
- **Generator Status** --If the facility's
  [Generator](Generator.md) is destroyed a lightning bolt with
  a cross through it will appear as an icon next to the name.
- **Spawn Tube Status** --If all of the facility's [Spawn
  Tubes](Respawn_Tube.md) are destroyed, a crossed-out spawn
  tube icon will appear next to the name.
- **Boosted Pain Field Status** --If the generator or [Spawn
  Room](Spawn_Room.md) has had its [Pain
  Field](Pain_Field.md) boosted, special icons will be
  displayed next to the name.
- **Base NTU Levels** --The current reserves of base
  [NTU](NTU.md) are displayed as a percentage below the base
  name. Generally, a Base will only consume large amounts of NTU if
  its equipment has been destroyed, so this can be an indication that
  enemy troops are operating in the structure.

### Tower Information

- **Tower Names** --[Tower](Towers.md) names are unique to each
  [Planet](Planet.md), and generally reflect the tower type,
  and the nearest other features of note; e.g 'SE Lahar Watch Tower'
- **Tower Spawn Tube Status** --If both of the tower's spawn tubes are
  destroyed, a special icon will appear under the tower name. The icon
  will only appear if you are zoomed in close enough.

### Latice Information

- **Lattice Links** --Each base is connected to its neighbours by the
  [Lattice](Lattice.md), and this is represented on the map by
  connecting lines in various colors, indicating oppotunities to hack.
  See [Lattice](Lattice.md) for more information on the
  colors.
- **Capitol Links and Force Dome Status** --Connections between
  [Capitols](Capitol.md) and their
  [Sub-Capitols](Sub-Capitol.md) are shown by green Lattice
  Links, and the status of the Capitol [Force
  Dome](Force_Dome.md) can be seen by a pale outline around
  the structure of the Capitol on the map.

### SOI Locations

- **[Base SOI](Sphere_of_Influence.md)** --The Sphere of Influence of a base
  is indicated by a large circle on the map in the color of the owning
  empire. The area covered by this circle has many special rules
  associated with it, and many deployables have SOI restrictions.
- **[Tower](Towers.md) SOIs** --Towers also have an
  [SOI](Sphere_of_Influence.md), although it is a lot smaller. Where a Tower
  and Base SOI overlap, your [empire](Empire.md)'s SOI takes
  priority.

### Warpgate Information

- **Warpgate Location** --[Warpgates](Warpgate.md) are shown
  on the map as green-yellow circles. Lattice links pass through these
  warpgates, to connect to the first base on the destination Planet.
  The destination of the warpgate is also shown if it is not a
  [Broadcast warpgate](Broadcast_warpgate.md).
- **Sanctuary Warpgates** --Sanctuary Warpgates leading to a
  [Sanctuary](Sanctuary.md) are colored accordingly and cannot
  be entered by enemy troops.
- **[Geowarp](Geowarp.md)** --Geowarp gates are shown
  similarly, but smaller, and lead into the indicated
  [Cavern](Caverns.md). Geowarps rotate in activity, thus an
  inactive geoward will be denoted on the map as well.

## Detailed Facility Information

By Double-clicking on a base on the map,a new window will pop up with
more details about that base ([Cavern](Caverns.md) facilities do
not have this feature).

- **Base Type** --Five base types exist, each having a different
  layout, and providing different features and benefits; [Amp
  Station](Amp_Station.md), [Tech
  Plant](Tech_Plant.md), [Bio
  Laboratory](Bio_Laboratory.md), [Interlink
  Facility](Interlink.md), and [Dropship
  Center](Dropship_Center.md).
- **Base Capture Type** --Bases can be captured in one of two ways;
  Standard (or 'Hack n Wait'), shown by a pair of clock symbols, or
  [LLU](Lattice_Logic_Unit.md), show by a pair of flag symbols.
- **NTU Level** --The ammount of [NTU](NTU.md) remaining
- **Base Hack Status** --If the base is hacked, the hack status will
  be desplayed here. If it is a hack and hold base, the time remaining
  until capture will be displayed.
- **Respawn Tube Status** --Normal or Destroyed
- **Generator Status** --Normal, Critical, or Destroyed
- **Network Status** --If the base is infected with a
  [Virus](Virus.md), "Infected" is displayed here. If a
  friendly player installed the virus, the virus type will be shown
  instead.
- **Base Module Status and Timers** --The Base Information Window
  lists all the currently available [Modules](Modules.md),
  along with their function, how long remains before they run out, and
  whether they are installed locally, or at a connected lattice base.
- **Base Benefit** --Each type of base provides a different
  [Lattice](Lattice.md) benefit. At the bottom of the window,
  it shows you what benefits the facility is receiving. Benefits in
  yellow are a result of [Continental
  lock](Continental_lock.md) benefits.

## Other Information

- **LLU location** --An [LLU](Lattice_Logic_Unit.md) that has been spawned as
  part of a capture attempt will be displayed cleary on the map for
  all to see. Its location updates dynamically, as the LLU is moved
  across the continent, making interception possible. The lactice link
  that the LLU must move upon will flash.
- **Module Location** --As with the LLU, any
  [Modules](Module.md) in transit are shown on the map in a
  similar manner.
- **Player Location** --The player is shown by a white arrow,
  indicating both position and facing.
- **Squad and Platoon locations** --Members of a player's current
  squad are shown as yellow numbers, corresponding to the numbers in
  the [Squad](Squad.md) bar at the top of the screen.
- **[Hotspots](Hotspot.md)** --Conflict between enemies and
  friendly troops or deployables is show by yellow flashing stars.
  This is dynamic, but not continuously updated, the interval being
  somewhere in the order of 5-10 seconds.
- **[Waypoints](Waypoint.md)** --A soldier's [Personal
  Waypoint](Personal_Waypoint.md) is shown as a white
  triangular icon. Squad Waypoints are shown as number yellow
  triangles, with purple and orange, if in a Platoon. The [Laze
  Pointer](Laze_Pointer.md) waypoint is shown as a yellow
  circle with black arrow.
- **Command Battleplans** --At [Command Rank](Command_Rank.md)
  3, Squad Leaders can edit text and draw lines directly on to the
  Continental Map for the whole Squad to see, in order to elaborate on
  objectives and tactics. This can look like anything, and is largely
  dependent on the artistic skill of the Squad Leader. If you see
  strange things on the map, it is most likely this!
- **Show Friendlies/Enemies** --Various Command Ranks gain special
  abilites to reveal troops. These are shown on this map.
- **Map Grid** --The map is overlaid with a basic [Map
  grid](Map_grid.md) reference system, allowing features to be
  called out quickly with chat text. The letters along the top and
  numbers down the side make up a co-ordinate; C10, G6, and so on.
- **Deployable Information** --Friendly [ACE](Adaptive_Construction_Engine.md) and
  [FDU](FDU.md) deployables will show on the map if zoomed in
  close enough. Each has their own special icon.

## Special Modes

As well as basic navigation, the Continental Map is used in three
special situations.

- **[Respawn](Respawn.md)** --Upon death, the map allows a
  soldier to select where to respawn. There are a potential six
  choices, all shown by spinning cyan circular icons; Nearest AMS,
  Nearest Tower, Nearest Base, Matrixed Base, Matrixed AMS, Sanctuary.
  If a spawn point is on another continent, a small inset map will be
  show to allow selection.
- **[HART](HART.md)** --The Continental Map is used to allow a
  soldier dropping from low orbit to pick his desintation. This
  destination may not be in ANY [SOI](Sphere_of_Influence.md) or on a Enemy
  Locked Continent, and uses a sort of snap grid system, making
  prescise dropping tricky.
- **[Broadcast](Broadcast.md)** Warp --The Continental Map is
  used to allow the driver of a vehicle, (or infantryman) to select a
  broadcast Warp destination. Available choices are shown by spining
  cyan circles on the warp gates.

[Category:Game Guides](Category:Game_Guides.md)
