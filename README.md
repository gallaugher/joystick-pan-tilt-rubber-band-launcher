This is a project for my Physical Computing Course where students create a "rubber band launcher" using 3 cheap servos, a joystick, a Raspberry Pi Pico 2w (should work with original, Wi-Fi / w not necessary), and a 3D-printed pan-tilt mechanism.
The 3D printed pan tilt I used is from here:
https://www.thingiverse.com/thing:2467743
The screws are all those incldued with standard servos, except for the one that provides the tilt axis. For this I used a 12mm M2.5 with nut on the outside.

Parts:
- Raspberry Pi Pico 2w (any pico should work) - https://www.adafruit.com/product/6315
- 3 Micro servos - TowerPro SG92R - https://www.adafruit.com/product/169
- M2.5" Screw with nut - individually these are super-cheap, but I have a complete kit for my experimental builds that I find useful - https://www.adafruit.com/product/3299
- 2 mini Breadboard - I use Monk Makes since Pico pin names are on the board - https://www.adafruit.com/product/5422
  You could use a single large breadboard for this, too.
- Joystick - I bought a bunch of these super-cheap ones off AliExpress, although I found the x and y values printed on the stick are opposite when one actually places these pins in the breadboard. So in my code you'll see what's labeled as X-axis as actually controlling the vertical axis, and vice-versa. - https://www.aliexpress.us/item/3256806299955871.html
  Joysticks are standard. They behalve like two potentiometers, so any stnadard joystick should work.
- A single momentary push button - Any standard button will work. I buy a bunch like this for my students - https://a.co/d/fdZCdJZ
  Note: Most joysticks include a wire for a button, that registeres when the joystick is tapped, but I found this was awkward on joysticks vertically mounted on the breadboard, so I had students use a separate button. If you laser-cut a wooden case & mounted the joystick, you could likely use the built-in button instead.
- At least 15 pin-pin breadboard wires. - a pack like this is fine - https://www.adafruit.com/product/1957
- A microUSB cable that supports data transfer, NOT a power-only cable.
- A wooden stick (you can likely use a popsicle stick. I have access to a lser-cutter, so I precisely cut sticks with mounting holes. See Adobe Illustrator file (laser cut stick.ai) in this repo, if useful.
- sticky-side velcro tape - for mounting the velcro to the platform
- SuperGlue - for gluing the larger platform to the pan/tilt base
- A washer or cardboard (I used both) can help fill in the gap between the base and pan-swivel. This creates more pan-stability on x-axis movements.
- You can also screw the base into something larger - cardboard, a cut piece of plywood (which I gave my students).

Note: This build uses the cheaper-quality nylon-gear micro-servos that most teachers use. The 3D printed model is sized for these. Unfortunately these servos jitter when stressed, and the tilt portion of the base is quite jittery. I've written the code to reduce this. If you have useful changes, do let me know what you come up with!
My students also have higher-quality metal-gear micro-servos for other projects, but these don't fit the 3D model. In the future I may change the model used above so it accomodtes better servos. Stay tuned!

A YouTube video of one build, without base-attachment, with my cat, "Admiral Grace Hoppper", mildly intrigued (Grace often likes to chase rubber pands & thrown twist-ties).
https://youtube.com/shorts/PU9N75umVBI

Wiring Diagram:
<img width="1884" height="1063" alt="Wiring Diagram for Launcher" src="https://github.com/user-attachments/assets/332edca5-55d6-4250-8fbf-99a1685ca17b" />



