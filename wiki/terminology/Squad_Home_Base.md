Implemented April 8, 2005 with version [3.5.4](../patches/3.5.4.md).

## Squad Home Base

Squad Home Bases are intended to strengthen group cohesion at the Squad and
Platoon levels. The primary functions of the system includes:

- Squad or Platoon Leaders can view Squad member bind locations.
- Squad or Platoon Leaders can set a friendly facility as their Sqad/Platoon's
  Home Base for easy binding.
- Request that Squad/Platoon members matrix to their self-bind points.
- Request that Squad/Platoon members recall to Sanctuary.

A Commander may use a facility's [Main Console](../items/Main_Terminal.md) to
designate it as the Squad's Home Base. The home base will be designated on the
planetary and overhead proximity maps by a recognizable [waypoint](Waypoint.md)
marker (This waypoint is toggleable, just like other waypoints). When a
Squad/Platoon Member enters the facility's SOI, they will be asked if they would
like to bind to it. This bind will replace the soldier's [bind](Matrix.md) point
with a new bind point to the Home Base.

When a Commander wants to recall his troops to the home facility, he must go to
a friendly facility and issue the Command from that base's Main Console. When a
rematrix order is issued, followers who are bound to the home base will receive
a pop up box indicating that their commander has issued the order, where they
will recall to if they accept the order and a dialog asking if they wish to
follow this order. Soldiers who are not bound to the home base will not receive
this option but will be notified that their leader has issued the command.

Followers will have 60 seconds to accept the recall order and must exit any
vehicles before they can. If they accept, all implants will be deactivated and
weapons holstered and soldiers will begin the countdown to rematrix to the
[spawn tubes](../items/Respawn_Tube.md) of that location.

Similar to a recall to Sanctuary, if a follower takes damage or takes any action
other than typing or viewing the map, the recall countdown will be cancelled. If
they are still inside of the 60 second response window, the "Follow Order"
button will become active again for them to restart their recall. If they are
not in the 60 second answer window, the Commander who issued the command will
receive a message that the soldier did not respond to the command.

If the respawn ability at the Soldier's Bind location becomes unavailable (tubes
blown, [generator](../items/Generator.md) down, base [hack](Hack.md) goes
through and becomes enemy base, etc.) the order will cancel and both the soldier
and the leader will receive notification.

If a Squad or Platoon's Home Base is captured by an enemy, the waypoint will
disappear. If that facility was the soldier's bind location, it will be set to
"none" and they will receive a message in a center print and chat menu letting
them know that their Home Base has been lost. There is a 60 second lock out
timer between issuing orders to allow them to be resolved before new orders are
passed down.

## Command Tools

There are two different means by which a Leader can activate these features.
Major functionality will be accessed through a facility's
[Main Console](../items/Main_Terminal.md). To use the Main Console, a facility
has to be secure (unhacked) and fully powered (generator online), have at least
one functioning spawn tube and be in the control of the command leader's Empire.
In order to interact with the Main Console, it must be repaired beyond 50% just
like any other Console in the game. Also, the main Console cannot be hacked by
enemies to gain access to its functionality. An
[Advanced Hacker](../certifications/Advanced_Hacking.md) can hack the main
Console of a friendly facility that has been hacked by an enemy
[Empire](Empire.md), as long as it is powered and has at least one functional
spawn tube.

Soldiers over [Command Rank](Command_Rank.md) 2 have access to the
[Command Uplink Device](../weapons/Command_Uplink_Device.md) (CUD) to upload
orders and receive information from Empire systems. The Uplink Device does not
have the necessary connection to set a base as a "Home Base" or to issue a squad
rematrix order. However, they can be used to recall the squad or Platoon to
Sanctuary and Commanders will be able to receive information on the timers for
these abilities. The CUD is able to issue a Recall to Sanctuary order while in
the Sanctuary, but other functionality of the CUD is not available (such as
firing an [Orbital Strike](../commands/Orbital_Strike.md) on a Sanctuary).

The Squad List has two columns: One displays which facility each Squad member is
bound to, and the other is a checkbox that indicates if that Squad member is
bound to their Home Base.



