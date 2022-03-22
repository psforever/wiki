There are a few things that need to be looked in to before the game shuts down.
While packet captures are great, how things are arranged in memory is really
crucial for reverse engineering.

1\. Capture memory dumps of game activity combined with HQ video and full packet
captures. All memory dumps should be loadable in to IDA Pro. Memory dumps should
be synced with the capture and video. A tool can be written later to combine the
video and network packets. Detailed notes should be taken to help the user
identify strange things.

Locations:

- VR Training
- Character creation screen
- Server selection
- A battle on a continent

Notes:

- Memory dump tool with periodic option -
  <https://technet.microsoft.com/en-us/sysinternals/dd996900.aspx>
- IDA memory dump help -
  <https://stackoverflow.com/questions/29433415/analyzing-binary-taken-from-memory-dump-in-ida-pro>
- TakeSnaphot IDA -
  <https://www.hex-rays.com/products/ida/support/idadoc/1470.shtml>
