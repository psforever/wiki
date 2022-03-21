## Game Packet Listing

| Packet ID | Packet ID (hex) | Name                                      | Status | Note                                                     |
| --------- | --------------- | ----------------------------------------- | ------ | -------------------------------------------------------- |
| 0         | 0x0             | _Missing_                                 | ???    |                                                          |
| 1         | 0x1             | LoginMessage                              |        |                                                          |
| 2         | 0x2             | LoginRespMessage                          |        |                                                          |
| 3         | 0x3             | ConnectToWorldRequestMessage              |        |                                                          |
| 4         | 0x4             | ConnectToWorldMessage                     |        |                                                          |
| 5         | 0x5             | VNLWorldStatusMessage                     |        |                                                          |
| 6         | 0x6             | _Missing_                                 | ???    |                                                          |
| 7         | 0x7             | _Missing_                                 | ???    |                                                          |
| 8         | 0x8             | PlayerStateMessage                        |        |                                                          |
| 9         | 0x9             | HitMessage                                |        |                                                          |
| 10        | 0xa             | HitHint                                   |        |                                                          |
| 11        | 0xb             | DamageMessage                             |        |                                                          |
| 12        | 0xc             | DestroyMessage                            |        |                                                          |
| 13        | 0xd             | ReloadMessage                             |        |                                                          |
| 14        | 0xe             | MountVehicleMsg                           |        |                                                          |
| 15        | 0xf             | DismountVehicleMsg                        |        |                                                          |
| 16        | 0x10            | UseItemMessage                            |        |                                                          |
| 17        | 0x11            | MoveItemMessage                           |        |                                                          |
| 18        | 0x12            | ChatMsg                                   |        |                                                          |
| 19        | 0x13            | CharacterNoRecordMessage                  |        |                                                          |
| 20        | 0x14            | CharacterInfoMessage                      |        |                                                          |
| 21        | 0x15            | _Missing_                                 | ???    |                                                          |
| 22        | 0x16            | BindPlayerMessage                         |        |                                                          |
| 23        | 0x17            | ObjectCreateMessage                       |        | It appears that both 0x17 and 0x18 represent this packet |
| 24        | 0x18            | ObjectCreateMessage                       |        |                                                          |
| 25        | 0x19            | ObjectDeleteMessage                       |        |                                                          |
| 26        | 0x1a            | PingMsg                                   |        |                                                          |
| 27        | 0x1b            | VehicleStateMessage                       |        |                                                          |
| 28        | 0x1c            | FrameVehicleStateMessage                  |        |                                                          |
| 29        | 0x1d            | GenericObjectStateMsg                     |        |                                                          |
| 30        | 0x1e            | ChildObjectStateMessage                   |        |                                                          |
| 31        | 0x1f            | _Missing_                                 | ???    |                                                          |
| 32        | 0x20            | _Missing_                                 | ???    |                                                          |
| 33        | 0x21            | ActionProgressMessage                     |        |                                                          |
| 34        | 0x22            | ActionCancelMessage                       |        |                                                          |
| 35        | 0x23            | ActionCancelAcknowledgeMessage            |        |                                                          |
| 36        | 0x24            | SetEmpireMessage                          |        |                                                          |
| 37        | 0x25            | EmoteMsg                                  |        |                                                          |
| 38        | 0x26            | UnuseItemMessage                          |        |                                                          |
| 39        | 0x27            | ObjectDetachMessage                       |        |                                                          |
| 40        | 0x28            | CreateShortcutMessage                     |        |                                                          |
| 41        | 0x29            | ChangeShortcutBankMessage                 |        |                                                          |
| 42        | 0x2a            | ObjectAttachMessage                       |        |                                                          |
| 43        | 0x2b            | _Missing_                                 | ???    |                                                          |
| 44        | 0x2c            | PlanetsideAttributeMessage                |        |                                                          |
| 45        | 0x2d            | RequestDestroyMessage                     |        |                                                          |
| 46        | 0x2e            | _Missing_                                 | ???    |                                                          |
| 47        | 0x2f            | CharacterCreateRequestMessage             |        |                                                          |
| 48        | 0x30            | CharacterRequestMessage                   |        |                                                          |
| 49        | 0x31            | LoadMapMessage                            |        |                                                          |
| 50        | 0x32            | SetCurrentAvatarMessage                   |        |                                                          |
| 51        | 0x33            | ObjectHeldMessage                         |        |                                                          |
| 52        | 0x34            | WeaponFireMessage                         |        |                                                          |
| 53        | 0x35            | AvatarJumpMessage                         |        |                                                          |
| 54        | 0x36            | PickupItemMessage                         |        |                                                          |
| 55        | 0x37            | DropItemMessage                           |        |                                                          |
| 56        | 0x38            | InventoryStateMessage                     |        |                                                          |
| 57        | 0x39            | ChangeFireStateMessage                    |        |                                                          |
| 58        | 0x3a            | ChangeFireStateMessage                    |        |                                                          |
| 59        | 0x3b            | _Missing_                                 | ???    |                                                          |
| 60        | 0x3c            | GenericCollisionMsg                       |        |                                                          |
| 61        | 0x3d            | QuantityUpdateMessage                     |        |                                                          |
| 62        | 0x3e            | ArmorChangedMessage                       |        |                                                          |
| 63        | 0x3f            | ProjectileStateMessage                    |        |                                                          |
| 64        | 0x40            | MountVehicleCargoMsg                      |        |                                                          |
| 65        | 0x41            | DismountVehicleCargoMsg                   |        |                                                          |
| 66        | 0x42            | CargoMountPointStatusMessage              |        |                                                          |
| 67        | 0x43            | BeginZoningMessage                        |        |                                                          |
| 68        | 0x44            | ItemTransactionMessage                    |        |                                                          |
| 69        | 0x45            | ItemTransactionResultMessage              |        |                                                          |
| 70        | 0x46            | ChangeFireModeMessage                     |        |                                                          |
| 71        | 0x47            | ChangeAmmoMessage                         |        |                                                          |
| 72        | 0x48            | TimeOfDayMessage                          |        |                                                          |
| 73        | 0x49            | _Missing_                                 | ???    |                                                          |
| 74        | 0x4a            | SpawnRequestMessage                       |        |                                                          |
| 75        | 0x4b            | DeployRequestMessage                      |        |                                                          |
| 76        | 0x4c            | _Missing_                                 | ???    |                                                          |
| 77        | 0x4d            | RepairMessage                             |        |                                                          |
| 78        | 0x4e            | ServerVehicleOverrideMsg                  |        |                                                          |
| 79        | 0x4f            | LashMessage                               |        |                                                          |
| 80        | 0x50            | TargetingInfoMessage                      |        |                                                          |
| 81        | 0x51            | TriggerEffectMessage                      |        |                                                          |
| 82        | 0x52            | WeaponDryFireMessage                      |        |                                                          |
| 83        | 0x53            | DroppodLaunchRequestMessage               |        |                                                          |
| 84        | 0x54            | HackMessage                               |        |                                                          |
| 85        | 0x55            | DroppodLaunchResponseMessage              |        |                                                          |
| 86        | 0x56            | GenericObjectActionMessage                |        |                                                          |
| 87        | 0x57            | AvatarVehicleTimerMessage                 |        |                                                          |
| 88        | 0x58            | AvatarImplantMessage                      |        |                                                          |
| 89        | 0x59            | _Missing_                                 | ???    |                                                          |
| 90        | 0x5a            | DelayedPathMountMsg                       |        |                                                          |
| 91        | 0x5b            | OrbitalShuttleTimeMsg                     |        |                                                          |
| 92        | 0x5c            | AIDamage                                  |        |                                                          |
| 93        | 0x5d            | DeployObjectMessage                       |        |                                                          |
| 94        | 0x5e            | FavoritesRequest                          |        |                                                          |
| 95        | 0x5f            | FavoritesResponse                         |        |                                                          |
| 96        | 0x60            | FavoritesMessage                          |        |                                                          |
| 97        | 0x61            | ObjectDetectedMessage                     |        |                                                          |
| 98        | 0x62            | SplashHitMessage                          |        |                                                          |
| 99        | 0x63            | SetChatFilterMessage                      |        |                                                          |
| 100       | 0x64            | AvatarSearchCriteriaMessage               |        |                                                          |
| 101       | 0x65            | AvatarSearchResponse                      |        |                                                          |
| 102       | 0x66            | WeaponJammedMessage                       |        |                                                          |
| 103       | 0x67            | LinkDeadAwarenessMsg                      |        |                                                          |
| 104       | 0x68            | DroppodFreefallingMessage                 |        |                                                          |
| 105       | 0x69            | AvatarFirstTimeEventMessage               |        |                                                          |
| 106       | 0x6a            | AggravatedDamageMessage                   |        |                                                          |
| 107       | 0x6b            | TriggerSoundMessage                       |        |                                                          |
| 108       | 0x6c            | LootItemMessage                           |        |                                                          |
| 109       | 0x6d            | VehicleSubStateMessage                    |        |                                                          |
| 110       | 0x6e            | SquadMembershipRequest                    |        |                                                          |
| 111       | 0x6f            | SquadMembershipResponse                   |        |                                                          |
| 112       | 0x70            | SquadMemberEvent                          |        |                                                          |
| 113       | 0x71            | PlatoonEvent                              |        |                                                          |
| 114       | 0x72            | FriendsRequest                            |        |                                                          |
| 115       | 0x73            | FriendsResponse                           |        |                                                          |
| 116       | 0x74            | TriggerEnvironmentalDamageMessage         |        |                                                          |
| 117       | 0x75            | TrainingZoneMessage                       |        |                                                          |
| 118       | 0x76            | DeployableObjectsInfoMessage              |        |                                                          |
| 119       | 0x77            | SquadState                                |        |                                                          |
| 120       | 0x78            | OxygenStateMessage                        |        |                                                          |
| 121       | 0x79            | TradeMessage                              |        |                                                          |
| 122       | 0x7a            | _Missing_                                 | ???    |                                                          |
| 123       | 0x7b            | DamageFeedbackMessage                     |        |                                                          |
| 124       | 0x7c            | DismountBuildingMsg                       |        |                                                          |
| 125       | 0x7d            | _Missing_                                 | ???    |                                                          |
| 126       | 0x7e            | _Missing_                                 | ???    |                                                          |
| 127       | 0x7f            | AvatarStatisticsMessage                   |        |                                                          |
| 128       | 0x80            | GenericObjectAction2Message               |        |                                                          |
| 129       | 0x81            | DestroyDisplayMessage                     |        |                                                          |
| 130       | 0x82            | TriggerBotAction                          |        |                                                          |
| 131       | 0x83            | SquadWaypointRequest                      |        |                                                          |
| 132       | 0x84            | SquadWaypointEvent                        |        |                                                          |
| 133       | 0x85            | OffshoreVehicleMessage                    |        |                                                          |
| 134       | 0x86            | ObjectDeployedMessage                     |        |                                                          |
| 135       | 0x87            | ObjectDeployedCountMessage                |        |                                                          |
| 136       | 0x88            | WeaponDelayFireMessage                    |        |                                                          |
| 137       | 0x89            | BugReportMessage                          |        |                                                          |
| 138       | 0x8a            | PlayerStasisMessage                       |        |                                                          |
| 139       | 0x8b            | _Missing_                                 | ???    |                                                          |
| 140       | 0x8c            | OutfitMembershipRequest                   |        |                                                          |
| 141       | 0x8d            | OutfitMembershipResponse                  |        |                                                          |
| 142       | 0x8e            | OutfitRequest                             |        |                                                          |
| 143       | 0x8f            | OutfitEvent                               |        |                                                          |
| 144       | 0x90            | OutfitMemberEvent                         |        |                                                          |
| 145       | 0x91            | OutfitMemberUpdate                        |        |                                                          |
| 146       | 0x92            | PlanetsideStringAttributeMessage          |        |                                                          |
| 147       | 0x93            | DataChallengeMessage                      |        |                                                          |
| 148       | 0x94            | DataChallengeMessageResp                  |        |                                                          |
| 149       | 0x95            | WeatherMessage                            |        |                                                          |
| 150       | 0x96            | SimDataChallenge                          |        |                                                          |
| 151       | 0x97            | SimDataChallengeResp                      |        |                                                          |
| 152       | 0x98            | OutfitListEvent                           |        |                                                          |
| 153       | 0x99            | EmpireIncentivesMessage                   |        |                                                          |
| 154       | 0x9a            | InvalidTerrainMessage                     |        |                                                          |
| 155       | 0x9b            | SyncMessage                               |        |                                                          |
| 156       | 0x9c            | DebugDrawMessage                          |        |                                                          |
| 157       | 0x9d            | SoulMarkMessage                           |        |                                                          |
| 158       | 0x9e            | UplinkPositionEvent                       |        |                                                          |
| 159       | 0x9f            | HotSpotUpdateMessage                      |        |                                                          |
| 160       | 0xa0            | BuildingInfoUpdateMessage                 |        |                                                          |
| 161       | 0xa1            | FireHintMessage                           |        |                                                          |
| 162       | 0xa2            | UplinkRequest                             |        |                                                          |
| 163       | 0xa3            | UplinkResponse                            |        |                                                          |
| 164       | 0xa4            | WarpgateRequest                           |        |                                                          |
| 165       | 0xa5            | WarpgateResponse                          |        |                                                          |
| 166       | 0xa6            | DamageWithPositionMessage                 |        |                                                          |
| 167       | 0xa7            | GenericActionMessage                      |        |                                                          |
| 168       | 0xa8            | ContinentalLockUpdateMessage              |        |                                                          |
| 169       | 0xa9            | AvatarGrenadeStateMessage                 |        |                                                          |
| 170       | 0xaa            | _Missing_                                 | ???    |                                                          |
| 171       | 0xab            | _Missing_                                 | ???    |                                                          |
| 172       | 0xac            | ReleaseAvatarRequestMessage               |        |                                                          |
| 173       | 0xad            | AvatarDeadStateMessage                    |        |                                                          |
| 174       | 0xae            | CSAssistMessage                           |        |                                                          |
| 175       | 0xaf            | CSAssistCommentMessage                    |        |                                                          |
| 176       | 0xb0            | VoiceHostRequest                          |        |                                                          |
| 177       | 0xb1            | VoiceHostKill                             |        |                                                          |
| 178       | 0xb2            | VoiceHostInfo                             |        |                                                          |
| 179       | 0xb3            | BattleplanMessage                         |        |                                                          |
| 180       | 0xb4            | BattleExperienceMessage                   |        |                                                          |
| 181       | 0xb5            | TargetingImplantRequest                   |        |                                                          |
| 182       | 0xb6            | ZonePopulationUpdateMessage               |        |                                                          |
| 183       | 0xb7            | DisconnectMessage                         |        |                                                          |
| 184       | 0xb8            | ExperienceAddedMessage                    |        |                                                          |
| 185       | 0xb9            | OrbitalStrikeWaypointMessage              |        |                                                          |
| 186       | 0xba            | KeepAliveMessage                          |        |                                                          |
| 187       | 0xbb            | MapObjectStateBlockMessage                |        |                                                          |
| 188       | 0xbc            | SnoopMsg                                  |        |                                                          |
| 189       | 0xbd            | PlayerStateMessageUpstream                |        |                                                          |
| 190       | 0xbe            | PlayerStateShiftMessage                   |        |                                                          |
| 191       | 0xbf            | ZipLineMessage                            |        |                                                          |
| 192       | 0xc0            | CaptureFlagUpdateMessage                  |        |                                                          |
| 193       | 0xc1            | VanuModuleUpdateMessage                   |        |                                                          |
| 194       | 0xc2            | FacilityBenefitShieldChargeRequestMessage |        |                                                          |
| 195       | 0xc3            | ProximityTerminalUseMessage               |        |                                                          |
| 196       | 0xc4            | QuantityDeltaUpdateMessage                |        |                                                          |
| 197       | 0xc5            | ChainLashMessage                          |        |                                                          |
| 198       | 0xc6            | ZoneInfoMessage                           |        |                                                          |
| 199       | 0xc7            | LongRangeProjectileInfoMessage            |        |                                                          |
| 200       | 0xc8            | WeaponLazeTargetPositionMessage           |        |                                                          |
| 201       | 0xc9            | ModuleLimitsMessage                       |        |                                                          |
| 202       | 0xca            | OutfitBenefitMessage                      |        |                                                          |
| 203       | 0xcb            | EmpireChangeTimeMessage                   |        |                                                          |
| 204       | 0xcc            | ClockCalibrationMessage                   |        |                                                          |
| 205       | 0xcd            | DensityLevelUpdateMessage                 |        |                                                          |
| 206       | 0xce            | ActOfGodMessage                           |        |                                                          |
| 207       | 0xcf            | AvatarAwardMessage                        |        |                                                          |
| 208       | 0xd0            | _Missing_                                 | ???    |                                                          |
| 209       | 0xd1            | DisplayedAwardMessage                     |        |                                                          |
| 210       | 0xd2            | RespawnAMSInfoMessage                     |        |                                                          |
| 211       | 0xd3            | ComponentDamageMessage                    |        |                                                          |
| 212       | 0xd4            | GenericObjectActionAtPositionMessage      |        |                                                          |
| 213       | 0xd5            | PropertyOverrideMessage                   |        |                                                          |
| 214       | 0xd6            | WarpgateLinkOverrideMessage               |        |                                                          |
| 215       | 0xd7            | EmpireBenefitsMessage                     |        |                                                          |
| 216       | 0xd8            | ForceEmpireMessage                        |        |                                                          |
| 217       | 0xd9            | BroadcastWarpgateUpdateMessage            |        |                                                          |
| 218       | 0xda            | _Missing_                                 | ???    |                                                          |
| 219       | 0xdb            | SquadMainTerminalMessage                  |        |                                                          |
| 220       | 0xdc            | SquadMainTerminalResponseMessage          |        |                                                          |
| 221       | 0xdd            | SquadOrderMessage                         |        |                                                          |
| 222       | 0xde            | SquadOrderResponse                        |        |                                                          |
| 223       | 0xdf            | ZoneLockInfoMessage                       |        |                                                          |
| 224       | 0xe0            | SquadBindInfoMessage                      |        |                                                          |
| 225       | 0xe1            | AudioSequenceMessage                      |        |                                                          |
| 226       | 0xe2            | SquadFacilityBindInfoMessage              |        |                                                          |
| 227       | 0xe3            | ZoneForcedCavernConnectionsMessage        |        |                                                          |
| 228       | 0xe4            | MissionActionMessage                      |        |                                                          |
| 229       | 0xe5            | MissionKillTriggerMessage                 |        |                                                          |
| 230       | 0xe6            | ReplicationStreamMessage                  |        |                                                          |
| 231       | 0xe7            | SquadDefinitionActionMessage              |        |                                                          |
| 232       | 0xe8            | SquadDetailDefinitionUpdateMessage        |        |                                                          |
| 233       | 0xe9            | TacticsMessage                            |        |                                                          |
| 234       | 0xea            | RabbitUpdateMessage                       |        |                                                          |
| 235       | 0xeb            | SquadInvitationRequestMessage             |        |                                                          |
| 236       | 0xec            | CharacterKnowledgeMessage                 |        |                                                          |
| 237       | 0xed            | GameScoreUpdateMessage                    |        |                                                          |
| 238       | 0xee            | _Missing_                                 | ???    |                                                          |
| 239       | 0xef            | OrderTerminalBugMessage                   |        |                                                          |
| 240       | 0xf0            | QueueTimedHelpMessage                     |        |                                                          |
| 241       | 0xf1            | MailMessage                               |        |                                                          |
| 242       | 0xf2            | GameVarUpdate                             |        |                                                          |
| 243       | 0xf3            | ClientCheatedMessage                      |        |                                                          |
| 244       | 0xf4            | _Missing_                                 | ???    |                                                          |
| 245       | 0xf5            | _Missing_                                 | ???    |                                                          |
| 246       | 0xf6            | _Missing_                                 | ???    |                                                          |
| 247       | 0xf7            | _Missing_                                 | ???    |                                                          |
| 248       | 0xf8            | _Missing_                                 | ???    |                                                          |
| 249       | 0xf9            | _Missing_                                 | ???    |                                                          |
| 250       | 0xfa            | _Missing_                                 | ???    |                                                          |
| 251       | 0xfb            | _Missing_                                 | ???    |                                                          |
| 252       | 0xfc            | _Missing_                                 | ???    |                                                          |
| 253       | 0xfd            | _Missing_                                 | ???    |                                                          |
| 254       | 0xfe            | _Missing_                                 | ???    |                                                          |
| 255       | 0xff            | _Missing_                                 | ???    |                                                          |
