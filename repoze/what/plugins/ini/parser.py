# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008, José Dinuncio <jdinunci@uc.edu.ve>
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

from pyparsing import alphas
from pyparsing import alphanums
from pyparsing import Combine
from pyparsing import Group
from pyparsing import Optional
from pyparsing import restOfLine
from pyparsing import Suppress
from pyparsing import White
from pyparsing import Word
from pyparsing import ZeroOrMore


# Parser definition
#   A little more complicated than is needed today, but needed to preserve 
#   comments in future versions.
identifier = Word(alphas, alphanums + '_-')
blank = White(' \t\n\r\f') #.leaveWhitespace()
comment = Combine(Optional(White(' \t')) + '#' + restOfLine)
comment_header = Optional(Combine(ZeroOrMore(comment | blank)), default='')
comment_inline = Optional(comment, default= '')
item = Group(comment_header + identifier + comment_inline)
section_header = comment_header + Suppress('[') + identifier + Suppress(']') + comment_inline
section_body = Group(ZeroOrMore(item))
section = Group(section_header + Optional(section_body, []))
parser = Group(ZeroOrMore(section)) + Optional(comment_header)
parser.leaveWhitespace()


def parse_INIFile(filename):
    info = {}
    secs, _ = parser.parseFile(filename)
    for _, sec, _, items in secs:
        sec = unicode(sec)
        info[sec] = set()
        for item in items:
            _, v, _ = item
            v = unicode(v)
            info[sec].add(v)
    return info

