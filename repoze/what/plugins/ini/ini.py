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

"""
Plugin for repoze.what which sources are INI files.

This is a core plugin that provides ``source adapters`` for groups and
permissions stored in a format very similar to INI files.

TODO: Differences between the real INI files and these.

"""

from repoze.what.adapters import BaseSourceAdapter, SourceError

from repoze.what.plugins.ini.parser import parse_INIFile

__all__ = ['INIGroupAdapter', 'INIPermissionsAdapter']


class INIAdapter(BaseSourceAdapter):
    """Base class for INI File adapters."""

    def __init__(self, filename):
        """
        Create an INI file source adapter.

        @param filename: The filename with the sections information.

        """
        super(BaseSourceAdapter, self).__init__()
        # for now, the adapter is read-only
        self.is_writable = False
        self.filename = filename
        self.info = parse_INIFile(self.filename)


    def _get_all_sections(self):
        return self.info

    def _get_section_items(self, section):
        return set(self.info[section])

    def _find_sections(self, hint):
        raise SourceError('This is implemented in the groups and '
                          'permissions adapters.')

    def _include_items(self, section, items):
        raise SourceError('For including items you must edit the '
                          'INI file directly.')

    def _item_is_included(self, section, item):
        return item in self.info[section]

    def _section_exists(self, section):
        return section in self.info


class INIGroupAdapter(INIAdapter):
    """INI Group Adapter."""

    def _find_sections(self, hint):
        userid = hint['repoze.who.userid']
        answer = set()
        for section in self.info.keys():
            if userid in self.info[section]:
                answer.add(section)
        return answer


class INIPermissionsAdapter(INIAdapter):
    """INI Permissions Adapters."""

    def _find_sections(self, hint):
        answer = set()
        for section in self.info.keys():
            if hint in self.info[section]:
                answer.add(section)
        return answer


