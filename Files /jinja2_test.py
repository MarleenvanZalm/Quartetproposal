#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


#dependencies:
#   jinja2 ( http://jinja.pocoo.org/ )

# the power of python, rely on code others wrote
import random, string, os, sys
import jinja2, codecs, argparse, time
import randit

html = """

<h1 style="color: {{my_color}}">Hello I am {{whoami}},</h1>

<p>Today is {{date}}, and its around {{time}}</p>

<p>I currently run a {{uname}} machine. It's been on for {{uptime}}.</p>

<p>And here's a random image from my desktop:</br>

<img src="{{image}}"> </img></p>

"""

#variables
whoami = os.popen("whoami").read().strip('\n')
date = os.popen("date '+%A %d %B %Y'").read().strip('\n')
time = os.popen("date '+%H:%M'").read().strip('\n')
uname = os.popen("uname").read().strip('\n')
uptime = os.popen("uptime").read().split()[2].strip(',')
color_list = ['violet', 'salmon', 'slate']
color = random.choice(color_list)

# random image from desktop:
images = []
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
for i in os.listdir(desktop):
    if i.lower().endswith(('.png', '.jpg', '.jpeg', 'gif')):
        images.append(i)
image = os.path.join(desktop, random.choice(images))


template = jinja2.Template(html)

print(template.render(whoami=whoami, my_color=color, date=date, time=time, uname=uname, uptime=uptime, image=image))
