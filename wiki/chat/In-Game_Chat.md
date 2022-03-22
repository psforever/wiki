In-game chat is the system that players use to communicate with each other, as
well as receive information regarding the current battle.
![](../images/ChatHUD.gif){ class="figure" } **TOC**

# The Chat HUD

The main interface of the in-game chat system. This is where all communication
is sent and received.

(See Also: [HUD Chat Pane](../terminology/Heads-up_Display.md#status--chat-pane-onoff))

## Sections

The chat HUD is made up of different sections and buttons.

### Status Area

This is the top half of the chat HUD that displays
[System Messages](#System_Messages)

### Chat Area

This is the bottom half of the chat HUD that displays
[Chat Messages](#Chat_Messages)

### Text entry

This section is at the very bottom of the chat HUD and is used for text input

### Options

This button opens up the chat HUD options dialog box, allowing a user to define
what channels they wish to see, as well as set the default channel to send
messages to from the text entry area

### New

This button opens up a second chat HUD that can be customized in the same way as
the main chat HUD.

# Status Messages

These messages are not actual user communication, but messages regarding the
status of the current battle, the system and/or server, and other events of
importance to the player.

## Killspam

These messages indicate kills among players. They are formatted in the following
manner:

<killing player name> <weapon icon> <victim player name>

At times, the names will appear in brackets ( \[name\] ) to indicate that the
specific player was inside a vehicle or [turret](../terminology/Turret.md) at
the time of the kill/death.

These messages can be used to determine the current status of the battle at
hand, from warning nearby players that an enemy is near to informing friendly
soldiers that an enemy vehicle has been destroyed.

These messages are color-coded per empire.

- Red Name - [Terran Republic](../factions/Terran_Republic.md) Soldier
- Purple Name - [Vanu Sovereignty](../factions/Vanu_Sovereignty.md) Soldier
- Blue Name - [New Conglomerate](../factions/New_Conglomerate.md) Soldier

<!-- -->

- White Name - This can occur if a player is killed by projectiles that are not
  "owned" by anyone. This can occur with slow projectiles like
  [Flail](../vehicles/Flail.md) projectiles and
  [Orbital Strikes](../terminology/Orbital_Strike.md) when the player that fired them logs off
  before the projectile hits. Being killed by a flail weapon directly (before it
  hits the ground) will also result in white killspam. Special CSR abilities
  like [meteor](../items/Meteor.md) showers or CSR Orbital Strikes also appear
  as white in the killspam. In these cases the name of the
  [weapon](../weapons/Weapon.md)/[vehicle](../vehicles/index.md) that killed
  the player is listed under <killing player name> (ie. orbital_strike_big,
  orbital_strike_small, Mosquito) and a white skull as <weapon icon>.

**Note**: If a player's squad-mate is killed, their death notice will appear to
the player anywhere on the server, regardless of range to squad-mate.

## System Messages

These messages usually indicate server, system, and/or player information and
status. They are white in color by default. Typical messages include:

- Character has been saved
- [Cavern](../locations/Caverns.md) closure warnings and/or notices
- [Implant](../implants/index.md) Status
- System errors

## Tactical Information

These messages are the same color as System Messages, but provide tactical
information pertinent to the empire. Messages include:

- [LLU](../terminology/Lattice_Logic_Unit.md) Messages
- Facility Capture Messages
- [Continental Capture](../terminology/Continental_lock.md) Messages
- [Empire Benefit](../terminology/Empire_Benefit.md) Messages (typically in
  <font color="yellow">Yellow</font>)
- Facility warning messages
  - Low [NTU](../items/NTU.md) warning
  - Hacked facility warning
  - [Alert](../terminology/Alert.md) status
  - [Force Dome](../items/Force_Dome.md) status

## Vehicle Warnings/Status

These messages are either <font color="red">Red</font> or white, depending on
the message.

- <font color="red">Vehicle Stolen!</font> will appear if an enemy
  [Jacked](../terminology/Jack.md) your vehicle or one of your deployed
  [One-Manned Field Turrets](../weapons/One-Manned_Field_Turret.md). The message
  will also display in the center of your screen.
- Deconstruction Warnings will be desplayed in red if your vehicle is too close
  to certain objects and will deconstruct if not moved within the specified
  number of seconds. A white message is sometimes displayed to indicate a
  successful exit from the deconstruction zone.
- Gunner/Passenger status: White messages will indicate the name of the player
  that has just exited or entered your vehicle.

# Chat Messages

Chat messages are player to player communication on different channels.

## Chat Channels

The following is a list of all the chat channels, their respective colors, and
information about each.

- Local - <font color="#FFFFFF">White</font> - The default channel for most
  clients. This channel is seen by any friendly soldiers within 20 to 30 meters
  of each other. This channel also has certain rules:
  - Each empire has a separate local channel, in that you cannot pick up or
    transmit to an enemy local channel
  - Any [voice macros](../terminology/Voice_Macro.md) within local range used by
    both friendly and enemy soldiers will appear in this channel to you
- Broadcast - <font color="#C0C0FF">Purple</font> - Channel used for
  communicating to all friendly soldiers within the same friendly
  [SOI](../locations/Sphere_of_Influence.md) or continental wide if continent is
  [locked](../terminology/Continental_lock.md) by the player's own empire.
- [Private](Tell.md) - <font color="#66CCFF">Blue</font> - Used for private
  communication between players. Can be used to communicate with enemy soldiers.
- Squad - <font color="#FFDC00">Yellow</font> - Channel used by squad members to
  communicate with eachother with unlimited range, even on other continents.
  - Squad Leader - <font color="#FFD49A">Light Brown</font> - Channel used by
    squad leaders to communicate with eachother across an entire continent.
- Platoon - <font color="#FF8A00">Orange</font> - Similar to squad chat, it
  allows members of the same [platoon](../terminology/Platoon.md) to communicate
  with eachother at an unlimited range.
  - Platoon Leader - <font color="#CC967A">Brown</font> - Channel used solely by
    leaders of each squad in the same platoon to coordinate platoon movement.
- Outfit - <font color="#40FF40">Green</font> - Channel used by members of the
  same [outfit](../terminology/Outfit.md) to communicate with eachother at an
  unlimited range.
- Command - <font color="#80FFD4">Teal</font> - Channel used by soldiers of the
  same [Command Rank](../terminology/Command_Rank.md) (Command Rank 2 or above),
  as well as continental and global messages sent by friendly CR5s, with range
  varying on command rank. Situation Reports, reports that a Commander can send
  to Commanders that are one level above him, also use this color.
  - Command Rank 2 - Small range, close to the range of an
    [SOI](../locations/Sphere_of_Influence.md)
  - Command Rank 3 - Medium range, close to about 3
    [SOIs](../locations/Sphere_of_Influence.md)
  - Command Rank 4 - Continental range, seen by all CR4 soldiers on the same
    continent
  - Command Rank 5 - Global range, seen by all CR5 soldiers on the server
- CSR World Broadcast - <font color="#FF8080">Red</font> - **This channel can
  only be used by CSRs**, yet can be seen by all players of all empires on the
  same server.
  - CSR Tell - Used by CSRs for private communication between the CSR and
    player, similar to the regular tell, except for its color and tag.

# Sending Messages

Sending messages is straight-forward. By default, a player simply has to hit
Enter in order to activate the chat entry mode.

## Sending to different channels

Players can send chat to different channels using a variety of commands.
|     |     |
| --- | --- |
| * Local Channel<br>    * /local<br>    * /l<br>* Broadcast Channel<br>    * /broadcast<br>    * /b<br>* Private Chat<br>    * /tell \- Sends a private message to a specific player<br>        <br>        * /t<br>        * Double-clicking on the name of a squad-mate<br>        <br>    * /reply \- Replies to last private message received<br>        <br>        * /r<br>        * Backspace key<br>        <br>* Squad Channel<br>    * /squad<br>    * /s | * Squad Leader Channel<br>    * /sl<br>* Platoon Channel<br>    * /platoon<br>    * /p<br>* Platoon Leader Channel<br>    * /pl<br>* Outfit Channel<br>    * /outfit<br>    * /o<br>* Command Channel<br>    * /command<br>    * /c<br>    * /sitrep<br>    * For CR5 continental and global chat commands, please see [Commands](Chat_Commands.md)<br>* [Black Ops](../factions/Black_Ops.md) Channel<br>    * /b<br>    * /c |

## Custom Colors

It is possible to customize the color of chat messages you send.

Please see [Color Codes](Color_Codes.md) for details on how to do this.
