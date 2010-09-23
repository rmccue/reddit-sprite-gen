# Minecraft Sprite Generator
This script generates a large image sprite containing custom skin heads for
each user and puts it before their username via CSS. It also adds Minecraft
usernames after each user's name.

## Requirements
* [Python](http://www.python.org/) (2.6 or 2.7 preferred)
* [Python Imaging Library](http://www.pythonware.com/products/pil/)

## Process
1. Read reddit usernames and Minecraft usernames from users.txt
2. Get skin sprites from the Minecraft site for each user
3. Slice the skin sprites to just get the head, and double the size of this
4. Reconstruct the slices into a new sprite
5. Generate the appropriate positioning CSS for each user, and also create the
   CSS to add their Minecraft names after their username
   
## Setup
1. Put usernames in users.txt in "reddit:minecraft" pairs, or as a single word
   if they are the same
2. Customise the CSS files as needed
3. Run script (`python gen.py`)
4. Upload the spritesheet.png to the subreddit under the name of "spritesheet"
5. Copy and paste the generated CSS into the subreddit's stylesheet
   configuration