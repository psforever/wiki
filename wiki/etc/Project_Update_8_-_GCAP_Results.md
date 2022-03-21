**Original Post by Chord - Monday February 29th, 2016**

I've just created a new tool, GCAPy, to help parse the nearly 1 million packets
that were submitted. It's open sourced online and it helped me get some
statistics below.

Code: Select all Packet statistics for 9,813,764 packets

**Top 10 Rarest:**

`1. 65 0x41 DismountVehicleCargoMsg (1)`
`2. 141 0x8d OutfitMembershipResponse (1)`
`3. 184 0xb8 ExperienceAddedMessage (1)` `4. 165 0xa5 WarpgateResponse (3)`
`5. 90 0x5a DelayedPathMountMsg (5)` `6. 101 0x65 AvatarSearchResponse (5)`
`7. 228 0xe4 MissionActionMessage (5)` `8. 10 0xa HitHint (9)`
`9. 34 0x22 ActionCancelMessage (9)`

10\. 66 0x42 CargoMountPointStatusMessage (12)

**Top 10 Most frequent:**

`1. 0 0x0 UnknownMessage0 (3548307)` `2. 8 0x8 PlayerStateMessage (2160171)`
`3. 44 0x2c PlanetsideAttributeMessage (968496)`
`4. 189 0xbd UnknownMessage189 (449497)`
`5. 27 0x1b VehicleStateMessage (297619)`
`6. 25 0x19 ObjectDeleteMessage (201468)`
`7. 97 0x61 ObjectDetectedMessage (184525)`
`8. 160 0xa0 BuildingInfoUpdateMessage (152807)`
`9. 205 0xcd DensityLevelUpdateMessage (144753)`

10\. 80 0x50 TargetingInfoMessage (144126)

**Missing 113 packets:**

`3 ( UnknownMessage3) 6 ( UnknownMessage6)`

`7 ( UnknownMessage7) 9 ( UnknownMessage9)`
`14 ( MountVehicleMsg) 15 ( DismountVehicleMsg)`
`17 ( UnknownMessage17) 19 ( CharacterNoRecordMessage)`
`21 ( UnknownMessage21) 26 ( UnknownMessage26)`
`32 ( UnknownMessage32) 35 ( ActionCancelAcknowledgeMessage)`
`43 ( UnknownMessage43) 45 ( UnknownMessage45)`
`46 ( UnknownMessage46) 47 ( UnknownMessage47)`
`48 ( UnknownMessage48) 52 ( WeaponFireMessage)`
`53 ( UnknownMessage53) 54 ( UnknownMessage54)`
`55 ( UnknownMessage55) 59 ( UnknownMessage59)`
`60 ( UnknownMessage60) 64 ( MountVehicleCargoMsg)`
`68 ( UnknownMessage68) 73 ( UnknownMessage73)`
`74 ( SpawnRequestMessage) 76 ( UnknownMessage76)`
`79 ( UnknownMessage79) 83 ( UnknownMessage83)`
`85 ( DroppodLaunchResponseMessage) 89 ( UnknownMessage89)`
`92 ( UnknownMessage92) 93 ( UnknownMessage93)`
`94 ( UnknownMessage94) 95 ( FavoritesResponse)`
`98 ( UnknownMessage98) 102 ( WeaponJammedMessage)`

103 ( LinkDeadAwarenessMsg) 108 ( UnknownMessage108) 109 ( UnknownMessage109)
110 ( UnknownMessage110) 114 ( UnknownMessage114) 117 ( TrainingZoneMessage) 121
( TradeMessage) 122 ( UnknownMessage122) 124 ( UnknownMessage124) 125 (
UnknownMessage125) 126 ( UnknownMessage126) 131 ( UnknownMessage131) 133 (
OffshoreVehicleMessage) 136 ( UnknownMessage136) 137 ( UnknownMessage137) 139 (
UnknownMessage139) 140 ( UnknownMessage140) 142 ( UnknownMessage142) 147 (
DataChallengeMessage) 148 ( UnknownMessage148) 151 ( UnknownMessage151) 154 (
UnknownMessage154) 156 ( DebugDrawMessage) 157 ( SoulMarkMessage) 162 (
UnknownMessage162) 164 ( UnknownMessage164) 170 ( UnknownMessage170) 171 (
UnknownMessage171) 172 ( UnknownMessage172) 174 ( CSAssistMessage) 175 (
CSAssistCommentMessage) 176 ( UnknownMessage176) 177 ( UnknownMessage177) 178 (
VoiceHostInfo) 181 ( UnknownMessage181) 183 ( DisconnectMessage) 188 ( SnoopMsg)
191 ( ZipLineMessage) 194 ( UnknownMessage194) 196 ( QuantityDeltaUpdateMessage)
199 ( UnknownMessage199) 202 ( OutfitBenefitMessage) 204 (
ClockCalibrationMessage) 206 ( ActOfGodMessage) 208 ( UnknownMessage208) 210 (
RespawnAMSInfoMessage) 212 ( UnknownMessage212) 214 (
WarpgateLinkOverrideMessage) 216 ( ForceEmpireMessage) 218 ( UnknownMessage218)
219 ( UnknownMessage219) 221 ( SquadOrderMessage) 222 ( UnknownMessage222) 225 (
AudioSequenceMessage) 229 ( UnknownMessage229) 234 ( RabbitUpdateMessage) 237 (
GameScoreUpdateMessage) 238 ( UnknownMessage238) 239 ( UnknownMessage239) 240 (
QueueTimedHelpMessage) 241 ( MailMessage) 242 ( UnknownMessage242) 243 (
ClientCheatedMessage) 244 ( UnknownMessage244) 245 ( UnknownMessage245) 246 (
UnknownMessage246) 247 ( UnknownMessage247) 248 ( UnknownMessage248) 249 (
UnknownMessage249) 250 ( UnknownMessage250) 251 ( UnknownMessage251) 252 (
UnknownMessage252) 253 ( UnknownMessage253) 254 ( UnknownMessage254) 255 (
UnknownMessage255)

Some observations from the statistics:

- There are a lot of missing packets. Most of these have unknown names because a
  tool I wrote wasn't able to extract all of them from the planetside binary
- Some things we're never going to be able to capture, such as 'ZipLineMessage'
  without access to core combat
- The most frequent packet of 0x00 isn't actually unknown, but it represents a
  control packet (used for special packets which have their own opcode space).
  It should be named accordingly

I'm sure there is some more data that can be drawn from this, but it's a good
start!

[Original Post](http://psforever.net/forum/viewtopic.php?f=11&t=146)

<!--[Category:PSForever Updates](Category:PSForever_Updates.md)-->
