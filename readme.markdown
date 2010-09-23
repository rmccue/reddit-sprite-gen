# Minecraft Sprite Generator
This script generates a large image sprite containing custom skin heads for
each user and puts it before their username via CSS. It also adds Minecraft
usernames after each user's name.

# Requirements
* Python (2.6 or 2.7 preferred)
* Python Imaging Library

# Process
1. Read reddit usernames and Minecraft usernames from users.txt
2. Get skin sprites from the Minecraft site for each user
3. Slice the skin sprites to just get the head, and double the size of this
4. Reconstruct the slices into a new sprite
5. Generate the appropriate positioning CSS for each user, and also create the
   CSS to add their Minecraft names after their username