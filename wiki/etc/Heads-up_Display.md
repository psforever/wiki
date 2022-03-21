### Squad Bar

(Note: Most elements of the user interface may be repositioned by dragging the
frames about, so the locations listed below may not always be the case.)

Located at the top middle, this strip shows the names, numbers, conditions and
grid references of the members of your current [squad](../terminology/Squad.md).
Red sections indicate a squad member's current Health, blue shows Armor. Each
squad member is given an arbitrarty number, which is used to show them on the
[Continental Map](Continental_Map.md). Thier current Map
[Grid](../terminology/Grid.md) reference is shown under their name.

In a [Platoon](../terminology/Platoon.md), this information extends to cover up
to two other squads, show in different colored borders; yellow, orange, and
purple.

### [Proximity Map](../terminology/Proximity_Map.md)

Located at the top left, the [Proximity Map](../terminology/Proximity_Map.md)
shows detailed information of the immediate surrounding terran or rooms. It also
shows friendly troop positions and movments as green dots, and in some
circumstances, enemy troops and vehicles as red.

The Proximity map can be set to show 200m, 100m and 50m. It may be toggled
between static, with North as up, or rotating, with the current field of view as
up, in the Video Options.

### Reticle

Located in the centre, this cross-hair shows you where your gun will fire. This
is dynamic and adjusts position in the case of off-set weaponry; i.e.
[Lightning](../vehicles/Lightning.md) weapon systems and BFR arms.

The reticule changes color depending on what it is over:

- Grey - No target
- Yellow - A target that is beyond the maximum range of the current weapon
  system
- Green - A friendly target
- Red - An enemy target in range of the current weapon

Locking weapons show a combination of red and green to indicate lock progress,
and are usually accompanied by an audio cue.

When over a target the reticle also displays the name and distance of the
target.

The reticle also shows the current status of the [Cone of fire](../terminology/Cone_of_fire.md)
system, and how accurate the shot will be. The further apart the reticule's
extremeties are, the less accurate. Stop moving and crouch to draw these edges
in and increase the accuracy. The shot has a random chance of landing anywhere
within a circle described by these outer points.

The reticle also displayed if a shot has hit the target, by flashing a
transparent gold disk each time a shot lands on target. This includes static
objects and friendlies.

### Status & [Chat](../commands/In-Game_Chat.md) Pane

This window is divided into two sections.

The Status section, on top, shows all relevant kills as they happen, in the
form:

{Killer Name} {Icon of the Weapon} {Victim}

and is shown in the color of the empire of the killer.

A soldier will see all kills near him, to a range of about 300m, along with any
kills made against, or by, his current squad. Squad kill messages can be from a
different planet. \[Square Brackets\] denote that that player was using a
vehicle at the time.

Used with the [Continental Map](Continental_Map.md), this 'kill spam' can be a
powerful tool to work our enemy positions and makeup, as it cannot be masked.

Also shown in this section in white text are [experience](../terminology/Experience_Points.md) awards,
as they happen, and world messages, such as the capture of facilities, and the
movement of [LLUs](../terminology/Lattice_Logic_Unit.md), implant activations
and any other system messages.

The lower half shows the chat section. Typed text and voice macros show here.
Default colors are:

- White: Local Text - Range 20-30m
- Yellow: [Squad](../terminology/Squad.md) Channel
- Orange: [Platoon](../terminology/Platoon.md) Channel
- Bright Green: [Outfit](../terminology/Outfit.md) Channel
- Indigo/Blue: [SOI](../locations/Sphere_of_Influence.md) Broadcast
- Blue: Private Messages
- Teal/Green: Command Broadcasts

These colors are all user definable from the options menu.

(See also: [In-Game Commands](../commands/In-Game_Commands.md))

Both section are scrollable and retain several hundred lines.

The top bar of this window has buttons to allow [LFS](../terminology/LFS.md)
toggle, and to select the default chat channel, and which channels are listened
to.

### Vehicle HUD Elements

If aboard a vehicle, the status of that vehicle is shown at the bottom left. The
green outline indicates a healthy vehicle, which fills with red as more damage
is taken. When the outline is full of red, the vehicle explodes.

The presence of an [Amp Station](../locations/Amp_Station.md) allows a shield to
be charged around the vehicle. This is shown by a blue ring around the green
outline, and also in the status bar at the bottom, as a separate gauge.

The vehicle outline may be changed for a more simple armor bar in the lower
status bar by clicking the appropriate down arrow.

For [ANT](../vehicles/Advanced_Nanite_Transport.md)'s, there is an
[NTU](../items/NTU.md) bar at the bottom which displays how many
[NTU](../items/NTU.md)'s have been stored from a warpgate to be transferred to
an [NTU Silo](../locations/NTU_Silo.md).

In the case of [BattleFrame Robotics](../vehicles/BattleFrame_Robotics.md), the
vehicle outline also displays the current state of the various BFR subsystems,
as green, yellow and red icons.

[Afterburner](../terminology/Afterburner.md) status, and vehicle speed are found
at the bottom, in the centre.

### Session Stats

This small window will show vital statistics about the current session:

- Time: How long this session has lasted.
- K/D: How many kills the soldier has made and how many time he has died, this
  session.
- A: How many Kill [Assists](../terminology/Assist.md) you have made.
- BEP: How many
  [Battle Experience Points](../terminology/Battle_Experience_Points.md) earned
  this session
- CEP: How many
  [Command Experience Points](../terminology/Command_Experience_Points.md)
  earned this session.
- SEP: How many
  [Support Experience Points](../terminology/Support_Experience_Points.md)
  earned this session.

These numbers reset when disconnected, even if only breifly. If you have to
reboot PlanetSide or your computer you will keep your K/D ratio and your
Assists, but your Time, BEP/CEP/SEP will be reset.

### PING Stats

Hidden by default, details of the current network connection can be shown as a
small window. (Default: SHIFT + . )

This shows Ping (Speed of messages from PC to Server, in milliseconds) and
Packet Loss (How many of the expected messages from the server didn't make it).

Network Communications is an exhaustive subject, but in general Green is Good
for these numbers, and simple tips to help this include:

- Play on the nearest server to you.
- Don't run other net-active programs while you play (Filesharing, Downloads,
  etc)
- Avoid playing during peak 'early evening' hours

This window also shows Frames Per Second (FPS), an indication of how fast and
smoothly everything will move, including you. Lowering detail settings (Video
Options) can improve this, but it will always spike in large indoor fights.

### Soldier Management Bar

This set of icons, lower right, provide access to a series of secondary detailed
information windows:

#### Inventory

(Default: I) The backpack icon allows access to the soldier's
[Inventory](../terminology/Inventory.md); pistol and rifle slots, and backpack.
Items may be picked up and dropped with the mouse pointer.

#### Character

(Default: O) This icon allows access to the soldier's Character Window,
containing details of experience progress, ranks, BRF Imprint Status, Greif
Points and Certifications. Training progress and career statistics can also be
found here.

#### [Map](../terminology/Map.md)

(Default: M) This icon opens the [Continental Map](Continental_Map.md), centered
on the soldier's current location.

#### Community Window

(Default: P) This opens the Community Window on the Squad tab, allowing squad
members to be kicked, promoted, and Platoons to be formed or disbanded.

Other tabs on this window allow [Friends List](../commands/Friends_List.md)
management and, [Ignore List](../terminology/Ignore.md) management.

#### Vehicle

(Default: Shift+V) This icon provides access to the Vehicle Management Window,
where lock status of the current vehicle may be altered, and passengers kicked
out.

#### Outfit

(Default: Shift+O) This icon opens the Outfit Window, where a list of outfit
members, their ranks and outfit point can be seen, as well as thier
online/offline status.

Senior [Outfit](../terminology/Outfit.md) members may edit outfit settings here.

#### Status & Chat Pane On/Off

This icon toggles the Status and Chat Window on or off.

#### Proximity Map On/Off

This icon toggles the Proximity or Radar Window on or off.

### Bio Pane

Located at the bottom left, a soldier's current
[Health](../terminology/Health.md), [Stamina](../terminology/Stamina.md) and
Armor totals are show in bar and numerical form.

- Red - Health
- Teal - Stamina
- Blue - Armor

### Hotkey Bar

Positioned in the centre of the status pane, the Hotkey bar contains eight
numbered fields corresponding to the F1-F8 function keys. Each can be used to
trigger [implants](../implants/Implants.md) (such as the
[Surge](../implants/Surge.md) implant), items (such as
[MedKits](../items/MedKit.md)), or text chat macros, by dragging the
corresponding icon from the [Inventory](../terminology/Inventory.md) or the
appropriate in-game panel to the hotkey you wish to assign.

### Holster Icons

Located lower right, the contents of any [holsters](Holster.md) are shown in
icon form. A faded icon indicates that a weapon is curently holstered.

Beneath the weapon is shown the number of shots left in the weapon, an icon
showing which type of ammunition is currently loaded, and the number of extra
rounds being carried in the [backpack](../terminology/Backpack.md), available
for reload.

The current fire-mode of the weapon is shown as a yellow pip to the left of the
gun, and is also shown as a status message in the Status Window when changed.

(Note: The
[Adaptive Construction Engine](../weapons/Adaptive_Construction_Engine.md) shows
the object it is set to make, rather than the ACE itself.)

In Vehicles, these icons are replaced with the currently available vehicle guns.

### Soldier Management Bar On/Off

This icon, located bottom right, hides or shows the Soldier Management toolbar,
above.

<!--[category:HUD](category:HUD.md)-->
