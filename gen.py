"""
Image Sprite Generator

Made for MonkeyCrumpets

Instructions on use:
1) Put usernames in users.txt
2) Run script
3) Follow instructions

Enjoy!
"""

import pprint

import urllib2
from PIL import Image

class SpriteGen:
	def __init__(self):
		self.users = self.get_users()
		self.skins = self.get_skins()
		self.coords = self.spritify()
		self.generate_css()
		
		self.log('All done!')
		self.log('1) Copy the CSS from sprites.css and save to the subreddit')
		self.log('2) Upload the spritesheet.png')
		self.log('3) ???')
		self.log('4) PROFIT!')
	
	def get_users(self):
		self.log('Loading users...')
		users = open('users.txt', 'r')
		
		userlist = {'default': 'default'}
		for user in users:
			if (user.startswith('#')):
				continue
			
			user = user.strip()
			user = user.split(':', 1)
			if len(user) == 1:
				user.append(user[0])
			
			userlist[ user[0] ] = user[1]
		
		users.close()
		return userlist
	
	def get_skins(self):
		self.log('Downloading skins...')

		skins = {}
		
		for reddit_user, mc_user in self.users.iteritems():
			if mc_user == 'default':
				url = 'http://minecraft.net/img/char.png'
			else:
				url = 'http://minecraft.net/skin/%s.png' % (mc_user,)
			skin = self.get_skin(url, reddit_user)
			if skin != False:
				skins[reddit_user] = skin

		return skins

	def get_skin(self, url, name):
		try:
			remoteimage = urllib2.urlopen(url)
		except urllib2.HTTPError as errstring:
			self.log('Error downloading skin for %s: %s' % (name, errstring))
			return False
		
		localimage = open('temp/%s.png' % (name,), 'wb')
		localimage.write(remoteimage.read())
		remoteimage.close()
		localimage.close()
		filename = 'temp/%s.png' % (name,)
		self.log('Downloaded skin for %s' % (name,))
		return filename

	def spritify(self):
		self.log('Cropping to just the heads...')
		coords = {}
		start = 0
		spritesheet = Image.new("RGBA", (16 * len(self.skins), 16), (0,0,0,0))
		for user, file in self.skins.iteritems():
			image = Image.open(file)
			image = image.crop((8, 8, 16, 16))
			image = image.resize((16, 16))
			spritesheet.paste(image, (start, 0, (start + 16), 16))
			coords[user] = start
			start = start + 16
		spritesheet.save('spritesheet.png')
		return coords

	def generate_css(self):
		self.log('Generating CSS')
		template = open('template.css', 'r')
		template_css = template.read()
		template.close()
		
		sprite = open('sprite.css', 'r')
		sprite_css = sprite.read()
		sprite.close()
		
		namefile = open('user.css', 'r')
		name_css = namefile.read()
		namefile.close()
		
		user_css = []
		for user, coord in self.coords.iteritems():
			if user == 'default':
				continue
			this_user = sprite_css.replace('%reddit%', user)
			this_user = this_user.replace('%coord%', str(coord))
			user_css.append(this_user)
		
		for user, mc in self.users.iteritems():
			this_user = name_css.replace('%reddit%', user)
			this_user = this_user.replace('%minecraft%', mc)
			user_css.append(this_user)
		
		css = template_css.replace('%users%', '\n'.join(user_css))
		css = css.replace('%defaultcoord%', str(self.coords['default']))
		output = open('sprites.css', 'w')
		output.write(css)
		output.close()

	def log(self, message):
		print message

def __main__():
	sg = SpriteGen()

if __name__ == '__main__':
	__main__()