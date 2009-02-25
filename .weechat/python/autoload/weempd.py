#Author: Pablo Escobar <pablo__escobar AT tlen DOT pl>
#What it does: This script shows the currently played song in mpd 
#Usage: /weempd - Displays the songname 
#Released under GNU GPL v2 or newer
#
#ported to new API - 0.2.7, by Bonzodog <Bonzodog01 AT gmail DOT com>, 5-2-2009
#/usr/bin/python
#coding: utf-8

import weechat
import re
import codecs
from os import popen

weechat.register ('weempd', 'pablo_escobar','0.2', 'GPL', 'mpd-weechat current song script (usage: /weempd)','','UTF-8')
weechat.hook_command('weempd', '','','','','show_it_to_them')

default = {
  "msg_head": "is playing: ",
  "msg_tail": " with mpd",
  "spacer": " ",
  "colour_title": "C12",
  "colour_spacer": "C08",
}

for k, v in default.items():
  if not weechat.config_get_plugin(k):
    weechat.config_set_plugin(k, v)

def show_it_to_them(server, args):
	spacer = weechat.config_get_plugin("spacer")
	msg_tail = weechat.config_get_plugin("msg_tail")
	msg_head = weechat.config_get_plugin("msg_head")
	colour_title = weechat.config_get_plugin("colour_title")
	colour_spacer = weechat.config_get_plugin("colour_spacer")
	tempinfo = popen('mpc').readline().rstrip()
#	all = '/me ' + msg_head + ' %' + colour_spacer + spacer + ' %' + colour_title + tempinfo + ' %' + colour_spacer + spacer + " %C00" + msg_tail 
	all = '/me plays: ' + tempinfo
	weechat.command(weechat.current_buffer(), all)
	return 0


