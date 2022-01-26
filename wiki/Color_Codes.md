**Color codes** will help you change the Color of your message or macro.

## Chat pane

When using the in-game chat (for instance, the output of a
[Macro](Macro "wikilink")) you use a single character code to denote
which color to use. (1-F, i.e., a single Hexadecimal digit).

The Command for this is:

-   <Channel> \\#<hexdigit> <message>
    -   <Channel> - The Channel you want your message to go to, this can
        be /o ([Outfit](Outfit "wikilink")), /s
        ([Squad](Squad "wikilink")), /p ([Platoon](Platoon "wikilink")),
        /b (Broadcast), /l (Local) or /c (Command).
    -   <hexdigit> - The number or letter of the color that you want
        your message to be.
    -   <message> - The message that you want colorized.

For example:

If you want to make an Outfit message in Yellow saying 'Incoming
Troops!', you would have to type this:

-   /o \\#3 Incoming Troops!

And it will appear like this:

-   <FONT Color=#40FE40>\[Outfit\] Name:</font>
    <FONT Color=#FFDC00>Incoming Troops!</font>

Here is a list of which number generates which color:

-   0 - <FONT Color=#FFFFFF>White</font> (Default Local Chat Color)
-   1 - <FONT Color=#000000>Black</font>
-   2 - <FONT Color=#66CCFF>Light blue</font>
-   3 - <FONT Color=#FFDC00>Yellow</font> (Default Squad Chat Color)
-   4 - <FONT Color=#40FE40>Green</font> (Default Outfit Chat Color)
-   5 - <FONT Color=#80FED3>Light green</font> (Default Command Chat and
    Global Chat Color)
-   6 - <FONT Color=#CB967A>Brown</font> (Default Platoon Chat Color)
-   7 - <FONT Color=#BFBFFE>Light purple</font> (Default Broadcast Chat
    Color)
-   8 - <FONT Color=#F440FF>Pink</font>
-   9 - <FONT Color=#9640FF>Purple</font>
-   a - <FONT Color=#40FCFE>Turquoise</font>
-   b - <FONT Color=#DEFE7F>Light yellow</font>
-   c - <FONT Color=#2E4CE6>Blue</font>
-   d - <FONT Color=#FFBFFF>Light pink</font>
-   e - <FONT Color=#C9FEBE>Light green</font>
-   f - <FONT Color=#FFCCB2>Brown/Pink</font>

## Outfit Message of the Day

The Message of the Day displayed on the Outfit pane (and editable only
by the Outfit Leader) uses a similar scheme, but instead of a single
hexadecimal digit, uses a six-character scheme similar to HTML.

The Command for this is:

-   \\#<red><green><blue> <message>
    -   <red> - The two hexadecimal digit for the amount of red in the
        color used (range: 00 - FF).
    -   <green> - The two hexadecimal digit for the amount of red in the
        color used (range: 00 - FF).
    -   <blue> - The two hexadecimal digit for the amount of red in the
        color used (range: 00 - FF).
    -   <message> - The message that you want colorized.

For example:

If you want to make an Message of the Day in Pink saying 'BFR event this
Friday!', you would have to type this:

-   \\#F440FF BFR event this Friday!

And it will appear like this:

-   <FONT Color=#F440FF>BFR event this Friday!</font>

There are over 16 million possible color combinations and details of how
to create specific colors is beyond the scope of this wiki. Please refer
to tools such as the [W3 School's List of HTML Color
Names](http://www.w3schools.com/tags/ref_colornames.asp).

[Category:Commands](Category:Commands "wikilink")