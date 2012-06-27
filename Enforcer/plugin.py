###
# Copyright (c) 2012, Gabriel Morell-Pacheco
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.world as world
import supybot.ircmsgs as ircmsgs
import re
import random

class Roar(callbacks.Plugin):
    """Add the help for "@plugin help Roar" here
    This should describe *how* to use this plugin."""
    threaded = True
    noIgnore = True
    def __init__(self, irc):
        self.__parent = super(Roar, self)
        self.__parent.__init__(irc)
        self.lastMsgs = {}
        self.lastStates = {}
        self.logs = {}
        #world.flushers.append(self.flush)
    def doPrivmsg(self,irc,msg):
        caller =  msg.prefix.split('!')[0]#caller= ircdb.users.getUser(msg.prefix)
        text = msg.args[1].lower().split(' ')
        lentext = float(len(text))
        regex = re.compile('r+o+a+r+', flags=re.I)
        
        roarcnt = 0.0
        for x in text:
            if regex.match(x):
                roarcnt += 1.0
                
        if roarcnt/lentext > .9:
            chance =  random.random()
            if chance > .65:
            #irc.sendMsg(ircmsgs.privmsg(msg.args[0],"NO"))
                irc.queueMsg(ircmsgs.kick(msg.args[0], caller, "NO"))
Class = Roar


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
