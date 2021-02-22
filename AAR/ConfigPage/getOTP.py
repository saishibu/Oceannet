#!/usr/bin/python
from random import randint
import math, random
from PIL import Image, ImageDraw, ImageFont
def get_random_color():
	return randint(120, 200), randint(120, 200), randint(120, 200)

def get_random_code():
	#random characters 
	# codes = [[chr(i) for i in range(48, 58)], [chr(i) for i in range(65, 91)], [chr(i) for i in range(97, 123)]]
	# codes = codes[randint(0, 2)]
	# return codes[randint(0, len(codes)-1)]
	digits = "0123456789"
	otp = ""
	for x in range(4):
		otp += digits[math.floor(random.random()*10)]
	return str(otp)


def generate_captcha(width=140, height=20, length=4):
	#  generate verification code 
	img = Image.new("RGB", (width, height), (250, 250, 250))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("static/font/font.ttf", size=16)
	text = get_random_code()
	
	draw.line((randint(0,140),randint(0,20),randint(0,140),randint(0,20)), fill=get_random_color())
	draw.line((randint(0,140),randint(0,20),randint(0,140),randint(0,20)), fill=get_random_color())
	draw.line((randint(0,140),randint(0,20),randint(0,140),randint(0,20)), fill=get_random_color())
	draw.line((randint(0,140),randint(0,20),randint(0,140),randint(0,20)), fill=get_random_color())
	draw.line((randint(0,140),randint(0,20),randint(0,140),randint(0,20)), fill=get_random_color())
	draw.point((randint(0,140),randint(0,20)), fill= get_random_color())
	draw.point((randint(0,140),randint(0,20)), fill= get_random_color())
	draw.point((randint(0,140),randint(0,20)), fill= get_random_color())
	draw.text((50,0), text, font=font, fill= get_random_color())


	# #captcha text 

	# text = ""
	# for i in range(length):
	# 	c = get_random_code()
	# 	text += c
	# rand_len = randint(-5, 5)
	# draw.text((width * 0.2 * (i+1) + rand_len, height * 0.2 + rand_len), c, font=font, fill=get_random_color())
	# #  add interference line 
	# for i in range(3):
	# 	x1 = randint(0, width)
	# 	y1 = randint(0, height)
	# 	x2 = randint(0, width)
	# 	y2 = randint(0, height)
	# 	draw.line((x1, y1, x2, y2), fill=get_random_color())
	# 	#add interference point 
	# for i in range(16):
	# 	draw.point((randint(0, width), randint(0, height)), fill=get_random_color())
	#save the picture 
	img.save("static/images/captcha.jpg")
	return text