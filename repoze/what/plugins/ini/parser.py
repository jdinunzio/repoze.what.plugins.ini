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

from pyparsing import Group
from pyparsing import Literal
from pyparsing import OneOrMore
from pyparsing import Optional
from pyparsing import Or 
from pyparsing import Regex
from pyparsing import Suppress 
from pyparsing import Word
from pyparsing import alphas
from pyparsing import alphanums


# Parser definition
identifier = Word(alphas, alphanums + '_')
comment = Suppress(Regex('#.*'))
header_openpar = Suppress(Literal('['))
header_closepar = Suppress(Literal(']'))

header = header_openpar + identifier + header_closepar
item = identifier + Optional(comment)
body = Group(OneOrMore(Or([item, comment])))
section = Group(header + body)
config = OneOrMore(section)

def parse_INIFile(filename):
    info = {}
    _info = config.parseFile(filename)
    for k, vs in _info:
        info[k] = []
        for v in vs:
            info[k].append(v)
    print info
    return info


if __name__ == '__main__' :
    print parse_INIFile('test.ini')
