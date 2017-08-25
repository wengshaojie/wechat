#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import os
import config

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
def emoji_dealer(l):
    regex = re.compile('^(.*?)(?:<span class="emoji (.*?)"></span>(.*?))+$')
    for m in l: # because m is dict so can be used like this
        match = re.findall(regex, m['NickName'])
        if len(match) > 0: 
            #nickname=''
            emojiname=''
            for str in match[0]:
                if  'emoji' in str:
                   #nickname+=u'口'
                   emojiname+='<img src=\"img/emoji/'+str.replace('emoji','')+'.png\" />'
                else:
                   #nickname+=str
                   emojiname+=str
            m['NickName'] = emojiname
            #m['EmojiName'] = emojiname
            #m['NickName'] = ''.join(match[0])
            #m['EmojiNickName'] = match[0]
        #else:
            #m['EmojiNickName'] = m['NickName']
    return l
def check_file(fileDir):
    try:
        with open(fileDir): pass
        return True
    except:
        return False
